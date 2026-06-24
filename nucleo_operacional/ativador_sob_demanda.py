from painel_agentes import (
    status_agente,
    ativar_agente
)

from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)


class AtivadorSobDemanda:

    def __init__(self):

        self.ocorrencias = GerenciadorOcorrencias()

    def solicitar_agente(self, nome_agente):

        if status_agente(nome_agente):

            return f"{nome_agente} já está ativo"

        ativar_agente(nome_agente)

        self.ocorrencias.registrar(
            "ATIVACAO",
            f"{nome_agente} ativado sob demanda"
        )

        return f"{nome_agente} ativado automaticamente"


if __name__ == "__main__":

    ativador = AtivadorSobDemanda()

    print(
        ativador.solicitar_agente(
            "pesquisa_avancada"
        )
)
