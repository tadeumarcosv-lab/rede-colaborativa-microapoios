"""
ORQUESTRADOR DO NÚCLEO
Rede Colaborativa de Microapoios

Responsável por coordenar os principais agentes
operacionais da Rede utilizando a arquitetura
baseada em classes.
"""

from agente_comunicacao import AgenteComunicacao
from agente_coordenacao import AgenteCoordenacao
from agente_central import AgenteCentral


class OrquestradorNucleo:

    def __init__(self):

        self.comunicacao = AgenteComunicacao()
        self.coordenacao = AgenteCoordenacao()
        self.central = AgenteCentral()

    def executar(self, mensagem):

        etapa1 = self.comunicacao.executar(
            mensagem
        )

        etapa2 = self.coordenacao.executar(
            etapa1
        )

        etapa3 = self.central.executar(
            etapa2
        )

        return etapa3


if __name__ == "__main__":

    orquestrador = OrquestradorNucleo()

    resultado = orquestrador.executar(
        "Teste do Orquestrador do Núcleo"
    )

    print(resultado)
