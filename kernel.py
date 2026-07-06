"""
KERNEL DA REDE COLABORATIVA DE MICROAPOIOS

Autor: Tadeu Marcos Viana

Responsabilidade:
Inicializar toda a Rede.
"""

import os
from datetime import datetime

import gerenciador_inicializacao

VERSAO = "1.1"

DOCUMENTOS_PRINCIPAIS = [
    "CONSTITUICAO_DA_REDE.md",
    "DNA_DA_REDE.md",
    "ARQUITETURA_MESTRA.md",
    "SISTEMA_OPERACIONAL_DA_REDE_PARTE_1.md",
    "KERNEL_DA_REDE.md",
    "BOOTSTRAP_DA_REDE.md"
]


def registrar(mensagem):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"[{horario}] {mensagem}")


def verificar_documentos():

    registrar("Verificando documentos principais...")

    faltando = []

    for documento in DOCUMENTOS_PRINCIPAIS:

        if os.path.exists(documento):
            registrar(f"OK -> {documento}")

        else:
            registrar(f"FALTANDO -> {documento}")
            faltando.append(documento)

    return faltando


def iniciar():

    registrar("====================================")
    registrar("INICIALIZANDO KERNEL DA REDE")
    registrar(f"VERSÃO {VERSAO}")
    registrar("====================================")

    faltando = verificar_documentos()

    if len(faltando) == 0:

        registrar("Todos os documentos principais foram encontrados.")
        registrar("Kernel inicializado com sucesso.")

        registrar("Transferindo controle ao Gerenciador de Inicialização...")

        gerenciador = gerenciador_inicializacao.GerenciadorInicializacao()
        gerenciador.iniciar()

    else:

        registrar("Existem documentos ausentes.")
        registrar("Inicialização interrompida.")


if __name__ == "__main__":
    iniciar()
