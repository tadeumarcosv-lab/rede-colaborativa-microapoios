from painel_agentes import AGENTES_ATIVOS

from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)


class AgenteAuditor:

    def __init__(self):

        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

    def verificar_agentes(self):

        relatorio = []

        for agente, status in (
            AGENTES_ATIVOS.items()
        ):

            if status:

                relatorio.append(
                    f"{agente}: OK"
                )

            else:

                relatorio.append(
                    f"{agente}: DESLIGADO"
                )

        return relatorio

    def gerar_relatorio(self):

        return {
            "agentes":
                self.verificar_agentes(),

            "ocorrencias":
                self.ocorrencias.listar()
        }


if __name__ == "__main__":

    auditor = AgenteAuditor()

    print(
        auditor.gerar_relatorio()
)
