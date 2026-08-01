"""
GERENCIADOR DE INICIALIZAÇÃO
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por executar toda a sequência oficial de inicialização.
"""

from datetime import datetime

from nucleo_operacional.supervisor import Supervisor
from nucleo_operacional.integracao_completa import IntegracaoCompleta


class GerenciadorInicializacao:

    def __init__(self):

        self.status = "PRONTO"

        self.etapas_executadas = 0

        self.etapas = [

            "Inicializar Supervisor",

            "Inicializar Integração",

            "Executar Bootstrap",

            "Validar Inicialização",

            "Finalizar Inicialização"

        ]

        self.ultima_atividade = None

        self.inicio = None

        self.fim = None

        self.tempo_total = None

        self.etapas_sucesso = 0

        self.etapas_falha = 0

        self.resultado_geral = None

        self.operacao_continua = False

        self.intervalo_monitoramento = 10

        self.ciclos_monitoramento = 0

        self.ultimo_monitoramento = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[INICIALIZAÇÃO] [{horario}] {mensagem}")

    def registrar_evento(self, descricao, resultado="OK", importancia="NORMAL"):

        try:
            from registro_central_eventos import RegistroCentralEventos
            registro = RegistroCentralEventos()
            registro.registrar(
                origem="Gerenciador de Inicialização",
                destino="Rede",
                responsavel="Sistema",
                descricao=descricao,
                resultado=resultado,
                importancia=importancia
            )
        except Exception as e:
            self.registrar(f"Erro ao registrar evento: {e}")

    def registrar_memoria(self, descricao):

        try:
            from gerenciador_memoria import GerenciadorMemoria
            memoria = GerenciadorMemoria()
            memoria.adicionar_historico(descricao)
        except Exception as e:
            self.registrar(f"Erro ao registrar na memória: {e}")

    def listar_etapas(self):

        self.ultima_atividade = "listar_etapas"

        self.registrar("Etapas oficiais:")

        for etapa in self.etapas:

            self.registrar(f"ETAPA -> {etapa}")

        return self.etapas

    def adicionar_etapa(self, etapa):

        self.ultima_atividade = "adicionar_etapa"

        if etapa not in self.etapas:

            self.etapas.append(etapa)

            self.registrar(f"Nova etapa registrada: {etapa}")

    def obter_status(self):

        return {

            "status": self.status,

            "etapas": len(self.etapas),

            "executadas": self.etapas_executadas

        }

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_resultado_geral(self):

        return self.resultado_geral

    def obter_tempo_total(self):

        return self.tempo_total

    def obter_etapas_sucesso(self):

        return self.etapas_sucesso

    def obter_etapas_falha(self):

        return self.etapas_falha

    def iniciar_operacao_continua(self):

        self.operacao_continua = True

        self.registrar("Operação contínua ativada.")

        self.registrar_evento(
            "Gerenciador de Inicialização entrou em operação contínua.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            "Gerenciador de Inicialização entrou em operação contínua."
        )

    def executar_monitoramento(self):

        self.ciclos_monitoramento += 1

        self.ultimo_monitoramento = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.registrar(
            f"Ciclo de monitoramento #{self.ciclos_monitoramento} executado."
        )

        self.registrar_evento(
            f"Ciclo de monitoramento #{self.ciclos_monitoramento} executado.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            f"Ciclo de monitoramento #{self.ciclos_monitoramento} executado."
        )

    def parar_operacao_continua(self):

        self.operacao_continua = False

        self.registrar("Operação contínua desativada.")

        self.registrar_evento(
            "Gerenciador de Inicialização encerrou operação contínua.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            "Gerenciador de Inicialização encerrou operação contínua."
        )

    def obter_estado_operacao(self):

        return {

            "status": self.status,

            "operacao_continua": self.operacao_continua,

            "ciclos_monitoramento": self.ciclos_monitoramento,

            "ultimo_monitoramento": self.ultimo_monitoramento,

            "resultado_geral": self.resultado_geral,

            "tempo_total": self.tempo_total

        }

    def iniciar(self):

        self.inicio = datetime.now()

        self.status = "EXECUTANDO"

        self.ultima_atividade = "iniciar"

        self.registrar("Gerenciador iniciado.")

        self.registrar_evento(
            "Gerenciador de Inicialização iniciado.",
            resultado="EXECUTANDO",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            "Gerenciador de Inicialização iniciado."
        )

        self.listar_etapas()

        # Etapa 1: Supervisor
        try:
            self.ultima_atividade = "inicializar_supervisor"

            supervisor = Supervisor()

            self.etapas_executadas += 1

            self.etapas_sucesso += 1

            self.registrar("Supervisor ativo.")

            self.registrar_evento(
                "Supervisor inicializado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.etapas_falha += 1

            self.registrar(f"Erro ao inicializar Supervisor: {e}")

            self.registrar_evento(
                f"Falha ao inicializar Supervisor: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )

            self.registrar_memoria(
                f"Falha ao inicializar Supervisor: {e}"
            )

        # Etapa 2: Integração Completa
        try:
            self.ultima_atividade = "inicializar_integracao"

            sistema = IntegracaoCompleta()

            self.etapas_executadas += 1

            resultado = sistema.executar(
                "Inicialização Oficial da Rede"
            )

            print(resultado)

            self.etapas_sucesso += 1

            self.registrar("Integração Completa executada com sucesso.")

            self.registrar_evento(
                "Integração Completa executada com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.etapas_falha += 1

            self.registrar(f"Erro ao executar Integração Completa: {e}")

            self.registrar_evento(
                f"Falha na Integração Completa: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )

            self.registrar_memoria(
                f"Falha na Integração Completa: {e}"
            )

        self.status = "OPERACIONAL"

        self.fim = datetime.now()

        self.tempo_total = (self.fim - self.inicio).total_seconds()

        self.ultima_atividade = "finalizar"

        if self.etapas_falha == 0:
            self.resultado_geral = "SUCESSO"
        elif self.etapas_sucesso > 0 and self.etapas_falha > 0:
            self.resultado_geral = "PARCIAL"
        else:
            self.resultado_geral = "FALHA_CRITICA"

        self.registrar("Rede inicializada com sucesso.")

        self.registrar(f"Status atual: {self.status}")

        self.registrar(
            f"Etapas executadas: {self.etapas_executadas}"
        )

        self.registrar(
            f"Etapas com sucesso: {self.etapas_sucesso}"
        )

        self.registrar(
            f"Etapas com falha: {self.etapas_falha}"
        )

        self.registrar(
            f"Resultado geral: {self.resultado_geral}"
        )

        self.registrar(
            f"Tempo de inicialização: {self.tempo_total:.2f} segundos"
        )

        self.registrar_evento(
            f"Gerenciador de Inicialização concluído. "
            f"Resultado: {self.resultado_geral}. "
            f"Tempo: {self.tempo_total:.2f}s.",
            resultado=self.resultado_geral,
            importancia="NORMAL"
        )

        self.registrar_memoria(
            f"Gerenciador de Inicialização concluído. "
            f"Resultado: {self.resultado_geral}."
        )

        self.iniciar_operacao_continua()

        return self.resultado_geral == "SUCESSO"


if __name__ == "__main__":

    gerenciador = GerenciadorInicializacao()

    gerenciador.iniciar()
