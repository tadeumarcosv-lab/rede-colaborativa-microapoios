from datetime import datetime

from nucleo_operacional.agente_central import AgenteCentral
from nucleo_operacional.agente_coordenacao import AgenteCoordenacao
from nucleo_operacional.agente_comunicacao import AgenteComunicacao
from nucleo_operacional.agente_pesquisa_avancada import AgentePesquisaAvancada
from nucleo_operacional.agente_memoria_estrategica import AgenteMemoriaEstrategica
from nucleo_operacional.agente_gestao_conhecimento import AgenteGestaoConhecimento

from config_nucleo import *


class IntegracaoCompleta:

    def __init__(self):

        self.status = "ATIVO"

        self.agentes = [
            "Comunicação",
            "Coordenação",
            "Central",
            "Pesquisa",
            "Memória",
            "Conhecimento"
        ]

        self.central = AgenteCentral()
        self.coordenacao = AgenteCoordenacao()
        self.comunicacao = AgenteComunicacao()
        self.pesquisa = AgentePesquisaAvancada()
        self.memoria = AgenteMemoriaEstrategica()
        self.conhecimento = AgenteGestaoConhecimento()

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[INTEGRACAO] [{horario}] {mensagem}")

    def listar_agentes(self):

        self.registrar("Agentes operacionais ativos:")

        for agente in self.agentes:

            self.registrar(f"- {agente}")

        return self.agentes

    def verificar_status(self):

        self.registrar(f"Status da integração: {self.status}")

        return self.status

    def executar(self, solicitacao):

        self.registrar("Iniciando integração completa.")

        self.verificar_status()

        self.listar_agentes()

        etapa1 = self.comunicacao.executar(solicitacao)

        etapa2 = self.coordenacao.executar(etapa1)

        etapa3 = self.central.executar(etapa2)

        etapa4 = self.pesquisa.executar(etapa3)

        etapa5 = self.memoria.executar(etapa4)

        etapa6 = self.conhecimento.executar(etapa5)

        self.registrar("Integração concluída com sucesso.")

        return etapa6


if __name__ == "__main__":

    sistema = IntegracaoCompleta()

    resultado = sistema.executar(
        "Teste de integração completa"
    )

    print(resultado)
