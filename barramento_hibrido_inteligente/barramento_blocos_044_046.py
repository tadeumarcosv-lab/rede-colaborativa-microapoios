"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 044-046

BLOCO 044: abertura de consenso
BLOCO 045: registro de decisão
BLOCO 046: encerramento de consenso
"""

from datetime import datetime
import uuid


class BarramentoBlocos044046:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "consensos"
        ):
            barramento.consensos = []

    def abrir_consenso(
        self,
        assunto,
        participantes=None
    ):
        consenso = {
            "id": str(uuid.uuid4()),
            "assunto": assunto,
            "participantes": (
                participantes or []
            ),
            "decisao": None,
            "status": "PENDENTE",
            "criado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.consensos.append(
            consenso
        )

        return consenso

    def registrar_decisao(
        self,
        consenso_id,
        decisao
    ):
        for consenso in self.barramento.consensos:

            if consenso.get("id") == consenso_id:

                consenso["decisao"] = decisao
                consenso["status"] = "DECIDIDO"

                return consenso

        return None

    def encerrar_consenso(
        self,
        consenso_id
    ):
        for consenso in self.barramento.consensos:

            if consenso.get("id") == consenso_id:

                consenso["status"] = "ENCERRADO"
                consenso["encerrado_em"] = (
                    datetime.now().isoformat(
                        timespec="seconds"
                    )
                )

                return consenso

        return None

    def executar(self):
        return {
            "blocos": "044-046",
            "consensos": len(
                self.barramento.consensos
            ),
        }
