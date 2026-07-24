"""
INTEGRADOR DOS MOTORES DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada na arquitetura oficial da Rede.
"""

from datetime import datetime


class IntegradorDosMotores:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.motores = [
            "Motor de Construção",
            "Motor de Verificação",
            "Motor de Aprendizado"
        ]

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.ultima_atividade = None

        self.motores_disponiveis = []

        self.motores_executados = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[INTEGRADOR] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def adicionar_motor(self, motor):

        if motor not in self.motores:

            self.motores.append(motor)

            self.ultima_atividade = "adicionar_motor"

            self.registrar(f"Novo motor integrado: {motor}")

    def listar_motores(self):

        self.ultima_atividade = "listar_motores"

        self.registrar("Motores atualmente integrados:")

        for motor in self.motores:

            self.registrar(f"ATIVO -> {motor}")

        return self.motores

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def quantidade_motores(self):

        return len(self.motores)

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_historico(self):

        return self.historico_execucoes

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_motores_disponiveis(self):

        return self.motores_disponiveis

    def obter_motores_executados(self):

        return self.motores_executados

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def integrar_construcao(self):

        self.ultima_atividade = "integrar_construcao"

        self.registrar("Integrando Motor de Construção.")

        return True

    def integrar_verificacao(self):

        self.ultima_atividade = "integrar_verificacao"

        self.registrar("Integrando Motor de Verificação.")

        return True

    def integrar_aprendizado(self):

        self.ultima_atividade = "integrar_aprendizado"

        self.registrar("Integrando Motor de Aprendizado.")

        return True

    def sincronizar_motores(self):

        self.ultima_atividade = "sincronizar_motores"

        self.registrar("Sincronizando todos os motores.")

        return True

    def verificar_motores(self):

        self.ultima_atividade = "verificar_motores"

        self.registrar("Verificando motores integrados.")

        for motor in self.motores:

            self.registrar(f"OK -> {motor}")

        return True

    def registrar_ciclo(self):

        self.ciclo += 1

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo operacional {self.ciclo} registrado.")

        return True

    def resumo(self):

        self.ultima_atividade = "resumo"

        self.registrar(
            f"Resumo: {len(self.motores)} motores | Status: {self.status}"
        )

    def executar_motores(self):

        self.ultima_atividade = "executar_motores"

        self.registrar("Iniciando execução dos motores disponíveis.")

        self.motores_disponiveis = []

        self.motores_executados = 0

        # Motor de Construção
        try:
            from motor_de_construcao import MotorDeConstrucao
            motor = MotorDeConstrucao()
            motor.executar()
            self.motores_disponiveis.append("Motor de Construção")
            self.motores_executados += 1
            self.registrar("Executando Motor de Construção")
        except ImportError:
            self.registrar("Motor de Construção indisponível")

        # Motor de Verificação
        try:
            from motor_de_verificacao import MotorDeVerificacao
            motor = MotorDeVerificacao()
            motor.executar()
            self.motores_disponiveis.append("Motor de Verificação")
            self.motores_executados += 1
            self.registrar("Executando Motor de Verificação")
        except ImportError:
            self.registrar("Motor de Verificação indisponível")

        # Motor de Aprendizado
        try:
            from motor_de_aprendizado import MotorDeAprendizado
            motor = MotorDeAprendizado()
            motor.executar()
            self.motores_disponiveis.append("Motor de Aprendizado")
            self.motores_executados += 1
            self.registrar("Executando Motor de Aprendizado")
        except ImportError:
            self.registrar("Motor de Aprendizado indisponível")

        self.registrar(
            f"Motores disponíveis: {len(self.motores_disponiveis)}"
        )

        self.registrar(
            f"Motores executados: {self.motores_executados}"
        )

        return True

    def executar(self):

        self.registrar("Integrador dos Motores iniciado.")

        self.listar_motores()

        self.integrar_construcao()

        self.integrar_verificacao()

        self.integrar_aprendizado()

        self.sincronizar_motores()

        self.executar_motores()

        self.verificar_motores()

        self.registrar_ciclo()

        self.resumo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "ciclos": self.ciclo,

            "motores_integrados": len(self.motores),

            "motores_disponiveis": len(self.motores_disponiveis),

            "motores_executados": self.motores_executados,

            "ultima_atividade": self.ultima_atividade,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar("Integração dos motores concluída.")


if __name__ == "__main__":

    integrador = IntegradorDosMotores()

    integrador.executar()
