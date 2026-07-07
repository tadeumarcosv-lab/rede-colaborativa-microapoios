"""
AGENTE DE MEMÓRIA ESTRATÉGICA
Rede Colaborativa de Microapoios

Responsável por registrar, recuperar e organizar
informações estratégicas da Rede.
"""


class AgenteMemoriaEstrategica:

    def __init__(self):

        self.nome = "Agente de Memoria Estrategica"
        self.codigo = "AGENTE-0005"
        self.status = "ativo"
        self.memoria = []

    def registrar(self, informacao):

        self.memoria.append(informacao)

        return "Informação registrada."

    def consultar(self):

        return self.memoria

    def status_operacional(self):

        return {

            "agente": self.nome,

            "status": self.status,

            "registros": len(self.memoria)

        }

    def executar(self, entrada):

        self.registrar(entrada)

        return {

            "agente": self.nome,

            "entrada": entrada,

            "memoria": self.consultar(),

            "status": self.status

        }


if __name__ == "__main__":

    memoria = AgenteMemoriaEstrategica()

    print(

        memoria.executar(

            "Teste de memória estratégica"

        )

    )
