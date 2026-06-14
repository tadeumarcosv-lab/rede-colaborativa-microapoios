from integracao_completa import IntegracaoCompleta


class ConectorTelegram:

    def __init__(self):

        self.nucleo = IntegracaoCompleta()

    def processar_mensagem(self, mensagem):

        resposta = self.nucleo.executar(
            mensagem
        )

        return resposta
