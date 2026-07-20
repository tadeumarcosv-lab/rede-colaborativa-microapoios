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

        self.etapas_executadas = 0

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

    def obter_status(self):

        return {

            "status": self.status,

            "etapas": len(self.etapas),

            "executadas": self.etapas_executadas

        }

    def iniciar(self):

        inicio = datetime.now()

        self.status = "EXECUTANDO"

        self.registrar("Gerenciador iniciado.")

        self.listar_etapas()

        supervisor = Supervisor()

        self.etapas_executadas += 1

        self.registrar("Supervisor ativo.")

        sistema = IntegracaoCompleta()

        self.etapas_executadas += 1

        resultado = sistema.executar(
            "Inicialização Oficial da Rede"
        )

        print(resultado)

        self.status = "OPERACIONAL"

        fim = datetime.now()

        tempo = (fim - inicio).total_seconds()

        self.registrar("Rede inicializada com sucesso.")

        self.registrar(f"Status atual: {self.status}")

        self.registrar(
            f"Etapas executadas: {self.etapas_executadas}"
        )

        self.registrar(
            f"Tempo de inicialização: {tempo:.2f} segundos"
        )


if __name__ == "__main__":

    gerenciador = GerenciadorInicializacao()

    gerenciador.iniciar()
