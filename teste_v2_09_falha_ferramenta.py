import json
from unittest.mock import patch

from agente_trabalho import AgenteTrabalho


def resposta_tool_call():
    """
    Primeira resposta controlada da IA:
    solicita uma leitura de arquivo que não existe.
    """
    return {
        "status": "sucesso",
        "mensagem": {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": "call_teste_09_1",
                    "type": "function",
                    "function": {
                        "name": "ler_arquivo",
                        "arguments": json.dumps(
                            {
                                "caminho": (
                                    "__arquivo_inexistente_teste_09__.py"
                                )
                            },
                            ensure_ascii=False,
                        ),
                    },
                }
            ],
        },
        "tool_calls": [
            {
                "id": "call_teste_09_1",
                "type": "function",
                "function": {
                    "name": "ler_arquivo",
                    "arguments": json.dumps(
                        {
                            "caminho": (
                                "__arquivo_inexistente_teste_09__.py"
                            )
                        },
                        ensure_ascii=False,
                    ),
                },
            }
        ],
    }


def resposta_conclusao():
    """
    Segunda resposta controlada da IA.
    O campo 'resposta' é obrigatório porque é esse campo
    que AgenteTrabalho.executar() utiliza para interpretar
    a conclusão.
    """
    return {
        "status": "sucesso",
        "mensagem": {
            "role": "assistant",
            "content": (
                '{"acao":"concluir",'
                '"resposta":"A falha da ferramenta foi observada e tratada '
                'sem inventar que o arquivo foi lido.",'
                '"status":"PROPOSTO",'
                '"confianca":"insuficiente",'
                '"evidencias":[],'
                '"observacoes":["Falha controlada da ferramenta observada."]}'
            ),
        },
        "resposta": (
            '{"acao":"concluir",'
            '"resposta":"A falha da ferramenta foi observada e tratada '
            'sem inventar que o arquivo foi lido.",'
            '"status":"PROPOSTO",'
            '"confianca":"insuficiente",'
            '"evidencias":[],'
            '"observacoes":["Falha controlada da ferramenta observada."]}'
        ),
        "tool_calls": [],
    }


def main():
    agente = AgenteTrabalho()

    mensagens_finais = []

    processador_original = agente._processar_tool_calls

    def processar_e_capturar(mensagens, tool_calls):
        resultado = processador_original(
            mensagens,
            tool_calls,
        )

        # Captura somente a mensagem de resultado da ferramenta.
        for mensagem in resultado:
            if (
                isinstance(mensagem, dict)
                and mensagem.get("role") == "tool"
            ):
                mensagens_finais.append(
                    dict(mensagem)
                )

        return resultado

    respostas = [
        resposta_tool_call(),
        resposta_conclusao(),
    ]

    with patch.object(
        agente,
        "_consultar_ia",
        side_effect=respostas,
    ):
        with patch.object(
            agente,
            "_processar_tool_calls",
            side_effect=processar_e_capturar,
        ):
            resultado = agente.executar(
                tarefa=(
                    "Teste o tratamento de uma falha controlada "
                    "da ferramenta ler_arquivo."
                ),
                criterio_conclusao=(
                    "A ferramenta deve receber um caminho inexistente, "
                    "produzir um erro controlado e devolver esse erro "
                    "ao fluxo do agente. O agente não deve inventar "
                    "que o arquivo foi lido."
                ),
            )

    falha_tool_observada = False
    tipo_erro = None
    mensagem_erro = None

    if mensagens_finais:
        conteudo = mensagens_finais[0].get(
            "content",
            "",
        )

        try:
            dados_tool = json.loads(conteudo)

            falha_tool_observada = (
                dados_tool.get("sucesso") is False
            )

            tipo_erro = dados_tool.get("erro")
            mensagem_erro = dados_tool.get("mensagem")

        except (
            TypeError,
            json.JSONDecodeError,
        ):
            pass

    chamada_registrada = (
        resultado.get("chamadas_ferramentas") == 1
    )

    erro_esperado = (
        tipo_erro == "FileNotFoundError"
    )

    mensagem_esperada = (
        isinstance(mensagem_erro, str)
        and "Arquivo não encontrado" in mensagem_erro
    )

    nao_inventou_leitura = (
        resultado.get("status") != "EXECUTADO"
        or not resultado.get("evidencias")
    )

    avaliacao = (
        "APROVADO"
        if (
            falha_tool_observada
            and chamada_registrada
            and erro_esperado
            and mensagem_esperada
            and nao_inventou_leitura
        )
        else "REPROVADO"
    )

    saida = {
        "avaliacao_teste_09": avaliacao,
        "resultado_agente": resultado,
        "resultado_real_da_ferramenta": {
            "capturado": bool(mensagens_finais),
            "sucesso": (
                False if falha_tool_observada else None
            ),
            "erro": tipo_erro,
            "mensagem": mensagem_erro,
        },
        "verificacoes": {
            "falha_da_ferramenta_observada": (
                falha_tool_observada
            ),
            "uma_chamada_de_ferramenta": (
                chamada_registrada
            ),
            "erro_FileNotFoundError": (
                erro_esperado
            ),
            "mensagem_de_arquivo_nao_encontrado": (
                mensagem_esperada
            ),
            "agente_nao_inventou_leitura": (
                nao_inventou_leitura
            ),
            "chamada_real_da_Groq": False,
            "agente_trabalho_modificado": False,
        },
    }

    print(
        json.dumps(
            saida,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
