"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE
PARTE 03 DE 04

Métodos:
- identificação de componentes
- registro
- conexão
- desconexão
- listagem
- obtenção
- monitoramento
- status
- resumo operacional
"""

from datetime import datetime
from typing import List, Dict, Any, Optional


class BarramentoComponentesMixin:

    # ============================================
    # REGISTRO DE COMPONENTES
    # ============================================

    def _identificar_tipo_componente(
        self,
        nome: str
    ) -> str:
        """Identifica o tipo de um componente."""

        nome_lower = nome.lower()

        for tipo, lista in self.componentes_conhecidos.items():

            nomes = [
                item.lower()
                for item in lista
            ]

            if nome_lower in nomes:
                return tipo

        if "motor" in nome_lower:
            return "motores"

        if "sistema" in nome_lower:
            return "sistemas"

        if "agente" in nome_lower:
            return "agentes"

        if "integrador" in nome_lower:
            return "integradores"

        if "barramento" in nome_lower:
            return "barramentos"

        return "desconhecido"

    def registrar_componente(
        self,
        nome: str,
        referencia: Any = None,
        tipo: str = None
    ) -> Dict[str, Any]:
        """Registra um componente no Barramento."""

        if nome in self.registro_componentes:

            self.registrar(
                f"Componente {nome} já está registrado"
            )

            return self.registro_componentes[nome]

        if tipo is None:
            tipo = self._identificar_tipo_componente(nome)

        componente = {
            "id": str(__import__("uuid").uuid4()),
            "nome": nome,
            "tipo": tipo,
            "referencia": referencia,
            "status": "REGISTRADO",
            "data_registro": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "ultima_atividade": None
        }

        self.registro_componentes[nome] = componente
        self.total_componentes_registrados += 1

        if tipo == "modulos":
            self.total_modulos_registrados += 1

        elif tipo == "sistemas":
            self.total_sistemas_registrados += 1

        elif tipo == "agentes":
            self.total_agentes_registrados += 1

        elif tipo == "motores":
            self.total_motores_registrados += 1

        elif tipo == "integradores":
            self.total_integradores_registrados += 1

        elif tipo == "barramentos":
            self.total_barramentos_registrados += 1

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Componente registrado: {nome} "
            f"(tipo: {tipo})"
        )

        self.registrar_evento(
            f"Componente registrado: {nome}",
            "OK",
            "NORMAL"
        )

        return componente

    def conectar_componente(
        self,
        nome: str
    ) -> bool:
        """Conecta um componente registrado."""

        if nome not in self.registro_componentes:

            self.registrar(
                f"Componente {nome} não encontrado "
                "para conexão"
            )

            return False

        componente = self.registro_componentes[nome]

        if componente["status"] == "CONECTADO":

            self.registrar(
                f"Componente {nome} já está conectado"
            )

            return True

        componente["status"] = "CONECTADO"

        componente["ultima_atividade"] = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        if nome not in self.componentes_conectados:
            self.componentes_conectados.append(nome)

        tipo = componente["tipo"]

        if tipo == "modulos":
            if nome not in self.modulos_conectados:
                self.modulos_conectados.append(nome)

        elif tipo == "agentes":
            if nome not in self.agentes_conectados:
                self.agentes_conectados.append(nome)

        elif tipo == "motores":
            if nome not in self.motores_conectados:
                self.motores_conectados.append(nome)

        elif tipo == "sistemas":
            if nome not in self.sistemas_conectados:
                self.sistemas_conectados.append(nome)

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Componente conectado: {nome}"
        )

        return True

    def desconectar_componente(
        self,
        nome: str
    ) -> bool:
        """Desconecta um componente."""

        if nome not in self.registro_componentes:

            self.registrar(
                f"Componente {nome} não encontrado "
                "para desconexão"
            )

            return False

        componente = self.registro_componentes[nome]

        if componente["status"] != "CONECTADO":

            self.registrar(
                f"Componente {nome} não está conectado"
            )

            return True

        componente["status"] = "REGISTRADO"

        componente["ultima_atividade"] = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        listas = [
            self.componentes_conectados,
            self.modulos_conectados,
            self.agentes_conectados,
            self.motores_conectados,
            self.sistemas_conectados
        ]

        for lista in listas:
            if nome in lista:
                lista.remove(nome)

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Componente desconectado: {nome}"
        )

        return True

    def listar_componentes(
        self,
        tipo: str = None
    ) -> List[Dict[str, Any]]:
        """Lista os componentes registrados."""

        if tipo is None:
            return list(
                self.registro_componentes.values()
            )

        return [
            componente
            for componente
            in self.registro_componentes.values()
            if componente["tipo"] == tipo
        ]

    def obter_componente(
        self,
        nome: str
    ) -> Optional[Dict[str, Any]]:
        """Obtém um componente pelo nome."""

        return self.registro_componentes.get(nome)

    # ============================================
    # MONITORAMENTO
    # ============================================

    def monitorar(self) -> Dict[str, Any]:
        """Realiza o monitoramento do Barramento."""

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.ultimo_monitoramento = agora

        barramentos_ativos = 0
        barramentos_inativos = 0

        principais = [
            self.barramento_principal,
            self.barramento_reserva,
            self.barramento_emergencial
        ]

        for barramento in principais:

            if barramento["ativo"]:
                barramentos_ativos += 1
            else:
                barramentos_inativos += 1

        for barramento in (
            self.barramentos_especializados.values()
        ):

            if barramento.get("status") == "ATIVO":
                barramentos_ativos += 1
            else:
                barramentos_inativos += 1

        for barramento in self.barramentos_locais.values():

            if barramento.get("status") == "ATIVO":
                barramentos_ativos += 1
            else:
                barramentos_inativos += 1

        filas_pendentes = (
            len(self.fila_critica)
            + len(self.fila_alta)
            + len(self.fila_normal)
            + len(self.fila_baixa)
            + len(self.fila_manutencao)
            + len(self.fila_sincronizacao)
            + len(self.fila_recuperacao)
            + len(self.fila_auditoria)
            + len(self.fila_aprendizado)
            + len(self.fila_expansao)
        )

        resultado = {
            "timestamp": agora,
            "barramentos_ativos": barramentos_ativos,
            "barramentos_inativos": barramentos_inativos,
            "componentes_conectados": len(
                self.componentes_conectados
            ),
            "mensagens_enviadas": self.mensagens_enviadas,
            "mensagens_recebidas": self.mensagens_recebidas,
            "filas_pendentes": filas_pendentes
        }

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Monitoramento realizado: {resultado}"
        )

        return resultado

    # ============================================
    # STATUS
    # ============================================

    def obter_status(self) -> Dict[str, Any]:
        """Retorna o status atual do Barramento."""

        return {
            "nome": self.nome,
            "versao": self.versao,
            "status": self.status,
            "operacao_continua": self.operacao_continua,
            "ciclos": self.ciclos,
            "barramento_principal": (
                self.barramento_principal["status"]
            ),
            "barramento_reserva": (
                self.barramento_reserva["status"]
            ),
            "barramento_emergencial": (
                self.barramento_emergencial["status"]
            ),
            "componentes_registrados": (
                self.total_componentes_registrados
            ),
            "componentes_conectados": len(
                self.componentes_conectados
            ),
            "mensagens_enviadas": (
                self.mensagens_enviadas
            ),
            "mensagens_recebidas": (
                self.mensagens_recebidas
            ),
            "heartbeats_realizados": (
                self.heartbeats_realizados
            ),
            "ultima_atividade": (
                self.ultima_atividade.strftime(
                    "%d/%m/%Y %H:%M:%S"
                )
                if self.ultima_atividade
                else None
            ),
            "ultimo_heartbeat": self.ultimo_heartbeat
        }

    def obter_resumo_operacional(self) -> Dict[str, Any]:
        """Retorna o resumo operacional."""

        return {
            "status": self.status,
            "versao": self.versao,
            "ciclos": self.ciclos,
            "componentes_registrados": (
                self.total_componentes_registrados
            ),
            "componentes_conectados": len(
                self.componentes_conectados
            ),
            "mensagens_enviadas": (
                self.mensagens_enviadas
            ),
            "mensagens_recebidas": (
                self.mensagens_recebidas
            ),
            "broadcasts_realizados": (
                self.broadcasts_realizados
            ),
            "heartbeats_realizados": (
                self.heartbeats_realizados
            ),
            "sincronizacoes_realizadas": (
                self.sincronizacoes_realizadas
            ),
            "trocas_automaticas": (
                self.trocas_automaticas
            ),
            "total_falhas_detectadas": (
                self.total_falhas_detectadas
            ),
            "total_recuperacoes_realizadas": (
                self.total_recuperacoes_realizadas
            )
  }
