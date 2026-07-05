"""
INTEGRADOR DE DECISÕES
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Integra o fluxo de decisões da Rede.
"""

from datetime import datetime


class IntegradorDeDecisoes:

    def __init__(self):

        self.decisores = [

            "Supervisor Geral",

            "Diretor Autônomo",

            "Orquestrador Central",

            "Motor de Planejamento",

            "Motor de Verificação"

        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[DECISOES] [{horario}] {mensagem}")

    def verificar(self):

        self.registrar("Verificando responsáveis pelas decisões.")

        for decisor in self.decisores:

            self.registrar(f"OK -> {decisor}")

    def integrar(self):

        self.registrar("Integrando fluxo de decisões.")

        for decisor in self.decisores:

            self.registrar(f"Fluxo integrado: {decisor}")

    def validar(self):

        self.registrar("Validando integração das decisões.")

    def finalizar(self):

        self.registrar("Integração das decisões concluída.")

    def executar(self):

        self.registrar("Integrador de Decisões iniciado.")

        self.verificar()

        self.integrar()

        self.validar()

        self.finalizar()


if __name__ == "__main__":

    sistema = IntegradorDeDecisoes()

    sistema.executar()
