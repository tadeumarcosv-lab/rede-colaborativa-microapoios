"""
SISTEMA EXECUTOR DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_EXECUTOR_DA_REDE.md
"""

from datetime import datetime


class SistemaExecutorDaRede:

    def __init__(self):

        self.status = "ATIVO"

        self.filas = []

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[EXECUTOR] [{horario}] {mensagem}")

    def receber_tarefa(self, tarefa):

        self.filas.append(tarefa)

        self.registrar(f"Tarefa adicionada: {tarefa}")

    def executar_filas(self):

        self.registrar("Executando filas.")

        while self.filas:

            tarefa = self.filas.pop(0)

            self.registrar(f"Executando: {tarefa}")

    def finalizar_execucao(self):

        self.registrar("Execução concluída.")

    def executar(self):

        self.registrar("Sistema Executor iniciado.")

        self.receber_tarefa("Inicialização da Rede")

        self.receber_tarefa("Verificação de Integridade")

        self.receber_tarefa("Planejamento")

        self.receber_tarefa("Construção")

        self.receber_tarefa("Aprendizado")

        self.executar_filas()

        self.finalizar_execucao()


if __name__ == "__main__":

    executor = SistemaExecutorDaRede()

    executor.executar()
