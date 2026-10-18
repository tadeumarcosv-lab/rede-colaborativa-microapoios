import json
from unittest.mock import patch

import agente_trabalho
from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    # Mantemos o mecanismo original do agente.
    # Apenas reduzimos o limite da instância para tornar o teste
    # determinístico e rápido.
    agente.TIMEOUT_TOTAL_S = 1.0

    # Evita efeitos externos do teste sobre memória e eventos.
    agente._registrar_historico_tarefa = lambda resultado: None
    agente._registrar_evento = lambda **kwargs: None

    # O executar() chama time.monotonic() em pontos conhecidos:
    #
    # 1. início da execução -> 100.0
    # 2. primeira verificação do timeout -> 101.0
    # 3. cálculo final da duração -> 101.0
    #
    # Como o limite é 1 segundo, 101.0 - 100.0 >= 1.0.
    # Portanto, o ramo real de timeout do executar() deve ser acionado.
    valores_relogio = [
        100.0,
        101.0,
        101.0,
    ]

    with patch.object(
        agente_trabalho.time,
        "monotonic",
        side_effect=valores_relogio,
    ):
        resultado = agente.executar(
            tarefa=(
                "Verifique se o mecanismo cooperativo de tempo "
                "é acionado quando o limite configurado é atingido."
            ),
            criterio_conclusao=(
                "O teste deve comprovar o acionamento do limite "
                "cooperativo de tempo através do resultado real "
                "produzido por AgenteTrabalho.executar()."
            ),
        )

    observacoes = resultado.get("observacoes", [])

    timeout_observado = (
        "Limite cooperativo de tempo atingido."
        in observacoes
    )

    status_correto = (
        resultado.get("status")
        == "EXECUTADO_PARCIALMENTE"
    )

    iteracao_correta = (
        resultado.get("iteracoes") == 1
    )

    nenhuma_ferramenta = (
        resultado.get("chamadas_ferramentas") == 0
    )

    avaliacao = (
        "APROVADO"
        if (
            timeout_observado
            and status_correto
            and iteracao_correta
            and nenhuma_ferramenta
        )
        else "REPROVADO"
    )

    saida = {
        "avaliacao_teste_08": avaliacao,
        "resultado_agente": resultado,
        "verificacoes": {
            "timeout_observado": timeout_observado,
            "status_EXECUTADO_PARCIALMENTE": status_correto,
            "primeira_iteracao_interrompida": iteracao_correta,
            "nenhuma_ferramenta_executada": nenhuma_ferramenta,
            "limite_configurado_segundos": (
                agente.TIMEOUT_TOTAL_S
            ),
            "relogio_controlado": True,
            "chamada_externa_de_IA_necessaria": False,
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
