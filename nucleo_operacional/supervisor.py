"""
SUPERVISOR DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana
"""

from datetime import datetime

from nucleo_operacional.painel_agentes import status_agente

HISTORICO_OCORRENCIAS = []


class Supervisor:

    def __init__(self):

        self.status = "ATIVO"

        self.verificacoes = 0

    def registrar_ocorrencia(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[{horario}] {mensagem}"

        HISTORICO_OCORRENCIAS.append(registro)

    def obter_historico(self):

        return HISTORICO_OCORRENCIAS

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.registrar_ocorrencia(
            f"Status alterado para {status}"
        )

    def verificar_agente(self, nome_agente):

        self.verificacoes += 1

        ativo = status_agente(nome_agente)

        if ativo:

            self.registrar_ocorrencia(
                f"Agente {nome_agente} disponível"
            )

            return True

        self.registrar_ocorrencia(
            f"Agente {nome_agente} indisponível"
        )

        return False

    def analisar_solicitacao(self, agente):

        if self.verificar_agente(agente):

            return f"Agente {agente} disponivel"

        return f"Agente {agente} indisponivel"

    def resumo_operacional(self):

        return {

            "status": self.status,

            "verificacoes": self.verificacoes,

            "ocorrencias": len(HISTORICO_OCORRENCIAS)

        }

    def executar(self):

        self.registrar_ocorrencia(
            "Supervisor iniciado."
        )

        self.resumo_operacional()


if __name__ == "__main__":

    supervisor = Supervisor()

    supervisor.executar()

    print(
        supervisor.analisar_solicitacao(
            "pesquisa_avancada"
        )
    )

    print(
        supervisor.resumo_operacional()
    )

    print(
        supervisor.obter_historico()
    )
