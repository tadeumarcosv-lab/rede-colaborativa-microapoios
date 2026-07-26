"""
CONFIGURAÇÕES DO NÚCLEO OPERACIONAL
Rede Colaborativa de Microapoios
Autor: Tadeu Marcos Viana

Versão expandida com suporte a histórico de alterações,
controle de versão e operações.
"""

from datetime import datetime


class ConfigNucleo:

    def __init__(self):

        self.versoes = []

        self.historico_alteracoes = []

        self.ultima_alteracao = None

        self.total_alteracoes = 0

        self.status = "ATIVO"

        self.carregar_configuracoes()

    def carregar_configuracoes(self):

        self.configuracoes = {

            "NUCLEO_OPERACIONAL_ATIVO": False,

            "AGENTE_CENTRAL_ATIVO": False,

            "AGENTE_COORDENACAO_ATIVO": False,

            "AGENTE_COMUNICACAO_ATIVO": False,

            "AGENTE_PESQUISA_AVANCADA_ATIVO": False,

            "AGENTE_MEMORIA_ESTRATEGICA_ATIVO": False,

            "AGENTE_GESTAO_CONHECIMENTO_ATIVO": False

        }

        self.versao_atual = "1.0"

        self.registrar_alteracao("Configurações iniciais carregadas.")

    def obter_configuracao(self, chave):

        return self.configuracoes.get(chave, None)

    def definir_configuracao(self, chave, valor):

        if chave in self.configuracoes:

            self.configuracoes[chave] = valor

            self.total_alteracoes += 1

            self.ultima_alteracao = datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            self.registrar_alteracao(
                f"{chave} alterado para {valor}"
            )

            return True

        return False

    def registrar_alteracao(self, descricao):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = {
            "horario": horario,
            "descricao": descricao,
            "versao": self.versao_atual
        }

        self.historico_alteracoes.append(registro)

    def obter_historico(self):

        return self.historico_alteracoes

    def obter_status(self):

        return self.status

    def definir_status(self, novo_status):

        self.status = novo_status

        self.registrar_alteracao(
            f"Status alterado para {novo_status}"
        )

    def obter_versoes(self):

        return self.versoes

    def obter_ultima_alteracao(self):

        return self.ultima_alteracao

    def obter_total_alteracoes(self):

        return self.total_alteracoes

    def obter_resumo_operacional(self):

        return {

            "status": self.status,

            "versoes": len(self.versoes),

            "versao_atual": self.versao_atual,

            "total_alteracoes": self.total_alteracoes,

            "ultima_alteracao": self.ultima_alteracao,

            "configuracoes": len(self.configuracoes)

        }

    def limpar_historico(self):

        self.historico_alteracoes.clear()

        self.registrar_alteracao("Histórico limpo.")

    def executar(self):

        print("========================================")
        print("CONFIGURAÇÕES DO NÚCLEO OPERACIONAL")
        print(f"Status: {self.status}")
        print(f"Versão atual: {self.versao_atual}")
        print(f"Total de alterações: {self.total_alteracoes}")
        print("========================================")

        for chave, valor in self.configuracoes.items():
            print(f"{chave}: {valor}")

        print("========================================")


if __name__ == "__main__":

    config = ConfigNucleo()
    config.executar()
