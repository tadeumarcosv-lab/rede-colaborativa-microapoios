"""
AGENTE DE GESTAO DO CONHECIMENTO
Rede Colaborativa de Microapoios

Responsável por organizar,
catalogar e estruturar conhecimentos.
"""

class AgenteGestaoConhecimento:

    def __init__(self):
        self.nome = "Agente de Gestao do Conhecimento"
        self.codigo = "AGENTE-0006"
        self.status = "ativo"
        self.base_conhecimento = {}

    def registrar_conhecimento(self, chave, conteudo):

        self.base_conhecimento[chave] = conteudo

        return {
            "agente": self.nome,
            "acao": "conhecimento_registrado",
            "chave": chave
        }

    def consultar_conhecimento(self, chave):

        return self.base_conhecimento.get(
            chave,
            "Conhecimento nao encontrado"
        )

    def status_operacional(self):

        return {
            "agente": self.nome,
            "status": self.status,
            "registros": len(self.base_conhecimento)
        }


if __name__ == "__main__":

    conhecimento = AgenteGestaoConhecimento()

    conhecimento.registrar_conhecimento(
        "missao",
        "Fortalecer a Rede Colaborativa de Microapoios"
    )

    print(
        conhecimento.consultar_conhecimento(
            "missao"
        )
    )

    print(
        conhecimento.status_operacional()
      )
