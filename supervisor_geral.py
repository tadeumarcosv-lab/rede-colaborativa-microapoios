"""
SUPERVISOR GERAL DA REDE COLABORATIVA DE MICROAPOIOS
Autor: Tadeu Marcos Viana

Responsável por supervisionar continuamente toda a Rede.
"""

from datetime import datetime


class SupervisorGeral:

    def __init__(self):
        self.status = "ATIVO"

    def registrar(self, mensagem):
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[SUPERVISOR] [{horario}] {mensagem}")

    def verificar(self):
        self.registrar("Verificando funcionamento geral da Rede...")

    def monitorar(self):
        self.registrar("Monitoramento contínuo iniciado.")

    def executar(self):
        self.registrar("Supervisor Geral iniciado.")
        self.verificar()
        self.monitorar()


if __name__ == "__main__":
    supervisor = SupervisorGeral()
    supervisor.executar()
