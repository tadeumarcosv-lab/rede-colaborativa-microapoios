"""
CAMADA DE IA
DA REDE COLABORATIVA DE MICROAPOIOS

Responsável por:
- receber solicitações do AgenteIA;
- realizar a chamada externa;
- proteger a chamada com timeout;
- devolver resultado estruturado;
- permitir tool calling local controlado pelo AgenteTrabalho.

V1:
- Groq como único provedor operacional;
- requests;
- sem SDK;
- sem retry;
- sem fallback.

V2:
- suporta mensagens completas de uma conversa;
- suporta definições de ferramentas;
- preserva tool_calls retornados pelo provedor;
- não executa ferramentas nesta camada.
"""

import os
import time
from datetime import datetime

import requests


class CamadaIA:

    VERSAO = "0.1.0"
    PROVEDOR = "groq"

    ENDPOINT = (
        "https://api.groq.com/openai/v1/chat/completions"
    )

    TIMEOUT = 30

    MODELO = os.environ.get(
        "GROQ_MODEL",
        "openai/gpt-oss-20b",
    )

    def __init__(self):
        self.status = "ATIVO"

    def _agora(self):
        return datetime.now().astimezone().isoformat()

    def _resultado_falha(
        self,
        erro,
        tempo_inicio,
        tentativas=1,
    ):
        return {
            "resposta": "",
            "mensagem": None,
            "tool_calls": [],
            "provedor": self.PROVEDOR,
            "modelo": self.MODELO,
            "status": "falha",
            "erro": erro,
            "tempo_ms": int(
                (time.perf_counter() - tempo_inicio) * 1000
            ),
            "timestamp": self._agora(),
            "tentativas": tentativas,
        }

    def consultar(
        self,
        prompt,
        sistema=None,
        tools=None,
        tool_choice="auto",
        mensagens=None,
    ):
        inicio = time.perf_counter()

        if mensagens is not None:
            if not isinstance(mensagens, list):
                return self._resultado_falha(
                    "As mensagens devem ser uma lista.",
                    inicio,
                )

            mensagens_api = mensagens

        else:
            if not isinstance(prompt, str):
                return self._resultado_falha(
                    "O prompt deve ser uma string.",
                    inicio,
                )

            prompt = prompt.strip()

            if not prompt:
                return self._resultado_falha(
                    "O prompt está vazio.",
                    inicio,
                )

            mensagens_api = []

            if sistema:
                mensagens_api.append(
                    {
                        "role": "system",
                        "content": str(sistema),
                    }
                )

            mensagens_api.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            return self._resultado_falha(
                "GROQ_API_KEY não configurada.",
                inicio,
            )

        payload = {
            "model": self.MODELO,
            "messages": mensagens_api,
        }

        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = tool_choice

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

        try:
            resposta_http = requests.post(
                self.ENDPOINT,
                headers=headers,
                json=payload,
                timeout=self.TIMEOUT,
            )

            if resposta_http.status_code != 200:

                try:
                    detalhes = resposta_http.json()

                    erro_api = detalhes.get(
                        "error",
                        {},
                    )

                    if isinstance(erro_api, dict):
                        mensagem_erro = erro_api.get(
                            "message"
                        )
                        tipo_erro = erro_api.get(
                            "type"
                        )
                        falha_geracao = erro_api.get(
                            "failed_generation"
                        )

                        partes = [
                            f"HTTP {resposta_http.status_code}"
                        ]

                        if mensagem_erro:
                            partes.append(
                                f"message={mensagem_erro}"
                            )

                        if tipo_erro:
                            partes.append(
                                f"type={tipo_erro}"
                            )

                        if falha_geracao:
                            partes.append(
                                "failed_generation="
                                + str(falha_geracao)[:2000]
                            )

                        erro_detalhado = "; ".join(
                            partes
                        )

                    else:
                        erro_detalhado = (
                            f"HTTP {resposta_http.status_code}; "
                            f"resposta="
                            f"{resposta_http.text[:2000]}"
                        )

                except ValueError:
                    erro_detalhado = (
                        f"HTTP {resposta_http.status_code}; "
                        f"resposta="
                        f"{resposta_http.text[:2000]}"
                    )

                return self._resultado_falha(
                    erro_detalhado,
                    inicio,
                )

            try:
                dados = resposta_http.json()
            except ValueError:
                return self._resultado_falha(
                    "Resposta do provedor não é um JSON válido.",
                    inicio,
                )

            escolhas = dados.get("choices", [])

            if not escolhas:
                return self._resultado_falha(
                    "O provedor não retornou choices.",
                    inicio,
                )

            mensagem = escolhas[0].get(
                "message",
                {},
            )

            if not isinstance(mensagem, dict):
                return self._resultado_falha(
                    "Mensagem retornada pelo provedor é inválida.",
                    inicio,
                )

            resposta = mensagem.get(
                "content",
                "",
            )

            if resposta is None:
                resposta = ""

            if not isinstance(resposta, str):
                resposta = str(resposta)

            resposta = resposta.strip()

            tool_calls = mensagem.get(
                "tool_calls",
                [],
            )

            if tool_calls is None:
                tool_calls = []

            if not isinstance(tool_calls, list):
                return self._resultado_falha(
                    "tool_calls retornado pelo provedor é inválido.",
                    inicio,
                )

            modelo = dados.get(
                "model",
                self.MODELO,
            )

            status = (
                "tool_call"
                if tool_calls
                else "sucesso"
            )

            if not tool_calls and not resposta:
                return self._resultado_falha(
                    "O provedor retornou resposta vazia.",
                    inicio,
                )

            return {
                "resposta": resposta,
                "mensagem": mensagem,
                "tool_calls": tool_calls,
                "provedor": self.PROVEDOR,
                "modelo": modelo,
                "status": status,
                "erro": None,
                "tempo_ms": int(
                    (time.perf_counter() - inicio) * 1000
                ),
                "timestamp": self._agora(),
                "tentativas": 1,
            }

        except requests.Timeout:
            return self._resultado_falha(
                "Timeout de 30 segundos excedido.",
                inicio,
            )

        except requests.RequestException as erro:
            return self._resultado_falha(
                f"Falha na comunicação com o provedor: {erro}",
                inicio,
            )

        except (KeyError, TypeError, IndexError) as erro:
            return self._resultado_falha(
                f"Estrutura inesperada da resposta: {erro}",
                inicio,
            )


if __name__ == "__main__":

    camada = CamadaIA()

    resultado = camada.consultar(
        "Qual é a capital do Brasil?"
    )

    print()
    print("===== TESTE DA CAMADA IA =====")
    print(resultado)
    print("===============================")
