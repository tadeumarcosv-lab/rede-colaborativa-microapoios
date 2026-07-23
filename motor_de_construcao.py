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

        self.historico = []

        self.componentes_construidos = []

        self.ultimo_componente = None

        self.ultima_construcao = None

        self.historico_execucoes = []

        self.resumo_operacional_dados = {}

        self.ultima_execucao = None

        self.total_construcoes = 0

        self.ultima_etapa_executada = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[CONSTRUCAO] [{horario}] {mensagem}"

        self.historico.append(registro)

        print(registro)

    def adicionar_etapa(self, etapa):

        if etapa not in self.etapas:

            self.etapas.append(etapa)

            self.registrar(f"Nova etapa adicionada: {etapa}")

    def remover_etapa(self, etapa):

        if etapa in self.etapas:

            self.etapas.remove(etapa)

            self.registrar(f"Etapa removida: {etapa}")

    def obter_etapas(self):

        return self.etapas

    def obter_status(self):

        return self.status

    def alterar_status(self, novo_status):

        self.status = novo_status

        self.registrar(f"Status alterado para: {novo_status}")

    def receber_plano(self):

        self.ultima_etapa_executada = "Receber Plano"

        self.registrar("Recebendo plano de construção.")

    def consultar_documentacao(self):

        self.ultima_etapa_executada = "Consultar Documentação"

        self.registrar("Consultando documentação oficial.")

    def construir(self):

        componente = "Componente_" + str(len(self.componentes_construidos) + 1)

        self.componentes_construidos.append(componente)

        self.ultimo_componente = componente

        self.ultima_construcao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.total_construcoes += 1

        self.ultima_etapa_executada = "Construir"

        self.registrar(f"Construindo {componente}.")

    def documentar(self):

        self.ultima_etapa_executada = "Documentar"

        self.registrar("Documentando componente criado.")

    def enviar_verificacao(self):

        self.ultima_etapa_executada = "Enviar para Verificação"

        self.registrar("Enviando componente para o Motor de Verificação.")

    def listar_etapas(self):

        self.registrar("Fluxo de construção:")

        for etapa in self.etapas:

            self.registrar(f"OK -> {etapa}")

    def listar_componentes(self):

        self.registrar("Componentes construídos:")

        if not self.componentes_construidos:

            self.registrar("Nenhum componente registrado.")

        else:

            for componente in self.componentes_construidos:

                self.registrar(f"OK -> {componente}")

        return self.componentes_construidos

    def quantidade_componentes(self):

        return len(self.componentes_construidos)

    def obter_historico(self):

        return self.historico

    def verificar_pendencias(self):

        self.registrar("Verificando pendências de construção.")

        return False

    def resumo_operacional(self):

        return {

            "status": self.status,

            "componentes": len(self.componentes_construidos),

            "ultimo_componente": self.ultimo_componente,

            "ultima_construcao": self.ultima_construcao

        }

    def obter_resumo_operacional(self):

        return self.resumo_operacional_dados

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_total_construcoes(self):

        return self.total_construcoes

    def obter_ultima_etapa_executada(self):

        return self.ultima_etapa_executada

    def limpar_historico_execucoes(self):

        self.historico_execucoes.clear()

    def executar(self):

        self.registrar("Motor de Construção iniciado.")

        self.listar_etapas()

        self.receber_plano()

        self.consultar_documentacao()

        self.construir()

        self.documentar()

        self.enviar_verificacao()

        self.verificar_pendencias()

        self.listar_componentes()

        self.registrar(f"Resumo: {self.resumo_operacional()}")

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional_dados = {

            "status": self.status,

            "componentes": len(self.componentes_construidos),

            "total_construcoes": self.total_construcoes,

            "ultimo_componente": self.ultimo_componente,

            "ultima_etapa": self.ultima_etapa_executada,

            "ultima_construcao": self.ultima_construcao,

            "ultima_execucao": self.ultima_execucao

        }

        self.historico_execucoes.append(self.resumo_operacional_dados)

        self.registrar("Construção concluída.")

        return True


if __name__ == "__main__":

    motor = MotorDeConstrucao()

    motor.executar()
