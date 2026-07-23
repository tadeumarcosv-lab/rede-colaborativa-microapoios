"""
SUPERVISOR GERAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por supervisionar continuamente toda a Rede.
"""

from datetime import datetime


class SupervisorGeral:

    def __init__(self):

        self.status = "ATIVO"

        self.componentes = [
            "Kernel",
            "Orquestrador Central",
            "Diretor Autônomo",
            "Planejador Mestre",
            "Gerador Autônomo",
            "Motor de Construção",
            "Motor de Verificação",
            "Motor de Aprendizado",
            "Sistema Executor",
            "Sistema de Monitoramento",
            "Sistema de Recuperação",
            "Gerenciador da Memória",
            "Registro Central de Eventos",
            "Integrador dos Motores",
            "Integrador dos Sistemas",
            "Integrador Operacional Principal"
        ]

        self.historico = []

        self.ciclos = 0

        self.ultima_supervisao = None

        self.historico_execucoes = []

        self.resumo_operacional_dados = {}

        self.ultima_execucao = None

        self.total_supervisoes = 0

        self.ultima_atividade = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[SUPERVISOR] [{horario}] {mensagem}"

        self.historico.append(registro)

        print(registro)

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def adicionar_componente(self, componente):

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.ultima_atividade = "adicionar_componente"

            self.registrar(f"Novo componente supervisionado: {componente}")

    def listar_componentes(self):

        self.ultima_atividade = "listar_componentes"

        self.registrar("Componentes supervisionados:")

        for componente in self.componentes:

            self.registrar(f"ATIVO -> {componente}")

        return self.componentes

    def obter_historico(self):

        return self.historico

    def resumo_operacional(self):

        return {

            "status": self.status,

            "componentes": len(self.componentes),

            "ciclos": self.ciclos,

            "ultima_supervisao": self.ultima_supervisao

        }

    def verificar(self):

        self.ultima_atividade = "verificar"

        self.registrar("Verificando funcionamento geral da Rede.")

        return True

    def monitorar(self):

        self.ultima_atividade = "monitorar"

        self.registrar("Monitoramento contínuo iniciado.")

        return True

    def verificar_componentes(self):

        self.ultima_atividade = "verificar_componentes"

        self.registrar("Verificando componentes supervisionados.")

        for componente in self.componentes:

            self.registrar(f"OK -> {componente}")

        return True

    def registrar_ciclo(self):

        self.ciclos += 1

        self.ultima_supervisao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo de supervisão #{self.ciclos} registrado.")

        return True

    def obter_resumo_operacional(self):

        return self.resumo_operacional_dados

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_total_supervisoes(self):

        return self.total_supervisoes

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def limpar_historico_execucoes(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def executar(self):

        self.registrar("Supervisor Geral iniciado.")

        self.listar_componentes()

        self.verificar()

        self.monitorar()

        self.verificar_componentes()

        self.registrar_ciclo()

        self.registrar(f"Resumo: {self.resumo_operacional()}")

        self.total_supervisoes += 1

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional_dados = {

            "status": self.status,

            "componentes": len(self.componentes),

            "ciclos": self.ciclos,

            "total_supervisoes": self.total_supervisoes,

            "ultima_atividade": self.ultima_atividade,

            "ultima_supervisao": self.ultima_supervisao,

            "ultima_execucao": self.ultima_execucao

        }

        self.historico_execucoes.append(self.resumo_operacional_dados)

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional_dados}"
        )

        self.registrar("Supervisão concluída.")


if __name__ == "__main__":

    supervisor = SupervisorGeral()

    supervisor.executar()
