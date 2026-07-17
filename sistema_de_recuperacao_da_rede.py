"""
SISTEMA DE RECUPERAÇÃO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_RECUPERACAO_DA_REDE.md
"""

from datetime import datetime


class SistemaDeRecuperacaoDaRede:

    def __init__(self):

        self.status = "ATIVO"

        self.ocorrencias = []

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[RECUPERACAO] [{horario}] {mensagem}")

    def detectar_falha(self, componente):

        self.ocorrencias.append(componente)

        self.registrar(f"Falha detectada em: {componente}")

    def listar_ocorrencias(self):
        """
        Retorna todas as ocorrências registradas.
        """

        return self.ocorrencias

    def quantidade_ocorrencias(self):
        """
        Retorna a quantidade de ocorrências registradas.
        """

        return len(self.ocorrencias)

    def obter_status(self):
        """
        Retorna o status atual do Sistema de Recuperação.
        """

        return self.status

    def alterar_status(self, novo_status):
        """
        Altera o status operacional do Sistema de Recuperação.
        """

        self.status = novo_status

        self.registrar(f"Status alterado para: {novo_status}")

    def analisar_falha(self):

        self.registrar("Analisando falha.")

    def recuperar(self):

        self.registrar("Executando processo de recuperação.")

    def validar_recuperacao(self):

        self.registrar("Validando recuperação.")

    def limpar_ocorrencias(self):

        self.ocorrencias.clear()

        self.registrar("Ocorrências encerradas.")

    def executar(self):

        self.registrar("Sistema de Recuperação iniciado.")

        self.detectar_falha("Sistema Executor")

        self.analisar_falha()

        self.recuperar()

        self.validar_recuperacao()

        self.limpar_ocorrencias()

        self.registrar("Sistema de Recuperação finalizado.")


if __name__ == "__main__":

    recuperacao = SistemaDeRecuperacaoDaRede()

    recuperacao.executar()
