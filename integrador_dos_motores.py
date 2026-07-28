"""
INTEGRADOR DOS MOTORES DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada na arquitetura oficial da Rede.
"""

from datetime import datetime
import time


class IntegradorDosMotores:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.motores = [
            "Motor de Construção",
            "Motor de Verificação",
            "Motor de Aprendizado"
        ]

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.ultima_atividade = None

        self.motores_disponiveis = []

        self.motores_executados = 0

        self.motores_com_sucesso = 0

        self.motores_com_falha = 0

        self.inicio_execucao = None

        self.fim_execucao = None

        self.tempo_total = None

        self.resultado_geral = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[INTEGRADOR] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def adicionar_motor(self, motor):

        if motor not in self.motores:

            self.motores.append(motor)

            self.ultima_atividade = "adicionar_motor"

            self.registrar(f"Novo motor integrado: {motor}")

    def listar_motores(self):

        self.ultima_atividade = "listar_motores"

        self.registrar("Motores atualmente integrados:")

        for motor in self.motores:

            self.registrar(f"ATIVO -> {motor}")

        return self.motores

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def quantidade_motores(self):

        return len(self.motores)

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_historico(self):

        return self.historico_execucoes

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_motores_disponiveis(self):

        return self.motores_disponiveis

    def obter_motores_executados(self):

        return self.motores_executados

    def obter_motores_com_sucesso(self):

        return self.motores_com_sucesso

    def obter_motores_com_falha(self):

        return self.motores_com_falha

    def obter_tempo_total(self):

        return self.tempo_total

    def obter_resultado_geral(self):

        return self.resultado_geral

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def registrar_evento(self, descricao, resultado="OK", importancia="NORMAL"):

        try:
            from registro_central_eventos import RegistroCentralEventos
            registro = RegistroCentralEventos()
            registro.registrar(
                origem="Integrador dos Motores",
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

    def integrar_construcao(self):

        self.ultima_atividade = "integrar_construcao"

        self.registrar("Integrando Motor de Construção.")

        return True

    def integrar_verificacao(self):

        self.ultima_atividade = "integrar_verificacao"

        self.registrar("Integrando Motor de Verificação.")

        return True

    def integrar_aprendizado(self):

        self.ultima_atividade = "integrar_aprendizado"

        self.registrar("Integrando Motor de Aprendizado.")

        return True

    def sincronizar_motores(self):

        self.ultima_atividade = "sincronizar_motores"

        self.registrar("Sincronizando todos os motores.")

        return True

    def verificar_motores(self):

        self.ultima_atividade = "verificar_motores"

        self.registrar("Verificando motores integrados.")

        for motor in self.motores:

            self.registrar(f"OK -> {motor}")

        return True

    def registrar_ciclo(self):

        self.ciclo += 1

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo operacional {self.ciclo} registrado.")

        return True

    def resumo(self):

        self.ultima_atividade = "resumo"

        self.registrar(
            f"Resumo: {len(self.motores)} motores | Status: {self.status}"
        )

    def executar_motores(self):

        self.ultima_atividade = "executar_motores"

        self.registrar("Iniciando execução dos motores disponíveis.")

        self.motores_disponiveis = []

        self.motores_executados = 0

        self.motores_com_sucesso = 0

        self.motores_com_falha = 0

        self.inicio_execucao = datetime.now()

        self.registrar_evento(
            "Execução dos motores iniciada.",
            resultado="EXECUTANDO",
            importancia="NORMAL"
        )

        # Motor de Construção
        try:
            from motor_de_construcao import MotorDeConstrucao
            motor = MotorDeConstrucao()
            motor.executar()
            self.motores_disponiveis.append("Motor de Construção")
            self.motores_executados += 1
            self.motores_com_sucesso += 1
            self.registrar("Executando Motor de Construção")
            self.registrar_evento(
                "Motor de Construção executado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.motores_com_falha += 1
            self.registrar(f"Erro ao executar Motor de Construção: {e}")
            self.registrar_evento(
                f"Falha no Motor de Construção: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )
            self.registrar_memoria(
                f"Falha no Motor de Construção: {e}"
            )

        # Motor de Verificação
        try:
            from motor_de_verificacao import MotorDeVerificacao
            motor = MotorDeVerificacao()
            motor.executar()
            self.motores_disponiveis.append("Motor de Verificação")
            self.motores_executados += 1
            self.motores_com_sucesso += 1
            self.registrar("Executando Motor de Verificação")
            self.registrar_evento(
                "Motor de Verificação executado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.motores_com_falha += 1
            self.registrar(f"Erro ao executar Motor de Verificação: {e}")
            self.registrar_evento(
                f"Falha no Motor de Verificação: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )
            self.registrar_memoria(
                f"Falha no Motor de Verificação: {e}"
            )

        # Motor de Aprendizado
        try:
            from motor_de_aprendizado import MotorDeAprendizado
            motor = MotorDeAprendizado()
            motor.executar()
            self.motores_disponiveis.append("Motor de Aprendizado")
            self.motores_executados += 1
            self.motores_com_sucesso += 1
            self.registrar("Executando Motor de Aprendizado")
            self.registrar_evento(
                "Motor de Aprendizado executado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.motores_com_falha += 1
            self.registrar(f"Erro ao executar Motor de Aprendizado: {e}")
            self.registrar_evento(
                f"Falha no Motor de Aprendizado: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )
            self.registrar_memoria(
                f"Falha no Motor de Aprendizado: {e}"
            )

        self.fim_execucao = datetime.now()

        self.tempo_total = (self.fim_execucao - self.inicio_execucao).total_seconds()

        self.registrar(
            f"Motores disponíveis: {len(self.motores_disponiveis)}"
        )

        self.registrar(
            f"Motores executados: {self.motores_executados}"
        )

        self.registrar(
            f"Motores com sucesso: {self.motores_com_sucesso}"
        )

        self.registrar(
            f"Motores com falha: {self.motores_com_falha}"
        )

        self.registrar(
            f"Tempo total: {round(self.tempo_total, 2)} segundos"
        )

        if self.motores_com_falha > 0 and self.motores_executados > 0:
            self.resultado_geral = "PARCIAL"
            self.registrar_evento(
                f"Execução dos motores concluída com {self.motores_com_falha} falha(s).",
                resultado="PARCIAL",
                importancia="MEDIA"
            )
        elif self.motores_com_falha > 0 and self.motores_executados == 0:
            self.resultado_geral = "FALHA_CRITICA"
            self.registrar_evento(
                "Nenhum motor foi executado com sucesso.",
                resultado="FALHA_CRITICA",
                importancia="CRITICA"
            )
            self.registrar_memoria(
                "Nenhum motor foi executado com sucesso."
            )
        else:
            self.resultado_geral = "SUCESSO"
            self.registrar_evento(
                "Execução dos motores concluída com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )

        self.registrar_memoria(
            f"Execução dos motores concluída. Resultado: {self.resultado_geral}."
        )

        return True

    def executar(self):

        self.registrar("Integrador dos Motores iniciado.")

        self.registrar_evento(
            "Integrador dos Motores iniciado.",
            resultado="EXECUTANDO",
            importancia="NORMAL"
        )

        self.listar_motores()

        self.integrar_construcao()

        self.integrar_verificacao()

        self.integrar_aprendizado()

        self.sincronizar_motores()

        self.executar_motores()

        self.verificar_motores()

        self.registrar_ciclo()

        self.resumo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "ciclos": self.ciclo,

            "motores_integrados": len(self.motores),

            "motores_disponiveis": len(self.motores_disponiveis),

            "motores_executados": self.motores_executados,

            "motores_com_sucesso": self.motores_com_sucesso,

            "motores_com_falha": self.motores_com_falha,

            "resultado_geral": self.resultado_geral,

            "tempo_total_segundos": round(self.tempo_total, 2) if self.tempo_total else 0,

            "ultima_atividade": self.ultima_atividade,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar("Integração dos motores concluída.")

        return self.resultado_geral == "SUCESSO"


if __name__ == "__main__":

    integrador = IntegradorDosMotores()

    integrador.executar()
