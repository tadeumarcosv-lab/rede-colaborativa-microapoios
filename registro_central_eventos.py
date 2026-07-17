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

    def obter_ultimo_evento(self):
        """
        Retorna o último evento registrado.
        """

        if self.eventos:

            return self.eventos[-1]

        return None

    def consultar_por_importancia(self, importancia):
        """
        Retorna todos os eventos de uma determinada importância.
        """

        return [

            evento

            for evento in self.eventos

            if evento["importancia"] == importancia

        ]

    def consultar_por_responsavel(self, responsavel):
        """
        Retorna todos os eventos registrados por um responsável.
        """

        return [

            evento

            for evento in self.eventos

            if evento["responsavel"] == responsavel

        ]

    def limpar(self):

        self.eventos = []

    def obter_status(self):
        """
        Retorna o estado atual do Registro Central de Eventos.
        """

        return {

            "eventos_registrados": len(self.eventos),

            "memoria_integrada": True

        }


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
