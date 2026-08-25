"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 035-037

BLOCO 035: criação de barramento
BLOCO 036: registro de barramento
BLOCO 037: remoção controlada
"""

from datetime import datetime
import uuid


class BarramentoBlocos035037:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "fabrica_registros"
        ):
            barramento.fabrica_registros = []

    def criar_barramento(
        self,
        nome,
        tipo="ESPECIALIZADO"
    ):
        identificador = str(
            uuid.uuid4()
        )

        novo = {
            "id": identificador,
            "nome": nome,
            "tipo": tipo,
            "status": "CRIADO",
            "ativo": True,
            "criado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.barramentos_temporarios[
            identificador
        ] = novo

        self.barramento.total_barramentos_criados += 1

        return self.registrar_barramento(
            novo
        )

    def registrar_barramento(
        self,
        barramento_novo
    ):
        registro = {
            "id": barramento_novo.get("id"),
            "nome": barramento_novo.get("nome"),
            "tipo": barramento_novo.get("tipo"),
            "registrado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.fabrica_registros.append(
            registro
        )

        return registro

    def remover_barramento(
        self,
        identificador
    ):
        if identificador not in (
            self.barramento.barramentos_temporarios
        ):
            return False

        del self.barramento.barramentos_temporarios[
            identificador
        ]

        return True

    def executar(self):
        return {
            "blocos": "035-037",
            "criados": (
                self.barramento.total_barramentos_criados
            ),
            "temporarios": len(
                self.barramento.barramentos_temporarios
            ),
        }
