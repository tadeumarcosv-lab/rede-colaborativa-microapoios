from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)

from painel_agentes import (
    AGENTES_ATIVOS
)


class AgenteObservador:

    def __init__(self):

        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

    def observar_agentes(self):

        alertas = []

        for agente, status in (
            AGENTES_ATIVOS.items()
        ):

            if not status:

                alerta = (
                    f"{agente} desligado"
                )

                alertas.append(
                    alerta
                )

                self.ocorrencias.registrar(
                    "OBSERVACAO",
                    alerta
                )

        return alertas

    def gerar_alertas(self):

        return {
            "alertas":
                self.observar_agentes()
        }


if __name__ == "__main__":

    observador = (
        AgenteObservador()
    )

    print(
        observador.gerar_alertas()
      )
