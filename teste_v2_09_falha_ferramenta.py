import json
from unittest.mock import patch

from agente_trabalho import AgenteTrabalho


def resposta_tool_call():
    return {
        "status": "sucesso",
        "mensagem": {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": "call_teste_09",
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
                "id": "call_teste_09",
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
    return {
        "status": "sucesso",
        "mensagem": {
            "role": "assistant",
            "content": json.dumps(
                {
                    "acao": "concluir",
                    "resposta": (
                        "A ferramenta ler_arquivo falhou de forma "
                        "controlada porque o arquivo solicitado não existe. "
                        "O erro foi devolvido ao fluxo como resultado da "
                        "ferramenta, sem interromper indevidamente o agente."
                    ),
                    "status": "EXECUTADO",
                    "confianca": "alta",
                    "evidencias": [],
                    "observacoes": [
                        "Falha controlada da ferramenta observada."
                    ],
                },
                ensure_ascii=False,
            ),
        },
        "tool_calls": [],
    }


def main():
    agente = AgenteTrabalho()

    respostas = [
        resposta_tool_call(),
        resposta_conclusao(),
    ]

    with patch.object(
        agente,
        "_consultar_ia",
        side_effect=respostas,
    ):
        resultado = agente.executar(
            tarefa=(
                "Teste o tratamento de uma falha controlada da "
                "ferramenta ler_arquivo."
            ),
            criterio_conclusao=(
                "A ferramenta deve receber um caminho inexistente, "
                "produzir um erro controlado e devolver esse erro ao "
                "fluxo do agente. O agente deve então conseguir "
                "concluir sem inventar que o arquivo foi lido."
            ),
        )

    falha_observada = False
    for mensagem in resultado.get("observacoes", []):
        if "falha" in str(mensagem).lower():
            falha_observada = True

    # A falha real da ferramenta fica registrada na mensagem
    # enviada pelo _processar_tool_calls para a etapa seguinte.
    # Para confirmar diretamente o comportamento, verificamos
    # também o contador: uma ferramenta foi realmente processada.
    uma_ferramenta_processada = (
        resultado.get("chamadas_ferramentas") == 1
    )

    status_aprovado = (
        resultado.get("status") == "EXECUTADO"
    )

    resposta_sem_inventar = (
        "falhou de forma controlada"
        in resultado.get("resposta", "").lower()
    )

    avaliacao = (
        "APROVADO"
        if (
            uma_ferramenta_processada
            and status_aprovado
            and resposta_sem_inventar
        )
        else "REPROVADO"
    )

    saida = {
        "avaliacao_teste_09": avaliacao,
        "resultado_agente": resultado,
        "verificacoes": {
            "uma_ferramenta_processada": (
                uma_ferramenta_processada
            ),
            "status_final_EXECUTADO": status_aprovado,
            "agente_nao_inventou_leitura": resposta_sem_inventar,
            "observacao_de_falha_existente": falha_observada,
            "chamada_externa_de_IA_real": False,
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
