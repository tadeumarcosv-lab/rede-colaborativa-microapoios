"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS
Módulo modular — BLOCO 014-016
Autor: Tadeu Marcos Viana

Este módulo complementa os quatro módulos iniciais do Barramento.
Não substitui a arquitetura existente; acrescenta capacidades de forma incremental.
Somente biblioteca padrão do Python.
"""

from datetime import datetime
import uuid


class BarramentoBlocos014016:
    """BLOCOS 014-016: registro, conexão e desconexão de componentes."""

    def __init__(self, estado=None):
        self.estado = estado if estado is not None else {}

        self.estado.setdefault(
            "componentes_conectados",
            [],
        )

        self.estado.setdefault(
            "conexoes",
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

    # BLOCO 014
    def registrar_componente(
        self,
        nome,
        tipo="modulo",
        metadata=None,
    ):
        atual = next(
            (
                componente
                for componente
                in self.estado[
                    "componentes_conectados"
                ]
                if componente["nome"] == nome
            ),
            None,
        )

        if atual:
            return atual

        componente = {
            "id": str(uuid.uuid4()),
            "nome": nome,
            "tipo": tipo,
            "status": "REGISTRADO",
            "metadata": metadata or {},
            "registrado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.estado[
            "componentes_conectados"
        ].append(componente)

        self._log(
            "014",
            "componente_registrado",
            componente,
        )

        return componente

    # BLOCO 015
    def conectar(
        self,
        origem,
        destino,
        canal="PRINCIPAL",
    ):
        if not any(
            componente["nome"] == origem
            for componente
            in self.estado[
                "componentes_conectados"
            ]
        ):
            self.registrar_componente(origem)

        if not any(
            componente["nome"] == destino
            for componente
            in self.estado[
                "componentes_conectados"
            ]
        ):
            self.registrar_componente(destino)

        conexao = {
            "id": str(uuid.uuid4()),
            "origem": origem,
            "destino": destino,
            "canal": canal,
            "ativo": True,
            "criado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.estado["conexoes"].append(
            conexao
        )

        return self._log(
            "015",
            "conexao_criada",
            conexao,
        )

    # BLOCO 016
    def desconectar(self, origem, destino):
        quantidade = 0

        for conexao in self.estado["conexoes"]:
            if (
                conexao["origem"] == origem
                and conexao["destino"] == destino
                and conexao["ativo"]
            ):
                conexao["ativo"] = False
                quantidade += 1

        return self._log(
            "016",
            "desconexao",
            {
                "origem": origem,
                "destino": destino,
                "quantidade": quantidade,
            },
        )

    def executar(self):
        return {
            "blocos": "014-016",
            "componentes": len(
                self.estado[
                    "componentes_conectados"
                ]
            ),
            "conexoes": len(
                self.estado["conexoes"]
            ),
        }
