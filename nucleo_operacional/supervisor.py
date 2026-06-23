from painel_agentes import status_agente


class Supervisor:

    def verificar_agente(self, nome_agente):

        ativo = status_agente(nome_agente)

        if ativo:
            return True

        return False

    def analisar_solicitacao(self, agente):

        if self.verificar_agente(agente):

            return f"Agente {agente} disponível"

        return f"Agente {agente} indisponível"


if __name__ == "__main__":

    supervisor = Supervisor()

    print(
        supervisor.analisar_solicitacao(
            "pesquisa_avancada"
        )
      )
