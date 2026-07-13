"""
REGISTRO CENTRAL DE EVENTOS
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
REGISTRO_CENTRAL_DE_EVENTOS.md
"""

from datetime import datetime


class RegistroCentralEventos:

    def __init__(self):

        self.eventos = []

    def registrar(
        self,
        origem,
        destino,
        responsavel,
        descricao,
        resultado,
        importancia
    ):

        evento = {

            "data": datetime.now().strftime("%d/%m/%Y"),

            "hora": datetime.now().strftime("%H:%M:%S"),

            "origem": origem,

            "destino": destino,

            "responsavel": responsavel,

            "descricao": descricao,

            "resultado": resultado,

            "importancia": importancia

        }

        self.eventos.append(evento)

        print(
            f"[EVENTO] "
            f"{evento['data']} "
            f"{evento['hora']} | "
            f"{descricao}"
        )

    def consultar_eventos(self):

        return self.eventos

    def quantidade_eventos(self):

        return len(self.eventos)

    def limpar(self):

        self.eventos = []


if __name__ == "__main__":

    registro = RegistroCentralEventos()

    registro.registrar(

        origem="Bootstrap",

        destino="Kernel",

        responsavel="Sistema",

        descricao="Primeiro evento registrado.",

        resultado="OK",

        importancia="ALTA"

    )

    print()

    print("Quantidade:", registro.quantidade_eventos())

    print()

    print(registro.consultar_eventos())
