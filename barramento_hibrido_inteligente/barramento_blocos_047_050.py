"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 047-050

BLOCO 047: diagnóstico estrutural
BLOCO 048: consolidação operacional
BLOCO 049: validação do conjunto
BLOCO 050: fechamento estrutural

IMPORTANTE:
Os blocos 001-050 constituem o primeiro conjunto
estrutural do Barramento Híbrido Inteligente.

Não existe BLOCO 051 neste conjunto.
"""

from datetime import datetime


class BarramentoBlocos047050:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "validacoes_estruturais"
        ):
            barramento.validacoes_estruturais = []

        if not hasattr(
            barramento,
            "conjunto_050_fechado"
        ):
            barramento.conjunto_050_fechado = False

    # ============================================
    # BLOCO 047
    # ============================================

    def diagnostico_estrutural(self):

        atributos_obrigatorios = [
            "barramento_principal",
            "barramento_reserva",
            "barramento_emergencial",
            "barramentos_especializados",
            "barramentos_locais",
            "componentes_conectados",
            "mensagens",
            "registro_componentes",
        ]

        ausentes = []

        for atributo in atributos_obrigatorios:

            if not hasattr(
                self.barramento,
                atributo
            ):
                ausentes.append(
                    atributo
                )

        resultado = {
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "status": (
                "OK"
                if not ausentes
                else "ATENCAO"
            ),
            "atributos_ausentes": ausentes,
        }

        self.barramento.validacoes_estruturais.append(
            resultado
        )

        return resultado

    # ============================================
    # BLOCO 048
    # ============================================

    def consolidar_operacao(self):

        status = (
            self.barramento.obter_status()
            if hasattr(
                self.barramento,
                "obter_status"
            )
            else {}
        )

        return {
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "status": "CONSOLIDADO",
            "barramento": status,
        }

    # ============================================
    # BLOCO 049
    # ============================================

    def validar_conjunto(self):

        diagnostico = (
            self.diagnostico_estrutural()
        )

        resultado = {
            "blocos": "001-050",
            "status": diagnostico["status"],
            "estrutura_valida": (
                diagnostico["status"] == "OK"
            ),
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        return resultado

    # ============================================
    # BLOCO 050
    # ============================================

    def fechar_conjunto(self):

        validacao = self.validar_conjunto()

        self.barramento.conjunto_050_fechado = True

        resultado = {
            "conjunto": "001-050",
            "status": "FECHADO",
            "validacao": validacao,
            "bloco_final": "050",
            "proximo_bloco": None,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        return resultado

    def executar(self):

        return {
            "blocos": "047-050",
            "conjunto": "001-050",
            "fechado": (
                self.barramento
                .conjunto_050_fechado
            ),
        }
