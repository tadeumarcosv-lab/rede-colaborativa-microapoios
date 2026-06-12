"""
AGENTE DE COORDENAÇÃO
Rede Colaborativa de Microapoios

Responsável por organizar tarefas,
controlar filas e acompanhar execuções.
"""

class AgenteCoordenacao:

    def __init__(self):
        self.nome = "Agente de Coordenacao"
        self.codigo = "AGENTE-0002"
        self.fila_tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.fila_tarefas.append(tarefa)
        return f"Tarefa adicionada: {tarefa}"

    def listar_tarefas(self):
        return self.fila_tarefas

    def total_tarefas(self):
        return len(self.fila_tarefas)

    def status(self):
        return {
            "agente": self.nome,
            "tarefas": len(self.fila_tarefas)
        }


if __name__ == "__main__":
    coordenacao = AgenteCoordenacao()

    print(coordenacao.adicionar_tarefa("Teste operacional"))
    print(coordenacao.listar_tarefas())
    print(coordenacao.status())
