from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)

from painel_agentes import (
    AGENTES_ATIVOS
)


class AgenteArquiteto:

    def __init__(self):

        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

    def analisar_estrutura(self):

        sugestoes = []

        total_agentes = (
            len(AGENTES_ATIVOS)
        )

        if total_agentes < 15:

            sugestoes.append(
                "Criar novos agentes especializados"
            )

        for agente, status in (
            AGENTES_ATIVOS.items()
        ):

            if not status:

                sugestoes.append(
                    f"Revisar agente {agente}"
                )

        return sugestoes

    def gerar_plano(self):

        plano = {

            "agentes_ativos":
                len(AGENTES_ATIVOS),

            "sugestoes":
                self.analisar_estrutura()
        }

        self.ocorrencias.registrar(
            "ARQUITETURA",
            "Plano gerado"
        )

        return plano


if __name__ == "__main__":

    arquiteto = (
        AgenteArquiteto()
    )

    print(
        arquiteto.gerar_plano()
)
