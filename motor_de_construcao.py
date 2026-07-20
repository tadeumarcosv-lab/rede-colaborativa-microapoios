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

        self.registrar("Recebendo plano de construção.")

    def consultar_documentacao(self):

        self.registrar("Consultando documentação oficial.")

    def construir(self):

        componente = "Componente_" + str(len(self.componentes_construidos) + 1)

        self.componentes_construidos.append(componente)

        self.ultimo_componente = componente

        self.ultima_construcao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.registrar(f"Construindo {componente}.")

    def documentar(self):

        self.registrar("Documentando componente criado.")

    def enviar_verificacao(self):

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

        self.registrar("Construção concluída.")

        return True


if __name__ == "__main__":

    motor = MotorDeConstrucao()

    motor.executar()
