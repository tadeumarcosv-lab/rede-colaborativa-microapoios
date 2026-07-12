from nucleo_operacional.agente_central import AgenteCentral
from nucleo_operacional.agente_coordenacao import AgenteCoordenacao
from nucleo_operacional.agente_comunicacao import AgenteComunicacao
from nucleo_operacional.agente_pesquisa_avancada import AgentePesquisaAvancada
from nucleo_operacional.agente_memoria_estrategica import AgenteMemoriaEstrategica
from nucleo_operacional.agente_gestao_conhecimento import AgenteGestaoConhecimento
from nucleo_operacional.config_nucleo import *


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

        return etapa6


if __name__ == "__main__":

    sistema = IntegracaoCompleta()

    resultado = sistema.executar(
        "Teste de integração completa"
    )

    print(resultado)
