from agente_central import AgenteCentral
from agente_coordenacao import AgenteCoordenacao
from agente_comunicacao import AgenteComunicacao
from agente_pesquisa_avancada import AgentePesquisaAvancada
from agente_memoria_estrategica import AgenteMemoriaEstrategica
from agente_gestao_conhecimento import AgenteGestaoConhecimento
from config_nucleo import *

from motor_de_aprendizado import MotorDeAprendizado


class IntegracaoCompleta:

    def __init__(self):

        self.central = AgenteCentral()
        self.coordenacao = AgenteCoordenacao()
        self.comunicacao = AgenteComunicacao()
        self.pesquisa = AgentePesquisaAvancada()
        self.memoria = AgenteMemoriaEstrategica()
        self.conhecimento = AgenteGestaoConhecimento()

    def executar(self, solicitacao):

        etapa1 = self.comunicacao.executar(solicitacao)

        etapa2 = self.coordenacao.executar(etapa1)

        etapa3 = self.central.executar(etapa2)

        etapa4 = self.pesquisa.executar(etapa3)

        etapa5 = self.memoria.executar(etapa4)

        etapa6 = self.conhecimento.executar(etapa5)

        # Primeiro componente autônomo integrado
        aprendizado = MotorDeAprendizado()
        aprendizado.executar()

        return etapa6


if __name__ == "__main__":

    sistema = IntegracaoCompleta()

    resultado = sistema.executar(
        "Teste de integração completa"
    )

    print(resultado)
