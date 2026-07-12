"""
ORQUESTRADOR CENTRAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Coordena o ciclo mínimo de funcionamento da Rede.
"""

from datetime import datetime

from sistema_executor_da_rede import SistemaExecutorDaRede
from motor_de_aprendizado import MotorDeAprendizado
from sistema_de_memoria_persistente import SistemaDeMemoriaPersistente


class OrquestradorCentralDaRede:

    def __init__(self):

        self.executor = SistemaExecutorDaRede()
        self.aprendizado = MotorDeAprendizado()
        self.memoria = SistemaDeMemoriaPersistente()

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[ORQUESTRADOR] [{horario}] {mensagem}")

    def executar(self):

        self.registrar("Orquestrador Central iniciado.")

        self.executor.executar()

        self.aprendizado.executar()

        self.memoria.adicionar(
            "Orquestrador",
            "Ciclo mínimo executado com sucesso."
        )

        self.registrar("Ciclo principal da Rede concluído.")


if __name__ == "__main__":

    orquestrador = OrquestradorCentralDaRede()

    orquestrador.executar()
