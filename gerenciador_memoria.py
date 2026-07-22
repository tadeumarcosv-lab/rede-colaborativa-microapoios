"""
GERENCIADOR DA MEMÓRIA
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por manipular memoria.json
"""

import json
import os
from datetime import datetime


class GerenciadorMemoria:

    ARQUIVO = "memoria.json"

    def __init__(self):

        self.status = "ATIVO"

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.total_operacoes = 0

        self.ultima_operacao = None

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

        self.total_operacoes += 1

        self.ultima_operacao = "adicionar_historico"

    def adicionar_aprendizado(self, aprendizado):

        memoria = self.carregar()

        memoria["aprendizados"].append(aprendizado)

        memoria["estatisticas"]["aprendizados_registrados"] += 1

        self.salvar(memoria)

        self.total_operacoes += 1

        self.ultima_operacao = "adicionar_aprendizado"

    def adicionar_decisao(self, decisao):

        memoria = self.carregar()

        memoria["decisoes"].append(decisao)

        memoria["estatisticas"]["decisoes_registradas"] += 1

        self.salvar(memoria)

        self.total_operacoes += 1

        self.ultima_operacao = "adicionar_decisao"

    def adicionar_conhecimento(self, conhecimento):

        memoria = self.carregar()

        memoria["conhecimento"].append(conhecimento)

        self.salvar(memoria)

        self.total_operacoes += 1

        self.ultima_operacao = "adicionar_conhecimento"

    def adicionar_contexto(self, contexto):

        memoria = self.carregar()

        memoria["contexto"].append(contexto)

        self.salvar(memoria)

        self.total_operacoes += 1

        self.ultima_operacao = "adicionar_contexto"

    def obter_estatisticas(self):

        memoria = self.carregar()

        return memoria["estatisticas"]

    def obter_historico(self):

        memoria = self.carregar()

        return memoria["historico"]

    def obter_aprendizados(self):

        memoria = self.carregar()

        return memoria["aprendizados"]

    def obter_decisoes(self):

        memoria = self.carregar()

        return memoria["decisoes"]

    def obter_conhecimento(self):

        memoria = self.carregar()

        return memoria["conhecimento"]

    def obter_contexto(self):

        memoria = self.carregar()

        return memoria["contexto"]

    def obter_status(self):

        return self.status

    def alterar_status(self, novo_status):

        self.status = novo_status

    def verificar_memoria(self):

        return os.path.exists(self.ARQUIVO)

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_total_operacoes(self):

        return self.total_operacoes

    def obter_ultima_operacao(self):

        return self.ultima_operacao

    def limpar_historico_execucoes(self):

        self.historico_execucoes.clear()

    def resumo(self):

        estatisticas = self.obter_estatisticas()

        print()

        print("===== MEMÓRIA =====")

        print(f"Status: {self.status}")

        print(f"Solicitações: {estatisticas['solicitacoes']}")

        print("===================")

    def executar(self):

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "total_operacoes": self.total_operacoes,

            "ultima_operacao": self.ultima_operacao,

            "arquivo_memoria": self.ARQUIVO,

            "ultima_execucao": self.ultima_execucao

        }

        self.historico_execucoes.append(self.resumo_operacional)

        self.resumo()


if __name__ == "__main__":

    memoria = GerenciadorMemoria()

    memoria.adicionar_historico(
        "Primeiro teste da memória."
    )

    memoria.executar()

    print(memoria.carregar())
