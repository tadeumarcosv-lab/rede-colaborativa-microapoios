from gerenciador_ocorrencias import GerenciadorOcorrencias


AGENTES_CADASTRADOS = []


class AgenteConstrutor:

    def __init__(self):

        self.ocorrencias = GerenciadorOcorrencias()

    def registrar_agente(self, nome_agente):

        AGENTES_CADASTRADOS.append(nome_agente)

        self.ocorrencias.registrar(
            "CONSTRUCAO",
            f"Agente registrado: {nome_agente}"
        )

        return f"Agente {nome_agente} registrado"

    def listar_agentes(self):

        return AGENTES_CADASTRADOS

    def quantidade_agentes(self):

        return len(AGENTES_CADASTRADOS)


if __name__ == "__main__":

    construtor = AgenteConstrutor()

    print(
        construtor.registrar_agente(
            "agente_exemplo"
        )
    )

    print(
        construtor.listar_agentes()
    )

    print(
        construtor.quantidade_agentes()
)
