"""
GERENCIADOR DE INICIALIZAÇÃO
DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por executar toda a sequência oficial de inicialização.
"""

from datetime import datetime

from nucleo_operacional.supervisor import Supervisor
from nucleo_operacional.integracao_completa import IntegracaoCompleta


class GerenciadorInicializacao:

    def __init__(self):

        self.status = "PRONTO"

        self.etapas = [

            "Inicializar Supervisor",

            "Inicializar Integração",

            "Executar Bootstrap",

            "Validar Inicialização",

            "Finalizar Inicialização"

        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[INICIALIZAÇÃO] [{horario}] {mensagem}")

    def listar_etapas(self):

        self.registrar("Etapas oficiais:")

        for etapa in self.etapas:

            self.registrar(f"ETAPA -> {etapa}")

        return self.etapas

    def adicionar_etapa(self, etapa):

        if etapa not in self.etapas:

            self.etapas.append(etapa)

            self.registrar(f"Nova etapa registrada: {etapa}")

    def iniciar(self):

        self.status = "EXECUTANDO"

        self.registrar("Gerenciador iniciado.")

        self.listar_etapas()

        supervisor = Supervisor()

        self.registrar("Supervisor ativo.")

        sistema = IntegracaoCompleta()

        resultado = sistema.executar(
            "Inicialização Oficial da Rede"
        )

        print(resultado)

        self.status = "OPERACIONAL"

        self.registrar("Rede inicializada com sucesso.")

        self.registrar(f"Status atual: {self.status}")


if __name__ == "__main__":

    gerenciador = GerenciadorInicializacao()

    gerenciador.iniciar()
