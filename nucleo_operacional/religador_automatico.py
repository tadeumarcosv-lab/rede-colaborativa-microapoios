from painel_agentes import (
    AGENTES_ATIVOS,
    ativar_agente,
    status_agente
)

class ReligadorAutomatico:

    def verificar_e_religar(self, nome_agente):

        if status_agente(nome_agente):
            return f"{nome_agente} já está ativo"

        ativar_agente(nome_agente)

        return f"{nome_agente} foi religado automaticamente"


if __name__ == "__main__":

    religador = ReligadorAutomatico()

    print(
        religador.verificar_e_religar(
            "pesquisa_avancada"
        )
      )
