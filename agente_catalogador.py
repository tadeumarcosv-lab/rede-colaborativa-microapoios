from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)

CATALOGO_AGENTES = []

class AgenteCatalogador:

    def __init__(self):

        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

    def catalogar(self, nome_agente):

        if nome_agente not in CATALOGO_AGENTES:

            CATALOGO_AGENTES.append(
                nome_agente
            )

            self.ocorrencias.registrar(
                "CATALOGO",
                f"Agente catalogado: {nome_agente}"
            )

        return nome_agente

    def listar_catalogo(self):

        return CATALOGO_AGENTES

    def quantidade_catalogada(self):

        return len(
            CATALOGO_AGENTES
        )

if __name__ == "__main__":

    catalogador = (
        AgenteCatalogador()
    )

    catalogador.catalogar(
        "agente_exemplo"
    )

    print(
        catalogador.listar_catalogo()
    )

    print(
        catalogador.quantidade_catalogada()
        )
