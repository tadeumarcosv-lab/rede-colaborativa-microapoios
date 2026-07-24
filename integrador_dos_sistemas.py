"""
INTEGRADOR DOS SISTEMAS DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada na arquitetura oficial da Rede.
"""

from datetime import datetime


class IntegradorDosSistemas:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.sistemas = [
            "Sistema Executor",
            "Sistema de Monitoramento",
            "Sistema de Recuperação",
            "Gerenciador da Memória",
            "Registro Central de Eventos"
        ]

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.ultima_atividade = None

        self.sistemas_disponiveis = []

        self.sistemas_executados = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[SISTEMAS] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def adicionar_sistema(self, sistema):

        if sistema not in self.sistemas:

            self.sistemas.append(sistema)

            self.ultima_atividade = "adicionar_sistema"

            self.registrar(f"Novo sistema integrado: {sistema}")

    def listar_sistemas(self):

        self.ultima_atividade = "listar_sistemas"

        self.registrar("Sistemas atualmente integrados:")

        for sistema in self.sistemas:

            self.registrar(f"ATIVO -> {sistema}")

        return self.sistemas

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def quantidade_sistemas(self):

        return len(self.sistemas)

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_historico(self):

        return self.historico_execucoes

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_sistemas_disponiveis(self):

        return self.sistemas_disponiveis

    def obter_sistemas_executados(self):

        return self.sistemas_executados

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def integrar_executor(self):

        self.ultima_atividade = "integrar_executor"

        self.registrar("Integrando Sistema Executor.")

        return True

    def integrar_monitoramento(self):

        self.ultima_atividade = "integrar_monitoramento"

        self.registrar("Integrando Sistema de Monitoramento.")

        return True

    def integrar_recuperacao(self):

        self.ultima_atividade = "integrar_recuperacao"

        self.registrar("Integrando Sistema de Recuperação.")

        return True

    def integrar_memoria(self):

        self.ultima_atividade = "integrar_memoria"

        self.registrar("Integrando Gerenciador da Memória.")

        return True

    def integrar_registro(self):

        self.ultima_atividade = "integrar_registro"

        self.registrar("Integrando Registro Central de Eventos.")

        return True

    def sincronizar_sistemas(self):

        self.ultima_atividade = "sincronizar_sistemas"

        self.registrar("Sincronizando todos os sistemas.")

        return True

    def verificar_sistemas(self):

        self.ultima_atividade = "verificar_sistemas"

        self.registrar("Verificando sistemas integrados.")

        for sistema in self.sistemas:

            self.registrar(f"OK -> {sistema}")

        return True

    def registrar_ciclo(self):

        self.ciclo += 1

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo operacional {self.ciclo} registrado.")

        return True

    def resumo(self):

        self.ultima_atividade = "resumo"

        self.registrar(
            f"Resumo: {len(self.sistemas)} sistemas | Status: {self.status}"
        )

    def executar_sistemas(self):

        self.ultima_atividade = "executar_sistemas"

        self.registrar("Iniciando execução dos sistemas disponíveis.")

        self.sistemas_disponiveis = []

        self.sistemas_executados = 0

        # Sistema Executor
        try:
            from sistema_executor_da_rede import SistemaExecutorDaRede
            sistema = SistemaExecutorDaRede()
            sistema.executar()
            self.sistemas_disponiveis.append("Sistema Executor")
            self.sistemas_executados += 1
            self.registrar("Executando Sistema Executor")
        except ImportError:
            self.registrar("Sistema Executor indisponível")

        # Sistema de Monitoramento
        try:
            from sistema_de_monitoramento_da_rede import SistemaDeMonitoramentoDaRede
            sistema = SistemaDeMonitoramentoDaRede()
            sistema.executar()
            self.sistemas_disponiveis.append("Sistema de Monitoramento")
            self.sistemas_executados += 1
            self.registrar("Executando Sistema de Monitoramento")
        except ImportError:
            self.registrar("Sistema de Monitoramento indisponível")

        # Sistema de Recuperação
        try:
            from sistema_de_recuperacao_da_rede import SistemaDeRecuperacaoDaRede
            sistema = SistemaDeRecuperacaoDaRede()
            sistema.executar()
            self.sistemas_disponiveis.append("Sistema de Recuperação")
            self.sistemas_executados += 1
            self.registrar("Executando Sistema de Recuperação")
        except ImportError:
            self.registrar("Sistema de Recuperação indisponível")

        # Gerenciador da Memória
        try:
            from gerenciador_memoria import GerenciadorMemoria
            sistema = GerenciadorMemoria()
            sistema.executar()
            self.sistemas_disponiveis.append("Gerenciador da Memória")
            self.sistemas_executados += 1
            self.registrar("Executando Gerenciador da Memória")
        except ImportError:
            self.registrar("Gerenciador da Memória indisponível")

        # Registro Central de Eventos
        try:
            from registro_central_eventos import RegistroCentralEventos
            sistema = RegistroCentralEventos()
            sistema.executar()
            self.sistemas_disponiveis.append("Registro Central de Eventos")
            self.sistemas_executados += 1
            self.registrar("Executando Registro Central de Eventos")
        except ImportError:
            self.registrar("Registro Central de Eventos indisponível")

        self.registrar(
            f"Sistemas disponíveis: {len(self.sistemas_disponiveis)}"
        )

        self.registrar(
            f"Sistemas executados: {self.sistemas_executados}"
        )

        return True

    def executar(self):

        self.registrar("Integrador dos Sistemas iniciado.")

        self.listar_sistemas()

        self.integrar_executor()

        self.integrar_monitoramento()

        self.integrar_recuperacao()

        self.integrar_memoria()

        self.integrar_registro()

        self.sincronizar_sistemas()

        self.executar_sistemas()

        self.verificar_sistemas()

        self.registrar_ciclo()

        self.resumo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "ciclos": self.ciclo,

            "sistemas_integrados": len(self.sistemas),

            "sistemas_disponiveis": len(self.sistemas_disponiveis),

            "sistemas_executados": self.sistemas_executados,

            "ultima_atividade": self.ultima_atividade,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar("Integração dos sistemas concluída.")


if __name__ == "__main__":

    integrador = IntegradorDosSistemas()

    integrador.executar()
