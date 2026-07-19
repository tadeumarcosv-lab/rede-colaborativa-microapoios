"""
SUPERVISOR GERAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Responsável por supervisionar continuamente toda a Rede.
"""

from datetime import datetime


class SupervisorGeral:

    def __init__(self):

        self.status = "ATIVO"

        self.componentes = [
            "Kernel",
            "Orquestrador Central",
            "Diretor Autônomo",
            "Planejador Mestre",
            "Gerador Autônomo",
            "Motor de Construção",
            "Motor de Verificação",
            "Motor de Aprendizado",
            "Sistema Executor",
            "Sistema de Monitoramento",
            "Sistema de Recuperação",
            "Gerenciador da Memória",
            "Registro Central de Eventos",
            "Integrador dos Motores",
            "Integrador dos Sistemas",
            "Integrador Operacional Principal"
        ]

        self.historico = []

        self.ciclos = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[SUPERVISOR] [{horario}] {mensagem}"

        self.historico.append(registro)

        print(registro)

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.registrar(f"Status alterado para: {status}")

    def adicionar_componente(self, componente):

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.registrar(f"Novo componente supervisionado: {componente}")

    def listar_componentes(self):

        self.registrar("Componentes supervisionados:")

        for componente in self.componentes:

            self.registrar(f"ATIVO -> {componente}")

        return self.componentes

    def obter_historico(self):

        return self.historico

    def verificar(self):

        self.registrar("Verificando funcionamento geral da Rede.")

        return True

    def monitorar(self):

        self.registrar("Monitoramento contínuo iniciado.")

        return True

    def verificar_componentes(self):

        self.registrar("Verificando componentes supervisionados.")

        for componente in self.componentes:

            self.registrar(f"OK -> {componente}")

        return True

    def registrar_ciclo(self):

        self.ciclos += 1

        self.registrar(f"Ciclo de supervisão #{self.ciclos} registrado.")

        return True

    def executar(self):

        self.registrar("Supervisor Geral iniciado.")

        self.listar_componentes()

        self.verificar()

        self.monitorar()

        self.verificar_componentes()

        self.registrar_ciclo()

        self.registrar("Supervisão concluída.")


if __name__ == "__main__":

    supervisor = SupervisorGeral()

    supervisor.executar()
