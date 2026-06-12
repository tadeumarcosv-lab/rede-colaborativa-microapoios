from agente_comunicacao import AgenteComunicacao
from agente_coordenacao import AgenteCoordenacao
from agente_central import AgenteCentral


class NucleoOperacional:

    def __init__(self):
        self.comunicacao = AgenteComunicacao()
        self.coordenacao = AgenteCoordenacao()
        self.central = AgenteCentral()

    def processar(self, mensagem_usuario):

        recebimento = self.comunicacao.receber_mensagem(
            mensagem_usuario
        )

        self.coordenacao.adicionar_tarefa(
            mensagem_usuario
        )

        resposta_central = self.central.receber_solicitacao(
            mensagem_usuario
        )

        resposta_final = self.comunicacao.enviar_resposta(
            str(resposta_central)
        )

        return {
            "recebimento": recebimento,
            "coordenacao": self.coordenacao.status(),
            "central": resposta_central,
            "resposta": resposta_final
        }


if __name__ == "__main__":

    sistema = NucleoOperacional()

    resultado = sistema.processar(
        "Quero participar da Rede Colaborativa de Microapoios"
    )

    print(resultado)
