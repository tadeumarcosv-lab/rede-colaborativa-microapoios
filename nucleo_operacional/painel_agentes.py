"""
PAINEL DE CONTROLE DOS AGENTES
Rede Colaborativa de Microapoios

Permite ativar e desativar agentes.
"""

AGENTES_ATIVOS = {

    "central": True,

    "coordenacao": True,

    "comunicacao": True,

    "pesquisa_avancada": True,

    "memoria_estrategica": True,

    "gestao_conhecimento": True

}


def listar_agentes():

    return AGENTES_ATIVOS


def ativar_agente(nome):

    if nome in AGENTES_ATIVOS:

        AGENTES_ATIVOS[nome] = True

        return f"{nome} ativado"

    return "Agente nao encontrado"


def desativar_agente(nome):

    if nome in AGENTES_ATIVOS:

        AGENTES_ATIVOS[nome] = False

        return f"{nome} desativado"

    return "Agente nao encontrado"


def status_agente(nome):

    if nome in AGENTES_ATIVOS:

        return AGENTES_ATIVOS[nome]

    return None


if __name__ == "__main__":

    print("PAINEL DE AGENTES")

    print(listar_agentes())
