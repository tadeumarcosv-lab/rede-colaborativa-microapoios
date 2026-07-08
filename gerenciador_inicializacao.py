"""
GERENCIADOR DE INICIALIZAÇÃO
DA REDE COLABORATIVA DE MICROAPOIOS

Autor: Tadeu Marcos Viana

Responsável por executar toda a sequência oficial de inicialização.
"""

from nucleo_operacional.supervisor import Supervisor
from nucleo_operacional.integracao_completa import IntegracaoCompleta


class GerenciadorInicializacao:

    def iniciar(self):

        print("========================================")
        print("GERENCIADOR DE INICIALIZAÇÃO")
        print("========================================")

        print("Supervisor inicializado.")

        supervisor_rede = Supervisor()

        print("Supervisor ativo.")

        print("Iniciando integração operacional da Rede...")

        sistema = IntegracaoCompleta()

        resultado = sistema.executar(
            "Inicialização Oficial da Rede"
        )

        print(resultado)

        print("========================================")
        print("REDE INICIALIZADA COM SUCESSO")
        print("========================================")


if __name__ == "__main__":

    gerenciador = GerenciadorInicializacao()

    gerenciador.iniciar()
