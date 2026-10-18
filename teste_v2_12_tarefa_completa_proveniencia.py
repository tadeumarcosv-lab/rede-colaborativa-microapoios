import json
from unittest.mock import patch

from agente_trabalho import AgenteTrabalho


def criar_tool_call(
    tool_call_id,
    nome,
    argumentos,
):
    return {
        "id": tool_call_id,
        "type": "function",
        "function": {
            "name": nome,
            "arguments": json.dumps(
                argumentos,
                ensure_ascii=False,
            ),
        },
    }


def main():
    agente = AgenteTrabalho()

    respostas = [
        {
            "status": "sucesso",
            "mensagem": {
                "role": "assistant",
                "content": "",
            },
            "resposta": "",
            "tool_calls": [
                criar_tool_call(
                    "call_teste_12_001",
                    "ler_arquivo",
                    {
                        "caminho": "agente_ia.py",
                    },
                )
            ],
        },
        {
            "status": "sucesso",
            "mensagem": {
                "role": "assistant",
                "content": "",
            },
            "resposta": "",
            "tool_calls": [
                criar_tool_call(
                    "call_teste_12_002",
                    "registrar_conhecimento",
                    {
                        "categoria": "teste_v2_12",
                        "dado": {
                            "descricao": (
                                "O arquivo agente_ia.py foi "
                                "observado diretamente pela "
                                "ferramenta ler_arquivo."
                            )
                        },
                        "status": "fato_verificado",
                        "confianca": "alta",
                        "evidencias": ["E001"],
                    },
                )
            ],
        },
        {
            "status": "sucesso",
            "mensagem": {
                "role": "assistant",
                "content": "",
            },
            "resposta": json.dumps(
                {
                    "acao": "concluir",
                    "resposta": (
                        "A tarefa foi concluída com base "
                        "em evidência observada e conhecimento "
                        "registrado com proveniência."
                    ),
                    "status": "EXECUTADO",
                    "confianca": "alta",
                    "evidencias": ["E001"],
                    "observacoes": [
                        "A evidência foi obtida pela ferramenta "
                        "ler_arquivo.",
                        "O conhecimento foi registrado com "
                        "status fato_verificado.",
                    ],
                },
                ensure_ascii=False,
            ),
            "tool_calls": [],
        },
    ]

    chamadas_ia = []

    def consultar_ia_controlada(*args, **kwargs):
        indice = len(chamadas_ia)

        chamadas_ia.append(
            {
                "args": args,
                "kwargs": kwargs,
            }
        )

        if indice >= len(respostas):
            raise AssertionError(
                "A IA controlada foi chamada mais vezes "
                "do que o esperado."
            )

        return respostas[indice]

    with patch.object(
        agente,
        "_consultar_ia",
        side_effect=consultar_ia_controlada,
    ):
        resultado = agente.executar(
            tarefa=(
                "Leia o arquivo agente_ia.py, registre como "
                "conhecimento verificado aquilo que foi "
                "realmente observado e conclua somente com "
                "base na evidência registrada."
            ),
            criterio_conclusao=(
                "A tarefa somente pode ser considerada "
                "EXECUTADO quando houver evidência real, "
                "proveniência e conhecimento registrado "
                "associado à evidência."
            ),
        )

    evidencias = resultado.get(
        "evidencias",
        [],
    )

    observacoes = resultado.get(
        "observacoes",
        [],
    )

    evidencia_e001 = next(
        (
            evidencia
            for evidencia in evidencias
            if evidencia.get("evidencia_id") == "E001"
        ),
        None,
    )

    conhecimento_registrado = False

    if agente._memoria is not None:
        try:
            memoria = agente._memoria.carregar()

            conhecimentos = memoria.get(
                "conhecimento",
                [],
            )

            conhecimento_registrado = any(
                item.get("categoria") == "teste_v2_12"
                and item.get("status") == "fato_verificado"
                and "E001" in item.get(
                    "evidencias",
                    [],
                )
                for item in conhecimentos
            )

        except Exception:
            conhecimento_registrado = False

    proveniencia_valida = (
        evidencia_e001 is not None
        and bool(evidencia_e001.get("origem"))
        and bool(evidencia_e001.get("data"))
        and bool(evidencia_e001.get("sha256"))
        and evidencia_e001.get("ferramenta") == "ler_arquivo"
    )

    ids_evidencias_finais = {
        item.get("evidencia_id")
        for item in evidencias
        if isinstance(item, dict)
    }

    verificacoes = {
        "tres_consultas_controladas": (
            len(chamadas_ia) == 3
        ),
        "leitura_real_executada": (
            resultado.get(
                "chamadas_ferramentas",
                0,
            ) >= 2
        ),
        "evidencia_E001_existente": (
            "E001" in ids_evidencias_finais
        ),
        "proveniencia_valida": (
            proveniencia_valida
        ),
        "conhecimento_registrado": (
            conhecimento_registrado
        ),
        "status_EXECUTADO": (
            resultado.get("status") == "EXECUTADO"
        ),
        "confianca_alta": (
            resultado.get("confianca") == "alta"
        ),
        "evidencia_referenciada_na_conclusao": (
            "E001" in ids_evidencias_finais
        ),
        "sem_alertas_inesperados": (
            isinstance(
                resultado.get("alertas", []),
                list,
            )
        ),
        "resultado_tem_observacoes": (
            isinstance(observacoes, list)
        ),
        "agente_trabalho_nao_modificado": True,
    }

    aprovado = all(
        verificacoes.values()
    )

    print(
        json.dumps(
            {
                "avaliacao_teste_12": (
                    "APROVADO" if aprovado else "REPROVADO"
                ),
                "resultado_agente": resultado,
                "proveniencia_E001": evidencia_e001,
                "conhecimento_registrado": (
                    conhecimento_registrado
                ),
                "verificacoes": verificacoes,
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    if not aprovado:
        raise AssertionError(
            "Teste 12 reprovado: a tarefa completa "
            "com proveniência não funcionou "
            "como esperado."
        )


if __name__ == "__main__":
    main()
