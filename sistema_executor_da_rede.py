"""
SISTEMA EXECUTOR DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por manter o ciclo operacional da Rede.
"""

from datetime import datetime
import time

from motor_de_aprendizado import MotorDeAprendizado


class SistemaExecutorDaRede:

    def __init__(self):

        self.aprendizado = MotorDeAprendizado()

        self.ativo = True

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[EXECUTOR] [{horario}] {mensagem}")

    def executar_ciclo(self):

        self.registrar("Executando ciclo operacional.")

        self.aprendizado.executar()

        self.registrar("Ciclo operacional concluído.")

    def executar(self):

        self.registrar("Sistema Executor iniciado.")

        self.executar_ciclo()

        self.registrar("Sistema Executor finalizado.")


if __name__ == "__main__":

    executor = SistemaExecutorDaRede()

    executor.executar()
