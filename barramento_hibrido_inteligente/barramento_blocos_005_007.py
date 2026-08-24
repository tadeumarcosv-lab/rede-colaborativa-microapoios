"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS
Módulo modular — BLOCO 005-007
Autor: Tadeu Marcos Viana

Este módulo complementa os quatro módulos iniciais do Barramento.
Não substitui a arquitetura existente; acrescenta capacidades de forma incremental.
Somente biblioteca padrão do Python.
"""

from datetime import datetime
import uuid


class BarramentoBlocos005007:
    """BLOCOS 005-007: mensagens, roteamento básico e prioridades."""

    def __init__(self, estado=None):
        self.estado = estado if estado is not None else {}
        self.estado.setdefault("mensagens", [])
        self.estado.setdefault("mensagens_enviadas", 0)
        self.estado.setdefault("mensagens_recebidas", 0)
        self.estado.setdefault("rotas", {})
        self.estado.setdefault("historico_blocos", [])

    def _evento(self, bloco, acao, dados=None):
        evento = {
            "id": str(uuid.uuid4())[:8],
            "bloco": bloco,
            "acao": acao,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "dados": dados or {},
        }
        self.estado["historico_blocos"].append(evento)
        return evento

    # BLOCO 005 — protocolo de mensagem
    def criar_mensagem(
        self,
        origem,
        destino,
        tipo,
        conteudo,
        prioridade="NORMAL",
    ):
        prioridade = str(prioridade).upper()

        if prioridade not in {
            "CRITICA",
            "ALTA",
            "NORMAL",
            "BAIXA",
            "MANUTENCAO",
        }:
            prioridade = "NORMAL"

        mensagem = {
            "id": str(uuid.uuid4()),
            "origem": origem,
            "destino": destino,
            "tipo": tipo,
            "conteudo": conteudo,
            "prioridade": prioridade,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "status": "PENDENTE",
        }

        self.estado["mensagens"].append(mensagem)
        self.estado["mensagens_enviadas"] += 1

        self._evento(
            "005",
            "mensagem_criada",
            mensagem,
        )

        return mensagem

    # BLOCO 006 — roteamento
    def registrar_rota(
        self,
        origem,
        destino,
        canal="PRINCIPAL",
        prioridade=1,
    ):
        self.estado["rotas"].setdefault(origem, [])

        rota = {
            "destino": destino,
            "canal": canal,
            "prioridade": int(prioridade),
            "ativo": True,
        }

        self.estado["rotas"][origem] = [
            r
            for r in self.estado["rotas"][origem]
            if r["destino"] != destino
        ]

        self.estado["rotas"][origem].append(rota)

        self.estado["rotas"][origem].sort(
            key=lambda item: item["prioridade"]
        )

        return self._evento(
            "006",
            "rota_registrada",
            rota,
        )

    def selecionar_rota(self, origem, destino):
        for rota in self.estado["rotas"].get(origem, []):
            if (
                rota["destino"] == destino
                and rota["ativo"]
            ):
                return rota

        return None

    # BLOCO 007 — despacho e confirmação
    def despachar(self, mensagem):
        if isinstance(mensagem, str):
            encontrados = [
                item
                for item in self.estado["mensagens"]
                if item["id"] == mensagem
            ]

            mensagem = (
                encontrados[0]
                if encontrados
                else None
            )

        if not mensagem:
            return {
                "status": "ERRO",
                "motivo": "mensagem_nao_encontrada",
            }

        rota = self.selecionar_rota(
            mensagem["origem"],
            mensagem["destino"],
        )

        mensagem["rota"] = (
            rota
            or {
                "canal": "PRINCIPAL",
                "prioridade": 1,
            }
        )

        mensagem["status"] = "DESPACHADA"
        self.estado["mensagens_recebidas"] += 1

        return self._evento(
            "007",
            "mensagem_despachada",
            {
                "id": mensagem["id"],
                "rota": mensagem["rota"],
            },
        )

    def executar(self):
        return {
            "blocos": "005-007",
            "mensagens": len(
                self.estado["mensagens"]
            ),
            "rotas": sum(
                map(
                    len,
                    self.estado["rotas"].values(),
                )
            ),
        }
