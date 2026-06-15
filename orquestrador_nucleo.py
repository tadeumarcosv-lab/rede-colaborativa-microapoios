from agente_comunicacao import processar_comunicacao
from agente_coordenacao import coordenar_tarefa
from agente_central import processar_solicitacao

def executar_nucleo(mensagem):

    comunicacao = processar_comunicacao(mensagem)

    coordenacao = coordenar_tarefa(comunicacao)

    resposta = processar_solicitacao(coordenacao)

    return resposta
