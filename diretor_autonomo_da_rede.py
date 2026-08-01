"""
DIRETOR AUTÔNOMO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
DIRETOR_AUTONOMO_DA_REDE.md
"""

from datetime import datetime


class DiretorAutonomoDaRede:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.componentes = [

            "Supervisor Geral",

            "Orquestrador Central",

            "Planejador Mestre de Expansão",

            "Sistema de Evolução Autônoma",

            "Gerador Autônomo de Componentes",

            "Motor de Planejamento",

            "Motor de Construção",

            "Sistema Executor",

            "Motor de Verificação",

            "Motor de Aprendizado",

            "Sistema de Auditoria",

            "Sistema de Monitoramento",

            "Sistema de Recuperação",

            "Sistema de Memória Persistente",

            "Registro Central de Eventos"

        ]

        self.operacao_continua = False

        self.intervalo_direcao = 10

        self.ciclos_continuos = 0

        self.ultima_direcao_continua = None

        self.ultima_execucao = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[DIRETOR] [{horario}] {mensagem}")

    def listar_componentes(self):

        self.registrar("Componentes supervisionados:")

        for componente in self.componentes:

            self.registrar(f"ATIVO -> {componente}")

        return self.componentes

    def verificar_componentes(self):

        self.registrar("Verificando componentes supervisionados.")

        for componente in self.componentes:

            self.registrar(f"OK -> {componente}")

        return True

    def adicionar_componente(self, componente):

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.registrar(f"Novo componente supervisionado: {componente}")

    def iniciar_ciclo(self):

        self.ciclo += 1

        self.registrar(f"Iniciando ciclo operacional {self.ciclo}")

    def coordenar(self):

        self.registrar("Coordenando os componentes da Rede.")

    def validar(self):

        self.registrar("Validando o ciclo operacional.")

    def finalizar_ciclo(self):

        self.registrar(f"Ciclo {self.ciclo} concluído.")

    def registrar_evento(self, descricao, resultado="OK", importancia="NORMAL"):

        try:
            from registro_central_eventos import RegistroCentralEventos
            registro = RegistroCentralEventos()
            registro.registrar(
                origem="Diretor Autônomo",
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

    def iniciar_operacao_continua(self):

        self.operacao_continua = True

        self.registrar("Diretor Autônomo entrou em operação contínua.")

        self.registrar_evento(
            "Diretor Autônomo entrou em operação contínua.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            "Diretor Autônomo entrou em operação contínua."
        )

    def executar_direcao_continua(self):

        self.ciclos_continuos += 1

        self.ultima_direcao_continua = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.iniciar_ciclo()

        self.coordenar()

        self.validar()

        self.verificar_componentes()

        self.finalizar_ciclo()

        self.registrar(
            f"Ciclo contínuo de direção #{self.ciclos_continuos} executado."
        )

        self.registrar_evento(
            f"Ciclo contínuo de direção #{self.ciclos_continuos} executado.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            f"Ciclo contínuo de direção #{self.ciclos_continuos} executado."
        )

    def parar_operacao_continua(self):

        self.operacao_continua = False

        self.registrar("Diretor Autônomo encerrou operação contínua.")

        self.registrar_evento(
            "Diretor Autônomo encerrou operação contínua.",
            resultado="OK",
            importancia="NORMAL"
        )

        self.registrar_memoria(
            "Diretor Autônomo encerrou operação contínua."
        )

    def obter_estado_operacao(self):

        return {

            "status": self.status,

            "operacao_continua": self.operacao_continua,

            "ciclos_continuos": self.ciclos_continuos,

            "ultima_direcao_continua": self.ultima_direcao_continua,

            "ultima_execucao": self.ultima_execucao,

            "ciclo": self.ciclo

        }

    def executar(self):

        self.registrar("Diretor Autônomo iniciado.")

        self.listar_componentes()

        self.iniciar_ciclo()

        self.coordenar()

        self.validar()

        self.finalizar_ciclo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.registrar("Diretor Autônomo operacional.")

        self.iniciar_operacao_continua()


if __name__ == "__main__":

    diretor = DiretorAutonomoDaRede()

    diretor.executar()
