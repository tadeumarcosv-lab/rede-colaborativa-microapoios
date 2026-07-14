"""
SISTEMA DE MONITORAMENTO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsabilidade:

- Monitorar continuamente os principais componentes da Rede.
- Registrar o estado operacional.
- Informar componentes indisponíveis.
- Preparar a integração com Auditoria, Recuperação e Autocorreção.

"""

from datetime import datetime


class SistemaDeMonitoramentoDaRede:

    def __init__(self):

        self.componentes = []

    def adicionar_componente(self, nome, objeto):

        self.componentes.append((nome, objeto))

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[MONITORAMENTO] [{horario}] {mensagem}")

    def verificar(self):

        self.registrar("Iniciando monitoramento da Rede.")

        if not self.componentes:

            self.registrar("Nenhum componente registrado para monitoramento.")
            return

        for nome, componente in self.componentes:

            try:

                status = "ATIVO" if componente is not None else "INATIVO"

                self.registrar(f"{nome}: {status}")

            except Exception as erro:

                self.registrar(f"{nome}: ERRO -> {erro}")

        self.registrar("Monitoramento concluído.")

    def executar(self):

        self.verificar()


if __name__ == "__main__":

    monitoramento = SistemaDeMonitoramentoDaRede()

    monitoramento.executar()
