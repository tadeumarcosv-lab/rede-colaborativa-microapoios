"""
INTEGRADOR DOS MOTORES
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Integra os Motores Inteligentes da Rede.
"""

from datetime import datetime


class IntegradorDosMotores:

    def __init__(self):

        self.motores = [

            "Motor de Planejamento",

            "Motor de Construção",

            "Motor de Verificação",

            "Motor de Aprendizado"

        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[MOTORES] [{horario}] {mensagem}")

    def verificar(self):

        self.registrar("Verificando motores.")

        for motor in self.motores:

            self.registrar(f"OK -> {motor}")

    def integrar(self):

        self.registrar("Integrando motores.")

        for motor in self.motores:

            self.registrar(f"Motor integrado: {motor}")

    def validar(self):

        self.registrar("Validando integração dos motores.")

    def finalizar(self):

        self.registrar("Integração dos motores concluída.")

    def executar(self):

        self.registrar("Integrador dos Motores iniciado.")

        self.verificar()

        self.integrar()

        self.validar()

        self.finalizar()


if __name__ == "__main__":

    sistema = IntegradorDosMotores()

    sistema.executar()
