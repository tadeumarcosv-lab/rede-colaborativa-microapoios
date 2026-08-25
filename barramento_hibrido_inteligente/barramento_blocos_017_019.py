"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS

Módulo modular — BLOCO 017-019

Autor:
Tadeu Marcos Viana

Funções:
- BLOCO 017: roteamento de mensagens
- BLOCO 018: seleção de prioridade
- BLOCO 019: encaminhamento inteligente

Este módulo é incremental.
Não substitui as Partes 01-04.
Utiliza somente biblioteca padrão do Python.
"""

from datetime import datetime


class BarramentoBlocos017019:
    """
    Implementação dos blocos 017-019.

    O módulo trabalha sobre uma instância do Barramento
    já existente, preservando sua estrutura e suas filas.
    """

    PRIORIDADES = (
        "CRITICA",
        "ALTA",
        "NORMAL",
        "BAIXA",
        "MANUTENCAO",
    )

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            self.barramento,
            "historico_blocos"
        ):
            self.barramento.historico_blocos = []

        if not hasattr(
            self.barramento,
            "rotas_mensagens"
        ):
            self.barramento.rotas_mensagens = {}

        if not hasattr(
            self.barramento,
            "mensagens_roteadas"
        ):
            self.barramento.mensagens_roteadas = 0

    def _registrar(self, bloco, acao, dados=None):
        evento = {
            "bloco": bloco,
            "acao": acao,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "dados": dados or {},
        }

        self.barramento.historico_blocos.append(
            evento
        )

        return evento

    # ============================================
    # BLOCO 017
    # ROTEAMENTO
    # ============================================

    def registrar_rota(
        self,
        origem,
        destino,
        canal="PRINCIPAL"
    ):
        """
        Registra uma rota lógica entre origem e destino.
        """

        chave = f"{origem}->{destino}"

        self.barramento.rotas_mensagens[chave] = {
            "origem": origem,
            "destino": destino,
            "canal": canal,
            "ativo": True,
            "criado_em": datetime.now().isoformat(
                timespec="seconds"
            ),
        }

        return self._registrar(
            "017",
            "rota_registrada",
            self.barramento.rotas_mensagens[chave],
        )

    def obter_rota(self, origem, destino):
        chave = f"{origem}->{destino}"

        return self.barramento.rotas_mensagens.get(
            chave
        )

    # ============================================
    # BLOCO 018
    # PRIORIDADE
    # ============================================

    def classificar_prioridade(self, mensagem):
        """
        Determina a prioridade de uma mensagem.
        """

        prioridade = str(
            mensagem.get(
                "prioridade",
                "NORMAL"
            )
        ).upper()

        if prioridade not in self.PRIORIDADES:
            prioridade = "NORMAL"

        mensagem["prioridade"] = prioridade

        self._registrar(
            "018",
            "prioridade_classificada",
            {
                "id": mensagem.get("id"),
                "prioridade": prioridade,
            },
        )

        return prioridade

    # ============================================
    # BLOCO 019
    # ENCAMINHAMENTO
    # ============================================

    def encaminhar(self, mensagem):
        """
        Encaminha uma mensagem para sua fila correspondente.
        """

        if not isinstance(mensagem, dict):
            return {
                "status": "ERRO",
                "motivo": "Mensagem inválida",
            }

        prioridade = self.classificar_prioridade(
            mensagem
        )

        fila_nome = (
            "fila_" + prioridade.lower()
        )

        fila = getattr(
            self.barramento,
            fila_nome,
            None
        )

        if fila is None:
            return {
                "status": "ERRO",
                "motivo": (
                    f"Fila inexistente: {fila_nome}"
                ),
            }

        fila.append(mensagem)

        mensagem["status"] = "ROTEADA"

        self.barramento.mensagens_roteadas += 1

        return self._registrar(
            "019",
            "mensagem_encaminhada",
            {
                "id": mensagem.get("id"),
                "destino": mensagem.get("destino"),
                "prioridade": prioridade,
                "fila": fila_nome,
            },
        )

    def executar(self):
        return {
            "blocos": "017-019",
            "rotas": len(
                self.barramento.rotas_mensagens
            ),
            "mensagens_roteadas": (
                self.barramento.mensagens_roteadas
            ),
        }
