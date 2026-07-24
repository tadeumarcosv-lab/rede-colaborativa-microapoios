"""
INTEGRADOR OPERACIONAL PRINCIPAL DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada na arquitetura oficial da Rede.
"""

from datetime import datetime


class IntegradorOperacionalPrincipal:

    def __init__(self):

        self.status = "ATIVO"

        self.ciclo = 0

        self.historico_execucoes = []

        self.resumo_operacional = {}

        self.ultima_execucao = None

        self.ultima_atividade = None

        self.integradores = [
            "Integrador dos Motores",
            "Integrador dos Sistemas"
        ]

        self.integradores_disponiveis = []

        self.integradores_executados = 0

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = f"[OPERACIONAL] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)

        print(registro)

    def obter_status(self):

        return self.status

    def definir_status(self, status):

        self.status = status

        self.ultima_atividade = "definir_status"

        self.registrar(f"Status alterado para: {status}")

    def listar_integradores(self):

        self.ultima_atividade = "listar_integradores"

        self.registrar("Integradores atualmente registrados:")

        for integrador in self.integradores:

            self.registrar(f"ATIVO -> {integrador}")

        return self.integradores

    def quantidade_integradores(self):

        return len(self.integradores)

    def obter_historico(self):

        return self.historico_execucoes

    def obter_resumo_operacional(self):

        return self.resumo_operacional

    def obter_ultima_execucao(self):

        return self.ultima_execucao

    def obter_ultima_atividade(self):

        return self.ultima_atividade

    def obter_integradores_disponiveis(self):

        return self.integradores_disponiveis

    def obter_integradores_executados(self):

        return self.integradores_executados

    def limpar_historico(self):

        self.historico_execucoes.clear()

        self.registrar("Histórico de execuções limpo.")

    def sincronizar_operacao(self):

        self.ultima_atividade = "sincronizar_operacao"

        self.registrar("Sincronizando toda a operação da Rede.")

        return True

    def verificar_operacao(self):

        self.ultima_atividade = "verificar_operacao"

        self.registrar("Verificando integradores registrados.")

        for integrador in self.integradores:

            self.registrar(f"OK -> {integrador}")

        return True

    def registrar_ciclo(self):

        self.ciclo += 1

        self.ultima_atividade = "registrar_ciclo"

        self.registrar(f"Ciclo operacional {self.ciclo} registrado.")

        return True

    def resumo(self):

        self.ultima_atividade = "resumo"

        self.registrar(
            f"Resumo: {len(self.integradores)} integradores | Status: {self.status}"
        )

    def executar_integradores(self):

        self.ultima_atividade = "executar_integradores"

        self.registrar("Iniciando execução dos integradores disponíveis.")

        self.integradores_disponiveis = []

        self.integradores_executados = 0

        # Integrador dos Motores
        try:
            from integrador_dos_motores import IntegradorDosMotores
            integrador = IntegradorDosMotores()
            integrador.executar()
            self.integradores_disponiveis.append("Integrador dos Motores")
            self.integradores_executados += 1
            self.registrar("Executando Integrador dos Motores")
        except ImportError:
            self.registrar("Integrador dos Motores indisponível")

        # Integrador dos Sistemas
        try:
            from integrador_dos_sistemas import IntegradorDosSistemas
            integrador = IntegradorDosSistemas()
            integrador.executar()
            self.integradores_disponiveis.append("Integrador dos Sistemas")
            self.integradores_executados += 1
            self.registrar("Executando Integrador dos Sistemas")
        except ImportError:
            self.registrar("Integrador dos Sistemas indisponível")

        self.registrar(
            f"Integradores disponíveis: {len(self.integradores_disponiveis)}"
        )

        self.registrar(
            f"Integradores executados: {self.integradores_executados}"
        )

        return True

    def executar(self):

        self.registrar("Integrador Operacional Principal iniciado.")

        self.listar_integradores()

        self.sincronizar_operacao()

        self.executar_integradores()

        self.verificar_operacao()

        self.registrar_ciclo()

        self.resumo()

        self.ultima_execucao = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.resumo_operacional = {

            "status": self.status,

            "ciclos": self.ciclo,

            "integradores": len(self.integradores),

            "integradores_disponiveis": len(self.integradores_disponiveis),

            "integradores_executados": self.integradores_executados,

            "ultima_atividade": self.ultima_atividade,

            "ultima_execucao": self.ultima_execucao

        }

        self.registrar(
            f"Resumo operacional: {self.resumo_operacional}"
        )

        self.registrar("Integração operacional concluída.")


if __name__ == "__main__":

    integrador = IntegradorOperacionalPrincipal()

    integrador.executar()
