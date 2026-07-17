"""
SISTEMA EXECUTOR DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana
"""

from datetime import datetime
import os
import time

from motor_de_aprendizado import MotorDeAprendizado
from registro_central_eventos import RegistroCentralEventos


class SistemaExecutorDaRede:

    def __init__(self):

        self.aprendizado = MotorDeAprendizado()

        self.registro = RegistroCentralEventos()

        self.ativo = True

        self.ciclo = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[EXECUTOR] [{horario}] {mensagem}")

    def obter_status(self):
        """
        Retorna o estado atual do Sistema Executor.
        """

        return {

            "ativo": self.ativo,

            "ciclo_atual": self.ciclo

        }

    def iniciar(self):
        """
        Ativa o Sistema Executor.
        """

        self.ativo = True

        self.registrar("Sistema Executor ativado.")

    def parar(self):
        """
        Encerra o ciclo contínuo.
        """

        self.ativo = False

        self.registrar("Sistema Executor encerrado.")

    def reiniciar(self):
        """
        Reinicia o Sistema Executor.
        """

        self.registrar("Reiniciando Sistema Executor.")

        self.ativo = True

        self.ciclo = 0

    def executar_ciclo(self):

        self.ciclo += 1

        self.registrar(f"Iniciando ciclo {self.ciclo}")

        self.registro.registrar(

            origem="Sistema Executor",

            destino="Motor de Aprendizado",

            responsavel="Sistema",

            descricao=f"Início do ciclo {self.ciclo}",

            resultado="EXECUTANDO",

            importancia="NORMAL"

        )

        self.aprendizado.executar()

        self.registro.registrar(

            origem="Motor de Aprendizado",

            destino="Sistema Executor",

            responsavel="Sistema",

            descricao=f"Fim do ciclo {self.ciclo}",

            resultado="OK",

            importancia="NORMAL"

        )

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
