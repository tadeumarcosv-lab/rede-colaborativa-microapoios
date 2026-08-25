"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 041-043

BLOCO 041: ativação da autoevolução
BLOCO 042: registro de propostas
BLOCO 043: avaliação de propostas
"""

from datetime import datetime
import uuid


class BarramentoBlocos041043:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "propostas_evolucao"
        ):
            barramento.propostas_evolucao = []

    def ativar(self):
        self.barramento.autoevolucao_ativa = True

        return {
            "status": "ATIVA",
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

    def registrar_proposta(
        self,
        descricao,
        origem="BARRAMENTO"
    ):
        proposta = {
            "id": str(uuid.uuid4()),
            "descricao": descricao,
            "origem": origem,
            "status": "PENDENTE",
            "criada_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.propostas_evolucao.append(
            proposta
        )

        return proposta

    def avaliar_proposta(
        self,
        proposta_id,
        aprovado=False
    ):
        for proposta in (
            self.barramento.propostas_evolucao
        ):

            if proposta.get("id") == proposta_id:

                proposta["status"] = (
                    "APROVADA"
                    if aprovado
                    else "REJEITADA"
                )

                proposta["avaliada_em"] = (
                    datetime.now().isoformat(
                        timespec="seconds"
                    )
                )

                return proposta

        return None

    def executar(self):
        return {
            "blocos": "041-043",
            "autoevolucao": (
                self.barramento.autoevolucao_ativa
            ),
            "propostas": len(
                self.barramento.propostas_evolucao
            ),
        }
