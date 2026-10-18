import json
from unittest.mock import patch

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    conclusao = {
        "acao": "concluir",
        "resposta": (
            "A tarefa foi considerada executada, "
            "mas não há evidências suficientes para confirmar."
        ),
        "status": "EXECUTADO",
        "confianca": "insuficiente",
        "evidencias": [],
        "observacoes": [
            "A conclusão foi fornecida sem evidências verificáveis."
        ],
    }

    conteudo_json = json.dumps(
        conclusao,
        ensure_ascii=False,
    )

    resposta_ia_controlada = {
        "status": "sucesso",
        "mensagem": {
            "role": "assistant",
            "content": conteudo_json,
        },
        "resposta": conteudo_json,
        "tool_calls": [],
    }

    chamadas = []

    def consultar_ia_controlada(*args, **kwargs):
        chamadas.append(
            {
                "args": args,
                "kwargs": kwargs,
            }
        )
        return resposta_ia_controlada

    with patch.object(
        agente,
        "_consultar_ia",
        side_effect=consultar_ia_controlada,
    ):
        resultado = agente.executar(
            tarefa=(
                "Avalie uma conclusão sem evidências verificáveis "
                "e com confiança insuficiente."
            ),
            criterio_conclusao=(
                "Uma conclusão sem evidências verificáveis não pode "
                "permanecer como EXECUTADO."
            ),
        )

    status_final = resultado.get("status")
    confianca_final = resultado.get("confianca")
    evidencias = resultado.get("evidencias", [])
    observacoes = resultado.get("observacoes", [])

    verificacoes = {
        "IA_controlada_chamada": len(chamadas) == 1,
        "status_nao_permaneceu_EXECUTADO": (
            status_final != "EXECUTADO"
        ),
        "status_PROPOSTO": (
            status_final == "PROPOSTO"
        ),
        "confianca_insuficiente": (
            confianca_final == "insuficiente"
        ),
        "sem_evidencias_inventadas": (
            len(evidencias) == 0
        ),
        "resultado_tem_observacoes": (
            isinstance(observacoes, list)
        ),
        "agente_trabalho_modificado": False,
    }

    aprovado = all(verificacoes.values())

    print(
        json.dumps(
            {
                "avaliacao_teste_10": (
                    "APROVADO" if aprovado else "REPROVADO"
                ),
                "resultado_agente": resultado,
                "verificacoes": verificacoes,
            },
            ensure_ascii=False,
            indent=2,
        )
    )

    if not aprovado:
        raise AssertionError(
            "Teste 10 reprovado: a proteção contra "
            "conclusão sem evidências não funcionou "
            "como esperado."
        )


if __name__ == "__main__":
    main()
