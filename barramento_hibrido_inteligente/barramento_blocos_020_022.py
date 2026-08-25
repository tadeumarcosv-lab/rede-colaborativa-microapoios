"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE

Módulo modular — BLOCO 020-022

BLOCO 020: estado compartilhado
BLOCO 021: sincronização de estado
BLOCO 022: comparação de estado

Somente biblioteca padrão do Python.
"""

from datetime import datetime
import copy


class BarramentoBlocos020022:

    def __init__(self, barramento):
        self.barramento = barramento

        if not hasattr(
            barramento,
            "estado_compartilhado"
        ):
            barramento.estado_compartilhado = {}

        if not hasattr(
            barramento,
            "historico_sincronizacoes"
        ):
            barramento.historico_sincronizacoes = []

    def _registrar(
        self,
        bloco,
        acao,
        dados=None
    ):
        evento = {
            "bloco": bloco,
            "acao": acao,
            "timestamp": datetime.now().isoformat(
                timespec="seconds"
            ),
            "dados": dados or {},
        }

        self.barramento.historico_sincronizacoes.append(
            evento
        )

        return evento

    # BLOCO 020

    def atualizar_estado(
        self,
        chave,
        valor
    ):
        self.barramento.estado_compartilhado[
            chave
        ] = copy.deepcopy(valor)

        return self._registrar(
            "020",
            "estado_atualizado",
            {
                "chave": chave,
            },
        )

    def obter_estado(self, chave=None):

        if chave is None:
            return copy.deepcopy(
                self.barramento.estado_compartilhado
            )

        return copy.deepcopy(
            self.barramento.estado_compartilhado.get(
                chave
            )
        )

    # BLOCO 021

    def sincronizar_estado(self, outro_estado):
        if not isinstance(
            outro_estado,
            dict
        ):
            return {
                "status": "ERRO",
                "motivo": "Estado inválido",
            }

        self.barramento.estado_compartilhado.update(
            copy.deepcopy(outro_estado)
        )

        return self._registrar(
            "021",
            "estado_sincronizado",
            {
                "quantidade": len(
                    outro_estado
                ),
            },
        )

    # BLOCO 022

    def comparar_estado(self, outro_estado):

        atual = self.barramento.estado_compartilhado

        if not isinstance(
            outro_estado,
            dict
        ):
            return {
                "igual": False,
                "diferencas": {
                    "erro": "Estado inválido"
                },
            }

        diferencas = {}

        chaves = set(
            atual
        ) | set(
            outro_estado
        )

        for chave in chaves:

            if atual.get(chave) != outro_estado.get(
                chave
            ):
                diferencas[chave] = {
                    "atual": atual.get(chave),
                    "outro": outro_estado.get(
                        chave
                    ),
                }

        resultado = {
            "igual": not bool(diferencas),
            "diferencas": diferencas,
        }

        self._registrar(
            "022",
            "estado_comparado",
            {
                "igual": resultado["igual"],
                "diferencas": len(
                    diferencas
                ),
            },
        )

        return resultado

    def executar(self):
        return {
            "blocos": "020-022",
            "chaves_estado": len(
                self.barramento.estado_compartilhado
            ),
            "sincronizacoes": len(
                self.barramento.historico_sincronizacoes
            ),
        }
