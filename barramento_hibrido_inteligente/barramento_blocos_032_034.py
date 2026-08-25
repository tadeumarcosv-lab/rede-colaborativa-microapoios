"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 032-034

BLOCO 032: memória operacional
BLOCO 033: recuperação de memória
BLOCO 034: histórico operacional
"""

from datetime import datetime


class BarramentoBlocos032034:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "memoria_operacional"
        ):
            barramento.memoria_operacional = []

    def registrar_memoria(
        self,
        categoria,
        dados
    ):
        registro = {
            "categoria": categoria,
            "dados": dados,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.memoria_operacional.append(
            registro
        )

        return registro

    def consultar_memoria(
        self,
        categoria=None
    ):
        if categoria is None:
            return list(
                self.barramento.memoria_operacional
            )

        return [
            item
            for item
            in self.barramento.memoria_operacional
            if item.get("categoria") == categoria
        ]

    def obter_historico_operacional(
        self,
        limite=50
    ):
        limite = max(
            0,
            int(limite)
        )

        return self.barramento.memoria_operacional[
            -limite:
        ]

    def executar(self):
        return {
            "blocos": "032-034",
            "registros": len(
                self.barramento.memoria_operacional
            ),
        }
