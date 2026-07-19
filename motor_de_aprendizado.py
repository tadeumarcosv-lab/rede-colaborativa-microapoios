"""
MOTOR DE APRENDIZADO DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento
MOTOR_DE_APRENDIZADO.md
"""

from datetime import datetime


class MotorDeAprendizado:

    def __init__(self):

        self.status = "ATIVO"

        self.conhecimentos = [
            "Constituição da Rede",
            "DNA da Rede",
            "Arquitetura Mestra",
            "Protocolos Oficiais",
            "Memória Persistente",
            "Monitoramento",
            "Verificação",
            "Construção"
        ]

        self.historico_aprendizado = []

        self.ultimo_aprendizado = None

    def registrar(self, mensagem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"[APRENDIZADO] [{horario}] {mensagem}")

    def adicionar_conhecimento(self, conhecimento):

        if conhecimento not in self.conhecimentos:

            self.conhecimentos.append(conhecimento)

            self.registrar(
                f"Novo conhecimento registrado: {conhecimento}"
            )

    def remover_conhecimento(self, conhecimento):
        """
        Remove um conhecimento da base.
        """

        if conhecimento in self.conhecimentos:

            self.conhecimentos.remove(conhecimento)

            self.registrar(
                f"Conhecimento removido: {conhecimento}"
            )

    def listar_conhecimentos(self):

        self.registrar("Base atual de conhecimentos:")

        for conhecimento in self.conhecimentos:

            self.registrar(f"OK -> {conhecimento}")

        return self.conhecimentos

    def quantidade_conhecimentos(self):
        """
        Retorna a quantidade de conhecimentos registrados.
        """

        return len(self.conhecimentos)

    def obter_status(self):
        """
        Retorna o status atual do Motor de Aprendizado.
        """

        return self.status

    def alterar_status(self, novo_status):
        """
        Altera o status operacional.
        """

        self.status = novo_status

        self.registrar(
            f"Status alterado para: {novo_status}"
        )

    def registrar_aprendizado(self, origem):

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        registro = {
            "origem": origem,
            "horario": horario
        }

        self.historico_aprendizado.append(registro)

        self.ultimo_aprendizado = registro

        self.registrar(
            f"Aprendizado registrado: {origem}"
        )

    def listar_historico(self):

        self.registrar(
            "Histórico de aprendizados:"
        )

        for registro in self.historico_aprendizado:

            self.registrar(
                f"{registro['horario']} -> {registro['origem']}"
            )

        return self.historico_aprendizado

    def obter_ultimo_aprendizado(self):

        return self.ultimo_aprendizado

    def limpar_historico(self):

        self.historico_aprendizado.clear()

        self.ultimo_aprendizado = None

        self.registrar(
            "Histórico de aprendizado limpo."
        )

    def aprender_monitoramento(self):

        self.registrar(
            "Aprendendo com o Sistema de Monitoramento."
        )

        self.registrar_aprendizado(
            "Sistema de Monitoramento"
        )

        return True

    def aprender_verificacao(self):

        self.registrar(
            "Aprendendo com o Motor de Verificação."
        )

        self.registrar_aprendizado(
            "Motor de Verificação"
        )

        return True

    def aprender_construcao(self):

        self.registrar(
            "Aprendendo com o Motor de Construção."
        )

        self.registrar_aprendizado(
            "Motor de Construção"
        )

        return True

    def atualizar_memoria(self):

        self.registrar(
            "Atualizando Memória Persistente."
        )

        return True

    def executar(self):

        self.registrar(
            "Motor de Aprendizado iniciado."
        )

        self.listar_conhecimentos()

        self.aprender_monitoramento()

        self.aprender_verificacao()

        self.aprender_construcao()

        self.atualizar_memoria()

        self.registrar(
            f"Total de conhecimentos: "
            f"{self.quantidade_conhecimentos()}"
        )

        self.registrar(
            f"Aprendizados registrados: "
            f"{len(self.historico_aprendizado)}"
        )

        self.registrar(
            "Aprendizado concluído."
        )


if __name__ == "__main__":

    motor = MotorDeAprendizado()

    motor.executar()
