"""
ORQUESTRADOR CENTRAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Coordena o ciclo mínimo de funcionamento da Rede.
"""

from datetime import datetime

from sistema_executor_da_rede import SistemaExecutorDaRede


class OrquestradorCentralDaRede:

    def __init__(self):

        self.executor = SistemaExecutorDaRede()

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[ORQUESTRADOR] [{horario}] {mensagem}")

    def executar(self):

        self.registrar("Orquestrador Central iniciado.")

        self.executor.executar()

        self.registrar("Ciclo principal da Rede concluído.")


if __name__ == "__main__":

    orquestrador = OrquestradorCentralDaRede()

    orquestrador.executar()
