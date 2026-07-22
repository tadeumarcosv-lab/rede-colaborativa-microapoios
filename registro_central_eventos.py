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

        self.status = "ATIVO"

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.total_registros = 0

        self.ultimo_responsavel = None

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

        self.total_registros += 1

        self.ultimo_responsavel = responsavel

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

        if self.eventos:

            return self.eventos[-1]

        return None

    def consultar_por_importancia(self, importancia):

        return [

            evento

            for evento in self.eventos

            if evento["importancia"] == importancia

        ]

    def consultar_por_responsavel(self, responsavel):

        return [

            evento

            for evento in self.eventos

            if evento["responsavel"] == responsavel

        ]

    def listar_resumo(self):

        print()

        print("===== RESUMO DO REGISTRO =====")

        print(f"Status: {self.status}")

        print(f"Eventos registrados: {len(self.eventos)}")

        if self.eventos:

            ultimo = self.eventos[-1]

            print(f"Último evento: {ultimo['descricao']}")

        print("==============================")

    def alterar_status(self, novo_status):

        self.status = novo_status

    def limpar(self):

        self.eventos = []

    def obter_status(self):

        return {

            "status": self.status,

            "eventos_registrados": len(self.eventos),

            "memoria_integrada": True

        }

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_total_registros(self):

        return self.total_registros

    def obter_ultimo_responsavel(self):

        return self.ultimo_responsavel

    def limpar_historico_execucoes(self):

        self.historico_execucoes.clear()

    def executar(self):

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "eventos_registrados": len(self.eventos),

            "total_registros": self.total_registros,

            "ultimo_responsavel": self.ultimo_responsavel,

            "ultima_execucao": self.ultima_execucao,

            "memoria_integrada": True

        }

        self.historico_execucoes.append(self.resumo_operacional)

        self.listar_resumo()


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

    registro.executar()

    print()

    print("Quantidade:", registro.quantidade_eventos())

    print()

    print(registro.consultar_eventos())
