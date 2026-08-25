"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 023-025

BLOCO 023: registro de falhas
BLOCO 024: classificação de falhas
BLOCO 025: preparação para recuperação

Somente biblioteca padrão do Python.
"""

from datetime import datetime
import uuid


class BarramentoBlocos023025:

    TIPOS_FALHA = (
        "LEVE",
        "MODERADA",
        "GRAVE",
        "CRITICA",
    )

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "registro_falhas"
        ):
            barramento.registro_falhas = []

        if not hasattr(
            barramento,
            "falhas_classificadas"
        ):
            barramento.falhas_classificadas = []

    def registrar_falha(
        self,
        componente,
        descricao,
        tipo="MODERADA"
    ):
        tipo = str(tipo).upper()

        if tipo not in self.TIPOS_FALHA:
            tipo = "MODERADA"

        falha = {
            "id": str(uuid.uuid4()),
            "componente": componente,
            "descricao": descricao,
            "tipo": tipo,
            "status": "DETECTADA",
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.registro_falhas.append(
            falha
        )

        self.barramento.falhas_detectadas.append(
            falha
        )

        self.barramento.total_falhas_detectadas += 1

        return falha

    def classificar_falha(self, falha):

        if not isinstance(falha, dict):
            return "DESCONHECIDA"

        tipo = falha.get(
            "tipo",
            "MODERADA"
        )

        if tipo not in self.TIPOS_FALHA:
            tipo = "MODERADA"

        falha["classificacao"] = tipo

        self.barramento.falhas_classificadas.append(
            falha
        )

        return tipo

    def preparar_recuperacao(self, falha):

        if not isinstance(falha, dict):
            return {
                "status": "ERRO"
            }

        falha["status"] = "RECUPERACAO_PREPARADA"

        return {
            "status": "PREPARADA",
            "falha_id": falha.get("id"),
            "componente": falha.get(
                "componente"
            ),
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

    def executar(self):
        return {
            "blocos": "023-025",
            "falhas": len(
                self.barramento.registro_falhas
            ),
            "classificadas": len(
                self.barramento.falhas_classificadas
            ),
        }
