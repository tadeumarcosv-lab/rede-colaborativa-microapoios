"""
AGENTE DE COMUNICACAO
Rede Colaborativa de Microapoios

Responsável pela interação com usuários,
recebimento de mensagens e entrega de respostas.
"""


class AgenteComunicacao:

    def __init__(self):

        self.nome = "Agente de Comunicacao"
        self.codigo = "AGENTE-0003"
        self.status = "ativo"

    def receber_mensagem(self, mensagem):

        return {

            "agente": self.nome,

            "acao": "mensagem_recebida",

            "conteudo": mensagem

        }

    def enviar_resposta(self, resposta):

        return {

            "agente": self.nome,

            "acao": "resposta_enviada",

            "conteudo": resposta

        }

    def status_operacional(self):

        return {

            "agente": self.nome,

            "status": self.status

        }

    def executar(self, entrada):

        mensagem = self.receber_mensagem(entrada)

        resposta = self.enviar_resposta(
            "Solicitação processada."
        )

        return {

            "agente": self.nome,

            "entrada": entrada,

            "mensagem": mensagem,

            "resposta": resposta,

            "status": self.status

        }


if __name__ == "__main__":

    comunicacao = AgenteComunicacao()

    print(

        comunicacao.executar(

            "Teste de comunicação"

        )

    )
