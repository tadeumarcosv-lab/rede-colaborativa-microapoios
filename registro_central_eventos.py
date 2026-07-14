"""
REGISTRO CENTRAL DE EVENTOS
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana
"""

from datetime import datetime

from gerenciador_memoria import GerenciadorMemoria


class RegistroCentralEventos:

    def __init__(self):

        self.eventos = []

        self.memoria = GerenciadorMemoria()

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

        self.memoria.adicionar_historico(evento)

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
