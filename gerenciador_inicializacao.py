"""
GERENCIADOR DE INICIALIZAÇÃO DA REDE
Responsável por executar toda a sequência oficial de inicialização.
"""

import bootstrap


class GerenciadorInicializacao:

    def iniciar(self):

        print("========================================")
        print("GERENCIADOR DE INICIALIZAÇÃO")
        print("========================================")

        bootstrap.bootstrap()

        print("========================================")
        print("REDE INICIALIZADA COM SUCESSO")
        print("========================================")


if __name__ == "__main__":

    gerenciador = GerenciadorInicializacao()
    gerenciador.iniciar()
