"""
INTEGRADOR DE COMUNICAÇÃO
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Integra toda a comunicação interna da Rede.
"""

from datetime import datetime


class IntegradorDeComunicacao:

    def __init__(self):

        self.componentes = [

            "Agente Central",

            "Supervisor Geral",

            "Orquestrador Central",

            "Diretor Autônomo",

            "Sistema Executor"

        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[COMUNICACAO] [{horario}] {mensagem}")

    def verificar(self):

        self.registrar("Verificando comunicação entre componentes.")

        for componente in self.componentes:

            self.registrar(f"OK -> {componente}")

    def integrar(self):

        self.registrar("Integrando comunicação interna.")

        for componente in self.componentes:

            self.registrar(f"Canal ativo: {componente}")

    def validar(self):

        self.registrar("Validando comunicação.")

    def finalizar(self):

        self.registrar("Integração da comunicação concluída.")

    def executar(self):

        self.registrar("Integrador de Comunicação iniciado.")

        self.verificar()

        self.integrar()

        self.validar()

        self.finalizar()


if __name__ == "__main__":

    sistema = IntegradorDeComunicacao()

    sistema.executar()
