"""
SISTEMA DE FILAS INTELIGENTES
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_FILAS_INTELIGENTES.md
"""

from datetime import datetime


class SistemaDeFilasInteligentes:

    def __init__(self):

        self.status = "ATIVO"

        self.fila = []

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[FILAS] [{horario}] {mensagem}")

    def adicionar_tarefa(self, prioridade, tarefa):

        self.fila.append({

            "prioridade": prioridade,

            "tarefa": tarefa

        })

        self.registrar(f"Tarefa adicionada: {tarefa}")

    def organizar_fila(self):

        self.fila.sort(

            key=lambda item: item["prioridade"]

        )

        self.registrar("Fila organizada por prioridade.")

    def executar_fila(self):

        self.registrar("Executando fila inteligente.")

        while self.fila:

            tarefa = self.fila.pop(0)

            self.registrar(

                f'Executando: {tarefa["tarefa"]}'

            )

    def finalizar(self):

        self.registrar("Fila concluída.")

    def executar(self):

        self.registrar(

            "Sistema de Filas Inteligentes iniciado."

        )

        self.adicionar_tarefa(

            2,

            "Atualizar Memória"

        )

        self.adicionar_tarefa(

            1,

            "Verificar Integridade"

        )

        self.adicionar_tarefa(

            3,

            "Gerar Relatório"

        )

        self.organizar_fila()

        self.executar_fila()

        self.finalizar()


if __name__ == "__main__":

    sistema = SistemaDeFilasInteligentes()

    sistema.executar()
