"""
CAMADA DE IA
DA REDE COLABORATIVA DE MICROAPOIOS

Responsável por:
- receber solicitações do AgenteIA;
- realizar a chamada externa;
- proteger a chamada com timeout;
- devolver resultado estruturado.

V1:
- Groq como único provedor operacional;
- requests;
- sem SDK;
- sem retry;
- sem fallback.
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

    def consultar(self, prompt, sistema=None):
        inicio = time.perf_counter()

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

        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            return self._resultado_falha(
                "GROQ_API_KEY não configurada.",
                inicio,
            )

        mensagens = []

        if sistema:
            mensagens.append(
                {
                    "role": "system",
                    "content": str(sistema),
                }
            )

        mensagens.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        payload = {
            "model": self.MODELO,
            "messages": mensagens,
        }

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
                return self._resultado_falha(
                    f"HTTP {resposta_http.status_code}",
                    inicio,
                )

            dados = resposta_http.json()

            escolhas = dados.get("choices", [])

            if not escolhas:
                return self._resultado_falha(
                    "O provedor não retornou choices.",
                    inicio,
                )

            mensagem = escolhas[0].get("message", {})
            resposta = mensagem.get("content", "")

            if not isinstance(resposta, str):
                resposta = str(resposta)

            resposta = resposta.strip()

            if not resposta:
                return self._resultado_falha(
                    "O provedor retornou resposta vazia.",
                    inicio,
                )

            modelo = dados.get(
                "model",
                self.MODELO,
            )

            return {
                "resposta": resposta,
                "provedor": self.PROVEDOR,
                "modelo": modelo,
                "status": "sucesso",
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

        except ValueError:
            return self._resultado_falha(
                "Resposta do provedor não é um JSON válido.",
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
