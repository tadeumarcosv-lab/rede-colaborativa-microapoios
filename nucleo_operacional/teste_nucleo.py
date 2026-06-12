from agente_comunicacao import AgenteComunicacao
from agente_coordenacao import AgenteCoordenacao
from agente_central import AgenteCentral

comunicacao = AgenteComunicacao()
coordenacao = AgenteCoordenacao()
central = AgenteCentral()

mensagem = comunicacao.receber_mensagem(
    "Quero participar da Rede Colaborativa de Microapoios"
)

print("COMUNICACAO:")
print(mensagem)

print()

coordenacao.adicionar_tarefa(
    "Processar solicitacao de participacao"
)

print("COORDENACAO:")
print(coordenacao.status())

print()

print("CENTRAL:")
print(
    central.receber_solicitacao(
        "Nova solicitacao recebida"
    )
)

print()

print("NUCLEO OPERACIONAL FUNCIONANDO")
