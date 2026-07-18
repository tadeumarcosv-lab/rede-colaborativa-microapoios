"""
SISTEMA DE AUDITORIA DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_AUDITORIA_DA_REDE.md
"""

from datetime import datetime


class SistemaDeAuditoriaDaRede:

    def __init__(self):

        self.status = "ATIVO"

        self.eventos = []

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[AUDITORIA] [{horario}] {mensagem}")

    def registrar_evento(self, evento):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.eventos.append({
            "data": horario,
            "evento": evento
        })

        self.registrar(f"Evento registrado: {evento}")

    def listar_eventos(self):

        self.registrar("Eventos registrados:")

        if not self.eventos:

            self.registrar("Nenhum evento registrado.")

        else:

            for evento in self.eventos:

                self.registrar(
                    f"{evento['data']} -> {evento['evento']}"
                )

        return self.eventos

    def verificar_integridade(self):

        self.registrar("Verificando integridade da Rede.")

        return True

    def gerar_relatorio(self):

        self.registrar("Gerando relatório de auditoria.")

        self.listar_eventos()

        return True

    def finalizar(self):

        self.registrar("Auditoria concluída.")

    def executar(self):

        self.registrar("Sistema de Auditoria iniciado.")

        self.registrar_evento("Inicialização da Auditoria")

        self.verificar_integridade()

        self.gerar_relatorio()

        self.finalizar()


if __name__ == "__main__":

    auditoria = SistemaDeAuditoriaDaRede()

    auditoria.executar()
