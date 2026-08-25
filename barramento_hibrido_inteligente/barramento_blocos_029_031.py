"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 029-031

BLOCO 029: registro de auditoria
BLOCO 030: consulta de auditoria
BLOCO 031: resumo de auditoria
"""

from datetime import datetime


class BarramentoBlocos029031:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "auditoria_barramento"
        ):
            barramento.auditoria_barramento = []

    def registrar_auditoria(
        self,
        evento,
        origem="BARRAMENTO"
    ):
        registro = {
            "evento": evento,
            "origem": origem,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.auditoria_barramento.append(
            registro
        )

        return registro

    def consultar_auditoria(
        self,
        origem=None
    ):
        registros = (
            self.barramento.auditoria_barramento
        )

        if origem is None:
            return list(registros)

        return [
            registro
            for registro in registros
            if registro.get("origem") == origem
        ]

    def resumo_auditoria(self):
        registros = (
            self.barramento.auditoria_barramento
        )

        return {
            "total": len(registros),
            "ultima": (
                registros[-1]
                if registros
                else None
            ),
        }

    def executar(self):
        return {
            "blocos": "029-031",
            "auditorias": len(
                self.barramento.auditoria_barramento
            ),
        }
