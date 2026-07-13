"""
SISTEMA EXECUTOR DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana
"""

from datetime import datetime
import os
import time

from motor_de_aprendizado import MotorDeAprendizado


class SistemaExecutorDaRede:

    def __init__(self):

        self.aprendizado = MotorDeAprendizado()

        self.ativo = True

        self.ciclo = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[EXECUTOR] [{horario}] {mensagem}")

    def executar_ciclo(self):

        self.ciclo += 1

        self.registrar(f"Iniciando ciclo {self.ciclo}")

        self.aprendizado.executar()

        self.registrar(f"Finalizando ciclo {self.ciclo}")

    def executar(self):

        self.registrar("Sistema Executor iniciado.")

        modo_teste = os.getenv("GITHUB_ACTIONS") == "true"

        if modo_teste:

            self.registrar("Modo TESTE detectado.")

            for _ in range(3):

                self.executar_ciclo()

            self.registrar("Teste concluído.")

        else:

            self.registrar("Modo CONTÍNUO iniciado.")

            while self.ativo:

                self.executar_ciclo()

                time.sleep(5)


if __name__ == "__main__":

    executor = SistemaExecutorDaRede()

    executor.executar()
