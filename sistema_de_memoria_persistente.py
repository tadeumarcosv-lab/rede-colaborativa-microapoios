"""
SISTEMA DE MEMÓRIA PERSISTENTE
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_MEMORIA_PERSISTENTE.md
"""

from datetime import datetime
import json
import os


class SistemaDeMemoriaPersistente:

    def __init__(self):

        self.arquivo = "memoria_persistente.json"

        self.status = "ATIVO"

        self.memoria = []

        self.carregar()

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[MEMORIA] [{horario}] {mensagem}")

    def carregar(self):

        if os.path.exists(self.arquivo):

            with open(self.arquivo, "r", encoding="utf-8") as arquivo:

                self.memoria = json.load(arquivo)

            self.registrar("Memória carregada.")

        else:

            self.memoria = []

            self.registrar("Nova memória criada.")

    def salvar(self):

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:

            json.dump(self.memoria, arquivo, indent=4, ensure_ascii=False)

        self.registrar("Memória salva.")

    def adicionar(self, tipo, descricao):

        registro = {

            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            "tipo": tipo,

            "descricao": descricao

        }

        self.memoria.append(registro)

        self.registrar(f"Registro adicionado: {tipo}")

        self.salvar()

    def listar(self):

        self.registrar("Listando memória persistente.")

        for registro in self.memoria:

            print(registro)

    def executar(self):

        self.registrar("Sistema de Memória Persistente iniciado.")

        self.adicionar(

            "Inicialização",

            "Sistema iniciado corretamente."

        )

        self.listar()

        self.registrar("Sistema finalizado.")


if __name__ == "__main__":

    memoria = SistemaDeMemoriaPersistente()

    memoria.executar()
