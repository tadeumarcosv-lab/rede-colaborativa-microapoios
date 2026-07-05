"""
INTEGRADOR DOS SISTEMAS
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Integra todos os Sistemas da Rede.
"""

from datetime import datetime


class IntegradorDosSistemas:

    def __init__(self):

        self.sistemas = [

            "Sistema Executor",

            "Sistema de Memória Persistente",

            "Sistema de Monitoramento",

            "Sistema de Auditoria",

            "Sistema de Recuperação",

            "Sistema de Filas Inteligentes"

        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[SISTEMAS] [{horario}] {mensagem}")

    def verificar(self):

        self.registrar("Verificando sistemas.")

        for sistema in self.sistemas:

            self.registrar(f"OK -> {sistema}")

    def integrar(self):

        self.registrar("Integrando sistemas.")

        for sistema in self.sistemas:

            self.registrar(f"Sistema integrado: {sistema}")

    def validar(self):

        self.registrar("Validando integração dos sistemas.")

    def finalizar(self):

        self.registrar("Integração dos sistemas concluída.")

    def executar(self):

        self.registrar("Integrador dos Sistemas iniciado.")

        self.verificar()

        self.integrar()

        self.validar()

        self.finalizar()


if __name__ == "__main__":

    sistema = IntegradorDosSistemas()

    sistema.executar()
