"""
GERENCIADOR DA MEMÓRIA
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por manipular memoria.json
"""

import json
import os


class GerenciadorMemoria:

    ARQUIVO = "memoria.json"

    def __init__(self):

        if not os.path.exists(self.ARQUIVO):

            raise FileNotFoundError(
                "Arquivo memoria.json não encontrado."
            )

    def carregar(self):

        with open(
            self.ARQUIVO,
            "r",
            encoding="utf-8"
        ) as arquivo:

            return json.load(arquivo)

    def salvar(self, memoria):

        with open(
            self.ARQUIVO,
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                memoria,
                arquivo,
                indent=2,
                ensure_ascii=False
            )

    def adicionar_historico(self, registro):

        memoria = self.carregar()

        memoria["historico"].append(registro)

        memoria["estatisticas"]["solicitacoes"] += 1

        self.salvar(memoria)

    def adicionar_aprendizado(self, aprendizado):

        memoria = self.carregar()

        memoria["aprendizados"].append(aprendizado)

        memoria["estatisticas"]["aprendizados_registrados"] += 1

        self.salvar(memoria)

    def adicionar_decisao(self, decisao):

        memoria = self.carregar()

        memoria["decisoes"].append(decisao)

        memoria["estatisticas"]["decisoes_registradas"] += 1

        self.salvar(memoria)

    def adicionar_conhecimento(self, conhecimento):

        memoria = self.carregar()

        memoria["conhecimento"].append(conhecimento)

        self.salvar(memoria)

    def adicionar_contexto(self, contexto):

        memoria = self.carregar()

        memoria["contexto"].append(contexto)

        self.salvar(memoria)


if __name__ == "__main__":

    memoria = GerenciadorMemoria()

    memoria.adicionar_historico(
        "Primeiro teste da memória."
    )

    print(memoria.carregar())
