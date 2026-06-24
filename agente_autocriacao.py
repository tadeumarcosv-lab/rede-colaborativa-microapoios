from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)

from agente_evolucao import (
    AgenteEvolucao
)

AGENTES_CRIADOS = []

class AgenteAutocriacao:

    def __init__(self):

        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

        self.evolucao = (
            AgenteEvolucao()
        )

    def analisar_necessidades(self):

        plano = (
            self.evolucao.gerar_plano_evolucao()
        )

        return plano

    def criar_agente(self, nome_agente):

        AGENTES_CRIADOS.append(
            nome_agente
        )

        self.ocorrencias.registrar(
            "AUTOCRIACAO",
            f"Agente criado: {nome_agente}"
        )

        return {
