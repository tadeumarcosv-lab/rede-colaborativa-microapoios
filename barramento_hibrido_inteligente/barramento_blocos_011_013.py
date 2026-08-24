"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS
Módulo modular — BLOCO 011-013
Autor: Tadeu Marcos Viana

Este módulo complementa os quatro módulos iniciais do Barramento.
Não substitui a arquitetura existente; acrescenta capacidades de forma incremental.
Somente biblioteca padrão do Python.
"""

from datetime import datetime
import uuid


class BarramentoBlocos011013:
    """BLOCOS 011-013: heartbeat, monitoramento e diagnóstico."""

    def __init__(self, estado=None):
        self.estado = estado if estado is not None else {}

        self.estado.setdefault(
            "heartbeats",
            {},
        )

        self.estado.setdefault(
            "diagnosticos",
            [],
        )

        self.estado.setdefault(
            "falhas_detectadas",
            [],
        )

        self.estado.setdefault(
            "historico_blocos",
            [],
        )

    def _log(self, bloco, acao, dados=None):
        evento = {
            "id": str(uuid.uuid4())[:8],
            "bloco": bloco,
            "acao": acao,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "dados": dados or {},
        }

        self.estado["historico_blocos"].append(
            evento
        )

        return evento

    # BLOCO 011
    def atualizar_heartbeat(
        self,
        nome="Barramento Híbrido Inteligente da Rede",
    ):
        timestamp = datetime.now().isoformat(
            timespec="seconds"
        )

        self.estado["heartbeats"][nome] = timestamp

        return self._log(
            "011",
            "heartbeat",
            {
                "nome": nome,
                "timestamp": timestamp,
            },
        )

    def verificar_heartbeat(self, nome):
        return nome in self.estado["heartbeats"]

    def verificar_todos(self):
        return {
            nome: bool(timestamp)
            for nome, timestamp
            in self.estado["heartbeats"].items()
        }

    # BLOCO 012
    def monitorar(self, componentes):
        resultado = {}

        for nome in componentes:
            resultado[nome] = (
                "ATIVO"
                if self.verificar_heartbeat(nome)
                else "SEM_HEARTBEAT"
            )

        self.estado["ultimo_monitoramento"] = {
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "resultado": resultado,
        }

        return self._log(
            "012",
            "monitoramento",
            resultado,
        )

    # BLOCO 013
    def diagnosticar(self):
        diagnostico = {
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "heartbeats": self.verificar_todos(),
            "falhas": list(
                self.estado["falhas_detectadas"]
            ),
        }

        self.estado["diagnosticos"].append(
            diagnostico
        )

        return self._log(
            "013",
            "diagnostico",
            diagnostico,
        )

    def executar(self):
        return {
            "blocos": "011-013",
            "heartbeats": self.verificar_todos(),
            "falhas": len(
                self.estado["falhas_detectadas"]
            ),
        }
