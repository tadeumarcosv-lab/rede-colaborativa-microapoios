"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS
Módulo modular — BLOCO 008-010
Autor: Tadeu Marcos Viana

Este módulo complementa os quatro módulos iniciais do Barramento.
Não substitui a arquitetura existente; acrescenta capacidades de forma incremental.
Somente biblioteca padrão do Python.
"""

from datetime import datetime
import uuid


class BarramentoBlocos008010:
    """BLOCOS 008-010: filas, classificação e despacho ordenado."""

    PRIORIDADES = (
        "CRITICA",
        "ALTA",
        "NORMAL",
        "BAIXA",
        "MANUTENCAO",
    )

    def __init__(self, estado=None):
        self.estado = estado if estado is not None else {}

        for prioridade in self.PRIORIDADES:
            self.estado.setdefault(
                "fila_" + prioridade.lower(),
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

    # BLOCO 008
    def enfileirar(self, mensagem, prioridade=None):
        prioridade = (
            prioridade
            or mensagem.get("prioridade", "NORMAL")
        ).upper()

        if prioridade not in self.PRIORIDADES:
            prioridade = "NORMAL"

        self.estado[
            "fila_" + prioridade.lower()
        ].append(mensagem)

        mensagem["status"] = "ENFILEIRADA"

        return self._log(
            "008",
            "enfileirada",
            {
                "id": mensagem.get("id"),
                "prioridade": prioridade,
            },
        )

    # BLOCO 009
    def tamanho_filas(self):
        return {
            prioridade: len(
                self.estado[
                    "fila_" + prioridade.lower()
                ]
            )
            for prioridade in self.PRIORIDADES
        }

    def proxima(self):
        for prioridade in self.PRIORIDADES:
            fila = self.estado[
                "fila_" + prioridade.lower()
            ]

            if fila:
                item = fila.pop(0)

                item["status"] = "EM_PROCESSAMENTO"

                self._log(
                    "009",
                    "retirada",
                    {
                        "id": item.get("id"),
                        "prioridade": prioridade,
                    },
                )

                return item

        return None

    # BLOCO 010
    def despachar_lote(self, limite=10):
        saida = []

        for _ in range(max(0, int(limite))):
            item = self.proxima()

            if item is None:
                break

            item["status"] = "PROCESSADA"
            saida.append(item)

        self._log(
            "010",
            "lote_processado",
            {
                "quantidade": len(saida),
            },
        )

        return saida

    def executar(self):
        return {
            "blocos": "008-010",
            "filas": self.tamanho_filas(),
        }
