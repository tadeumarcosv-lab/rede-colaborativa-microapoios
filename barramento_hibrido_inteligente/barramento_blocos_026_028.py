"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 026-028

BLOCO 026: recuperação de componente
BLOCO 027: validação pós-recuperação
BLOCO 028: encerramento de falha

Somente biblioteca padrão do Python.
"""

from datetime import datetime


class BarramentoBlocos026028:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "recuperacoes_blocos"
        ):
            barramento.recuperacoes_blocos = []

    def recuperar_componente(
        self,
        nome
    ):
        componente = self.barramento.obter_componente(
            nome
        )

        if componente is None:
            return {
                "status": "ERRO",
                "motivo": "Componente não encontrado",
                "componente": nome,
            }

        componente["status"] = "RECUPERANDO"

        registro = {
            "componente": nome,
            "status": "RECUPERACAO_INICIADA",
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        self.barramento.recuperacoes_blocos.append(
            registro
        )

        return registro

    def validar_recuperacao(
        self,
        nome
    ):
        componente = self.barramento.obter_componente(
            nome
        )

        if componente is None:
            return False

        return componente.get(
            "status"
        ) in (
            "CONECTADO",
            "REGISTRADO"
        )

    def encerrar_falha(
        self,
        falha_id
    ):
        for falha in self.barramento.registro_falhas:

            if falha.get("id") == falha_id:

                falha["status"] = "RESOLVIDA"

                falha["resolvida_em"] = (
                    datetime.now().isoformat(
                        timespec="seconds"
                    )
                )

                return True

        return False

    def executar(self):
        return {
            "blocos": "026-028",
            "recuperacoes": len(
                self.barramento.recuperacoes_blocos
            ),
        }
