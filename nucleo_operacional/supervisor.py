from painel_agentes import status_agente

HISTORICO_OCORRENCIAS = []


class Supervisor:

    def registrar_ocorrencia(self, mensagem):

        HISTORICO_OCORRENCIAS.append(
            mensagem
        )

    def obter_historico(self):

        return HISTORICO_OCORRENCIAS

    def verificar_agente(self, nome_agente):

        ativo = status_agente(nome_agente)

        if ativo:
            return True

        return False

    def analisar_solicitacao(self, agente):

        if self.verificar_agente(agente):

            return f"Agente {agente} disponivel"

        self.registrar_ocorrencia(
            f"Agente {agente} indisponivel"
        )

        return f"Agente {agente} indisponivel"


if __name__ == "__main__":

    supervisor = Supervisor()

    print(
        supervisor.analisar_solicitacao(
            "pesquisa_avancada"
        )
    )

    print(
        supervisor.obter_historico()
    )
