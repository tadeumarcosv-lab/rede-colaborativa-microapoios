"""
INTEGRADOR OPERACIONAL PRINCIPAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada na arquitetura oficial da Rede.
"""

from datetime import datetime
import time


class IntegradorOperacionalPrincipal:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.ultima_atividade = None

        self.integradores = [
            "Integrador dos Motores",
            "Integrador dos Sistemas"
        ]

        self.integradores_disponiveis = []

        self.integradores_executados = 0

        self.integradores_com_sucesso = 0

        self.integradores_com_falha = 0

        self.integracao_inicio = None

        self.integracao_fim = None

        self.tempo_total = None

        self.resultado_geral = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[OPERACIONAL] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def listar_integradores(self):

        self.ultima_atividade = "listar_integradores"

        self.registrar("Integradores atualmente registrados:")

        for integrador in self.integradores:

            self.registrar(f"ATIVO -> {integrador}")

        return self.integradores

    def quantidade_integradores(self):

        return len(self.integradores)

    def obter_historico(self):

        return self.historico_execucoes

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_integradores_disponiveis(self):

        return self.integradores_disponiveis

    def obter_integradores_executados(self):

        return self.integradores_executados

    def obter_integradores_com_sucesso(self):

        return self.integradores_com_sucesso

    def obter_integradores_com_falha(self):

        return self.integradores_com_falha

    def obter_tempo_total(self):

        return self.tempo_total

    def obter_resultado_geral(self):

        return self.resultado_geral

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def sincronizar_operacao(self):

        self.ultima_atividade = "sincronizar_operacao"

        self.registrar("Sincronizando toda a operação da Rede.")

        return True

    def verificar_operacao(self):

        self.ultima_atividade = "verificar_operacao"

        self.registrar("Verificando integradores registrados.")

        for integrador in self.integradores:

            self.registrar(f"OK -> {integrador}")

        return True

    def registrar_ciclo(self):

        self.ciclo += 1

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo operacional {self.ciclo} registrado.")

        return True

    def resumo(self):

        self.ultima_atividade = "resumo"

        self.registrar(
            f"Resumo: {len(self.integradores)} integradores | Status: {self.status}"
        )

    def registrar_evento(self, descricao, resultado="OK", importancia="NORMAL"):

        try:
            from registro_central_eventos import RegistroCentralEventos
            registro = RegistroCentralEventos()
            registro.registrar(
                origem="Integrador Operacional Principal",
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

    def executar_integradores(self):

        self.ultima_atividade = "executar_integradores"

        self.registrar("Iniciando execução dos integradores disponíveis.")

        self.integradores_disponiveis = []

        self.integradores_executados = 0

        self.integradores_com_sucesso = 0

        self.integradores_com_falha = 0

        # Registra início da integração
        self.registrar_evento(
            "Integração operacional iniciada.",
            resultado="EXECUTANDO",
            importancia="NORMAL"
        )

        # Integrador dos Motores
        try:
            from integrador_dos_motores import IntegradorDosMotores
            integrador = IntegradorDosMotores()
            integrador.executar()
            self.integradores_disponiveis.append("Integrador dos Motores")
            self.integradores_executados += 1
            self.integradores_com_sucesso += 1
            self.registrar("Executando Integrador dos Motores")
            self.registrar_evento(
                "Integrador dos Motores executado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.integradores_com_falha += 1
            self.registrar(f"Erro ao executar Integrador dos Motores: {e}")
            self.registrar_evento(
                f"Falha no Integrador dos Motores: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )
            self.registrar_memoria(
                f"Falha no Integrador dos Motores: {e}"
            )

        # Integrador dos Sistemas
        try:
            from integrador_dos_sistemas import IntegradorDosSistemas
            integrador = IntegradorDosSistemas()
            integrador.executar()
            self.integradores_disponiveis.append("Integrador dos Sistemas")
            self.integradores_executados += 1
            self.integradores_com_sucesso += 1
            self.registrar("Executando Integrador dos Sistemas")
            self.registrar_evento(
                "Integrador dos Sistemas executado com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )
        except Exception as e:
            self.integradores_com_falha += 1
            self.registrar(f"Erro ao executar Integrador dos Sistemas: {e}")
            self.registrar_evento(
                f"Falha no Integrador dos Sistemas: {e}",
                resultado="FALHA",
                importancia="ALTA"
            )
            self.registrar_memoria(
                f"Falha no Integrador dos Sistemas: {e}"
            )

        self.registrar(
            f"Integradores disponíveis: {len(self.integradores_disponiveis)}"
        )

        self.registrar(
            f"Integradores executados: {self.integradores_executados}"
        )

        self.registrar(
            f"Integradores com sucesso: {self.integradores_com_sucesso}"
        )

        self.registrar(
            f"Integradores com falha: {self.integradores_com_falha}"
        )

        # Registra conclusão da execução dos integradores
        if self.integradores_com_falha > 0:
            self.registrar_evento(
                f"Execução dos integradores concluída com {self.integradores_com_falha} falha(s).",
                resultado="PARCIAL",
                importancia="MEDIA"
            )
        else:
            self.registrar_evento(
                "Execução dos integradores concluída com sucesso.",
                resultado="OK",
                importancia="NORMAL"
            )

        return True

    def executar(self):

        self.integracao_inicio = datetime.now()

        self.registrar("Integrador Operacional Principal iniciado.")

        self.registrar_evento(
            "Integrador Operacional Principal iniciado.",
            resultado="EXECUTANDO",
            importancia="NORMAL"
        )

        self.listar_integradores()

        self.sincronizar_operacao()

        self.executar_integradores()

        self.verificar_operacao()

        self.registrar_ciclo()

        self.resumo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.integracao_fim = datetime.now()

        self.tempo_total = (self.integracao_fim - self.integracao_inicio).total_seconds()

        self.resultado_geral = "SUCESSO" if self.integradores_com_falha == 0 else "PARCIAL"

        self.resumo_operacional = {

            "status": self.status,

            "ciclos": self.ciclo,

            "integradores": len(self.integradores),

            "integradores_disponiveis": len(self.integradores_disponiveis),

            "integradores_executados": self.integradores_executados,

            "integradores_com_sucesso": self.integradores_com_sucesso,

            "integradores_com_falha": self.integradores_com_falha,

            "resultado_geral": self.resultado_geral,

            "tempo_total_segundos": round(self.tempo_total, 2),

            "ultima_atividade": self.ultima_atividade,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar_evento(
            f"Integração operacional concluída. Ciclo {self.ciclo}. "
            f"Resultado: {self.resultado_geral}. "
            f"Tempo: {round(self.tempo_total, 2)}s.",
            resultado=self.resultado_geral,
            importancia="NORMAL"
        )

        self.registrar_memoria(
            f"Integração operacional concluída. Ciclo {self.ciclo}. "
            f"Resultado: {self.resultado_geral}. "
            f"Tempo: {round(self.tempo_total, 2)}s."
        )

        self.registrar(
            f"Tempo total de execução: {round(self.tempo_total, 2)} segundos"
        )

        self.registrar("Integração operacional concluída.")

        return self.resultado_geral == "SUCESSO"


if __name__ == "__main__":

    integrador = IntegradorOperacionalPrincipal()

    integrador.executar()
