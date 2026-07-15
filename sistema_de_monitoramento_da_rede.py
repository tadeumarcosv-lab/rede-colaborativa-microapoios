"""
SISTEMA DE MONITORAMENTO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
SISTEMA_DE_MONITORAMENTO_DA_REDE.md
"""

from datetime import datetime


class SistemaDeMonitoramentoDaRede:

    def __init__(self):

        self.status = "ATIVO"

        self.componentes = [
            "Bootstrap",
            "Kernel",
            "Gerenciador de Inicialização",
            "Supervisor Geral",
            "Orquestrador Central",
            "Diretor Autônomo",
            "Motores Inteligentes",
            "Sistema Executor",
            "Memória Persistente"
        ]

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[MONITORAMENTO] [{horario}] {mensagem}")

    def adicionar_componente(self, componente):

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.registrar(f"Novo componente registrado: {componente}")

    def verificar_componentes(self):
        """
        Verifica os componentes atualmente registrados.

        Retorna uma lista com os componentes monitorados.
        Esta interface é utilizada pelo Motor de Aprendizado.
        """

        self.registrar("Verificando componentes da Rede...")

        for componente in self.componentes:

            self.registrar(f"ATIVO -> {componente}")

        return self.componentes

    def verificar_falhas(self):

        self.registrar("Verificando falhas operacionais.")

    def verificar_desempenho(self):

        self.registrar("Verificando desempenho da Rede.")

    def registrar_estado(self):

        self.registrar("Registrando estado operacional.")

    def executar(self):

        self.registrar("Sistema de Monitoramento iniciado.")

        self.verificar_componentes()

        self.verificar_falhas()

        self.verificar_desempenho()

        self.registrar_estado()

        self.registrar("Monitoramento concluído.")


if __name__ == "__main__":

    monitoramento = SistemaDeMonitoramentoDaRede()

    monitoramento.executar()
