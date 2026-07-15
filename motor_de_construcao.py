"""
MOTOR DE CONSTRUÇÃO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
MOTOR_DE_CONSTRUCAO.md
"""

from datetime import datetime


class MotorDeConstrucao:

    def __init__(self):

        self.status = "ATIVO"

        self.etapas = [
            "Receber Plano",
            "Consultar Constituição",
            "Consultar DNA",
            "Consultar Arquitetura",
            "Construir Estrutura",
            "Gerar Arquivos",
            "Documentar",
            "Enviar para Verificação"
        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[CONSTRUCAO] [{horario}] {mensagem}")

    def adicionar_etapa(self, etapa):
        """
        Adiciona uma nova etapa ao fluxo de construção.
        """

        if etapa not in self.etapas:
            self.etapas.append(etapa)
            self.registrar(f"Nova etapa adicionada: {etapa}")

    def remover_etapa(self, etapa):
        """
        Remove uma etapa existente.
        """

        if etapa in self.etapas:
            self.etapas.remove(etapa)
            self.registrar(f"Etapa removida: {etapa}")

    def obter_etapas(self):
        """
        Retorna todas as etapas cadastradas.
        """

        return self.etapas

    def obter_status(self):
        """
        Retorna o status atual do Motor de Construção.
        """

        return self.status

    def receber_plano(self):

        self.registrar("Recebendo plano de construção.")

    def consultar_documentacao(self):

        self.registrar("Consultando documentação oficial.")

    def construir(self):

        self.registrar("Construindo componente.")

    def documentar(self):

        self.registrar("Documentando componente criado.")

    def enviar_verificacao(self):

        self.registrar("Enviando componente para o Motor de Verificação.")

    def listar_etapas(self):

        self.registrar("Fluxo de construção:")

        for etapa in self.etapas:

            self.registrar(f"OK -> {etapa}")

    def executar(self):

        self.registrar("Motor de Construção iniciado.")

        self.listar_etapas()

        self.receber_plano()

        self.consultar_documentacao()

        self.construir()

        self.documentar()

        self.enviar_verificacao()

        self.registrar("Construção concluída.")


if __name__ == "__main__":

    motor = MotorDeConstrucao()

    motor.executar()
