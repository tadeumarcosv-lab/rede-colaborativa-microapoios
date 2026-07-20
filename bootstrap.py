"""
BOOTSTRAP DA REDE COLABORATIVA DE MICROAPOIOS

Responsável por iniciar oficialmente toda a Rede.
"""

from datetime import datetime

from kernel import KernelDaRede


def registrar(mensagem):

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(f"[BOOTSTRAP] [{horario}] {mensagem}")


def bootstrap():

    inicio = datetime.now()

    print("========================================")
    print("BOOTSTRAP DA REDE")
    print("Iniciando sequência oficial...")
    print("========================================")

    registrar("Inicialização iniciada.")

    kernel = KernelDaRede()

    kernel.executar()

    fim = datetime.now()

    tempo = (fim - inicio).total_seconds()

    registrar("Kernel inicializado com sucesso.")

    registrar(f"Tempo de inicialização: {tempo:.2f} segundos.")

    registrar("Bootstrap finalizado.")

    print("========================================")
    print("Bootstrap concluído.")
    print("========================================")


if __name__ == "__main__":

    bootstrap()
