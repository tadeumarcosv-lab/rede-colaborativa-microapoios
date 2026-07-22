"""
SISTEMA DE EVOLUÇÃO AUTÔNOMA
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_EVOLUCAO_AUTONOMA.md
"""

from datetime import datetime


class SistemaDeEvolucaoAutonoma:

    def __init__(self):

        self.status = "ATIVO"

        self.propostas = []

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.evolucoes_realizadas = 0

        self.total_validacoes = 0

        self.ultima_proposta_analisada = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[EVOLUCAO] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def listar_propostas(self):

        self.registrar("Propostas registradas:")

        if not self.propostas:

            self.registrar("Nenhuma proposta registrada.")

        else:

            for proposta in self.propostas:

                self.registrar(f"PROPOSTA -> {proposta}")

        return self.propostas

    def adicionar_proposta(self, proposta):

        if proposta not in self.propostas:

            self.propostas.append(proposta)

            self.registrar(f"Nova proposta registrada: {proposta}")

    def analisar(self):

        self.registrar("Analisando oportunidades de evolução.")

        if self.propostas:

            self.ultima_proposta_analisada = self.propostas[-1]

        self.evolucoes_realizadas += 1

        return True

    def validar(self):

        self.total_validacoes += 1

        self.registrar("Validando propostas de evolução.")

        return True

    def obter_historico(self):

        return self.historico_execucoes

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_total_evolucoes(self):

        return self.evolucoes_realizadas

    def obter_total_validacoes(self):

        return self.total_validacoes

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def executar(self):

        self.registrar("Sistema de Evolução Autônoma iniciado.")

        self.listar_propostas()

        self.analisar()

        self.validar()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "propostas": len(self.propostas),

            "evolucoes_realizadas": self.evolucoes_realizadas,

            "validacoes": self.total_validacoes,

            "ultima_proposta": self.ultima_proposta_analisada,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar("Sistema de Evolução Autônoma operacional.")


if __name__ == "__main__":

    sistema = SistemaDeEvolucaoAutonoma()

    sistema.executar()
