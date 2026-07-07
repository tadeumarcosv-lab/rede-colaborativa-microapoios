"""
AGENTE DE GESTÃO DO CONHECIMENTO
Rede Colaborativa de Microapoios

Responsável por organizar, consolidar e disponibilizar
o conhecimento produzido pela Rede.
"""


class AgenteGestaoConhecimento:

    def __init__(self):

        self.nome = "Agente de Gestao Conhecimento"
        self.codigo = "AGENTE-0006"
        self.status = "ativo"
        self.base_conhecimento = []

    def adicionar_conhecimento(self, informacao):

        self.base_conhecimento.append(informacao)

        return "Conhecimento registrado."

    def consultar_conhecimento(self):

        return self.base_conhecimento

    def status_operacional(self):

        return {

            "agente": self.nome,

            "status": self.status,

            "itens": len(self.base_conhecimento)

        }

    def executar(self, entrada):

        self.adicionar_conhecimento(entrada)

        return {

            "agente": self.nome,

            "entrada": entrada,

            "conhecimento": self.consultar_conhecimento(),

            "status": self.status

        }


if __name__ == "__main__":

    conhecimento = AgenteGestaoConhecimento()

    print(

        conhecimento.executar(

            "Teste de gestão do conhecimento"

        )

    )
