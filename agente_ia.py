"""
PRIMEIRO AGENTE DE IA
DA REDE COLABORATIVA DE MICROAPOIOS

Responsável por:
- criar e acompanhar tarefas;
- chamar a camada de IA;
- verificar o resultado;
- registrar memória;
- registrar eventos;
- produzir evidências de execução.

V1:
- um provedor operacional;
- sem retry;
- sem fallback;
- sem alteração do Kernel;
- sem alteração do Barramento.
"""

import hashlib
import os
import time
import uuid
from datetime import datetime

from camada_ia import CamadaIA
from gerenciador_memoria import GerenciadorMemoria
from registro_central_eventos import RegistroCentralEventos


class AgenteIA:

    VERSAO = "0.1.0"

    ESTADOS = (
        "CRIADA",
        "EM_EXECUCAO",
        "CONCLUIDA",
        "FALHA",
        "BLOQUEADA",
        "AGUARDANDO_INTERVENCAO",
        "CANCELADA",
    )

    ETAPAS = (
        "criando",
        "montando_contexto",
        "chamando_camada",
        "aguardando_provedor",
        "verificando_resposta",
        "registrando_memoria",
        "registrando_evento",
        "finalizando",
    )

    def __init__(self):
        self.status = "ATIVO"
        self.ambiente = os.environ.get("AMBIENTE", "dev")

        self.camada = CamadaIA()
        self.memoria = GerenciadorMemoria()
        self.eventos = RegistroCentralEventos()

    def _agora(self):
        return datetime.now().astimezone().isoformat()

    def _hash(self, texto):
        if texto is None:
            return None

        return hashlib.sha256(
            str(texto).encode("utf-8")
        ).hexdigest()

    def _criar_tarefa(self, solicitacao, objetivo):
        agora = self._agora()

        return {
            "task_id": str(uuid.uuid4()),
            "versao_agente": self.VERSAO,
            "versao_camada": self.camada.VERSAO,
            "ambiente": self.ambiente,

            "solicitacao_original": solicitacao,
            "objetivo": objetivo,

            "status": "CRIADA",
            "etapa_atual": "criando",

            "inicio": agora,
            "ultima_atividade": agora,
            "duracao_total_ms": 0,

            "resultado": {
                "resposta": "",
                "provedor": "",
                "modelo": "",
                "tempo_ms": 0,
                "tentativas": 0,
            },

            "verificacao": {
                "resposta_nao_vazia": False,
                "provedor_identificado": False,
                "chamada_provedor_sucesso": False,
            },

            "erro": None,

            "evidencia": {
                "hash_solicitacao": self._hash(solicitacao),
                "hash_resposta": None,
                "origem": "groq_api",
                "timestamp_resposta": None,
            },
        }

    def _registrar(self, tarefa):
        tarefa["etapa_atual"] = "registrando_memoria"
        tarefa["ultima_atividade"] = self._agora()

        self.memoria.adicionar_historico(tarefa)

        tarefa["etapa_atual"] = "registrando_evento"
        tarefa["ultima_atividade"] = self._agora()

        resultado_evento = (
            "SUCESSO"
            if tarefa["status"] == "CONCLUIDA"
            else "FALHA"
        )

        descricao = (
            f"Task {tarefa['task_id']} | "
            f"status={tarefa['status']} | "
            f"provedor={tarefa['resultado']['provedor']} | "
            f"hash_resposta={tarefa['evidencia']['hash_resposta']} | "
            f"hash_solicitacao={tarefa['evidencia']['hash_solicitacao']}"
        )

        if tarefa["erro"]:
            descricao += f" | erro={tarefa['erro']}"

        self.eventos.registrar(
            origem="agente_ia",
            destino="camada_ia",
            responsavel="AgenteIA",
            descricao=descricao,
            resultado=resultado_evento,
            importancia="MEDIA",
        )

    def executar(self, solicitacao, contexto=None, sistema=None):
        inicio = time.perf_counter()

        tarefa = self._criar_tarefa(
            solicitacao=solicitacao,
            objetivo="responder",
        )

        tarefa["status"] = "EM_EXECUCAO"
        tarefa["etapa_atual"] = "montando_contexto"
        tarefa["ultima_atividade"] = self._agora()

        if not isinstance(solicitacao, str):
            tarefa["status"] = "FALHA"
            tarefa["erro"] = (
                "A solicitação deve ser uma string."
            )

            tarefa["etapa_atual"] = "finalizando"
            tarefa["duracao_total_ms"] = int(
                (time.perf_counter() - inicio) * 1000
            )

            self._registrar(tarefa)
            return tarefa

        solicitacao = solicitacao.strip()

        if not solicitacao:
            tarefa["status"] = "FALHA"
            tarefa["erro"] = "A solicitação está vazia."

            tarefa["etapa_atual"] = "finalizando"
            tarefa["duracao_total_ms"] = int(
                (time.perf_counter() - inicio) * 1000
            )

            self._registrar(tarefa)
            return tarefa

        prompt = solicitacao

        if contexto:
            prompt = (
                f"Contexto disponível:\n{contexto}\n\n"
                f"Solicitação:\n{solicitacao}"
            )

        tarefa["etapa_atual"] = "chamando_camada"
        tarefa["ultima_atividade"] = self._agora()

        resultado = self.camada.consultar(
            prompt=prompt,
            sistema=sistema,
        )

        tarefa["etapa_atual"] = "verificando_resposta"
        tarefa["ultima_atividade"] = self._agora()

        resposta = resultado.get("resposta") or ""
        provedor = resultado.get("provedor") or ""
        status_provedor = resultado.get("status")

        verificacao = {
            "resposta_nao_vazia": bool(
                resposta and resposta.strip()
            ),
            "provedor_identificado": bool(provedor),
            "chamada_provedor_sucesso": (
                status_provedor == "sucesso"
            ),
        }

        tarefa["verificacao"] = verificacao

        tarefa["resultado"] = {
            "resposta": resposta,
            "provedor": provedor,
            "modelo": resultado.get("modelo", ""),
            "tempo_ms": resultado.get("tempo_ms", 0),
            "tentativas": resultado.get("tentativas", 0),
        }

        tarefa["evidencia"]["timestamp_resposta"] = (
            resultado.get("timestamp")
        )

        if resposta:
            tarefa["evidencia"]["hash_resposta"] = self._hash(
                resposta
            )

        if all(verificacao.values()):
            tarefa["status"] = "CONCLUIDA"
            tarefa["erro"] = None
        else:
            tarefa["status"] = "FALHA"
            tarefa["erro"] = (
                resultado.get("erro")
                or "A verificação mínima não foi aprovada."
            )

        tarefa["etapa_atual"] = "finalizando"
        tarefa["ultima_atividade"] = self._agora()

        tarefa["duracao_total_ms"] = int(
            (time.perf_counter() - inicio) * 1000
        )

        self._registrar(tarefa)

        return tarefa


if __name__ == "__main__":

    agente = AgenteIA()

    resultado = agente.executar(
        "Qual é a capital do Brasil?"
    )

    print()
    print("===== RESULTADO DO AGENTE IA =====")
    print(f"Task ID: {resultado['task_id']}")
    print(f"Status: {resultado['status']}")
    print(f"Resposta: {resultado['resultado']['resposta']}")
    print(f"Provedor: {resultado['resultado']['provedor']}")
    print(f"Modelo: {resultado['resultado']['modelo']}")
    print("===================================")
