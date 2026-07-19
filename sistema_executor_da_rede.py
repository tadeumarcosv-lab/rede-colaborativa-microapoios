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

        self.historico = []

        self.status = "ATIVO"

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[EXECUTOR] [{horario}] {mensagem}"

        self.historico.append(registro)

        print(registro)

    def obter_status(self):

        return {
            "status": self.status,
            "ativo": self.ativo,
            "ciclo_atual": self.ciclo
        }

    def obter_historico(self):

        return self.historico

    def iniciar(self):

        self.ativo = True

        self.status = "ATIVO"

        self.registrar("Sistema Executor ativado.")

    def parar(self):

        self.ativo = False

        self.status = "PARADO"

        self.registrar("Sistema Executor encerrado.")

    def reiniciar(self):

        self.registrar("Reiniciando Sistema Executor.")

        self.ativo = True

        self.status = "ATIVO"

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

        return True

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
