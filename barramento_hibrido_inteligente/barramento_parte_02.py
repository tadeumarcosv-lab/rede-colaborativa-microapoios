"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE
PARTE 02 DE 04

Métodos:
- registro
- eventos
- memória
- heartbeat
- mensagens
- broadcast
- processamento de filas
"""

from datetime import datetime
import uuid
from typing import Dict, Any


class BarramentoComunicacaoMixin:

    # ============================================
    # REGISTRO
    # ============================================

    def registrar(self, mensagem: str) -> None:
        """Registra uma mensagem no histórico do Barramento."""

        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        registro = f"[BARRAMENTO] [{horario}] {mensagem}"

        self.historico_execucoes.append(registro)
        print(registro)

    def registrar_evento(
        self,
        descricao: str,
        resultado: str = "OK",
        importancia: str = "NORMAL"
    ) -> None:
        """Registra um evento no Registro Central de Eventos."""

        try:
            from registro_central_eventos import RegistroCentralEventos

            registro = RegistroCentralEventos()

            registro.registrar(
                origem="Barramento Híbrido Inteligente",
                destino="Rede",
                responsavel="Sistema",
                descricao=descricao,
                resultado=resultado,
                importancia=importancia
            )

        except Exception as erro:
            self.registrar(
                f"Erro ao registrar evento: {erro}"
            )

    def registrar_memoria(self, descricao: str) -> None:
        """Registra uma informação na Memória Persistente."""

        try:
            from gerenciador_memoria import GerenciadorMemoria

            memoria = GerenciadorMemoria()
            memoria.adicionar_historico(descricao)

        except Exception as erro:
            self.registrar(
                f"Erro ao registrar na memória: {erro}"
            )

    # ============================================
    # HEARTBEAT
    # ============================================

    def atualizar_heartbeat(self) -> None:
        """Atualiza o heartbeat dos barramentos."""

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.ultimo_heartbeat = agora
        self.heartbeats_realizados += 1

        self.barramento_principal["heartbeat"] = agora
        self.barramento_principal["ultima_verificacao"] = agora

        self.barramento_reserva["heartbeat"] = agora
        self.barramento_reserva["ultima_verificacao"] = agora

        self.barramento_emergencial["heartbeat"] = agora
        self.barramento_emergencial["ultima_verificacao"] = agora

        for barramento in self.barramentos_especializados.values():
            barramento["heartbeat"] = agora
            barramento["ultima_verificacao"] = agora

        for barramento in self.barramentos_locais.values():
            barramento["heartbeat"] = agora
            barramento["ultima_verificacao"] = agora

    def verificar_heartbeat(
        self,
        tipo: str = "PRINCIPAL"
    ) -> bool:
        """Verifica o heartbeat de um tipo de barramento."""

        if tipo == "PRINCIPAL":
            return (
                self.barramento_principal["heartbeat"]
                is not None
            )

        if tipo == "RESERVA":
            return (
                self.barramento_reserva["heartbeat"]
                is not None
            )

        if tipo == "EMERGENCIAL":
            return (
                self.barramento_emergencial["heartbeat"]
                is not None
            )

        if tipo == "ESPECIALIZADO":
            return all(
                barramento["heartbeat"] is not None
                for barramento
                in self.barramentos_especializados.values()
            )

        if tipo == "LOCAL":
            return all(
                barramento["heartbeat"] is not None
                for barramento
                in self.barramentos_locais.values()
            )

        return False

    def verificar_heartbeat_todos(self) -> Dict[str, Any]:
        """Verifica o heartbeat de todos os barramentos."""

        resultado = {
            "principal": self.verificar_heartbeat("PRINCIPAL"),
            "reserva": self.verificar_heartbeat("RESERVA"),
            "emergencial": self.verificar_heartbeat("EMERGENCIAL"),
            "especializados": self.verificar_heartbeat(
                "ESPECIALIZADO"
            ),
            "locais": self.verificar_heartbeat("LOCAL"),
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        }

        self.registrar(
            f"Verificação de heartbeat concluída: {resultado}"
        )

        return resultado

    # ============================================
    # SISTEMA DE MENSAGENS
    # ============================================

    def _gerar_id_mensagem(self) -> str:
        """Gera um identificador único para uma mensagem."""

        return str(uuid.uuid4())[:8]

    def enviar_mensagem(
        self,
        origem: str,
        destino: str,
        tipo: str,
        conteudo: Any,
        prioridade: str = "NORMAL"
    ) -> Dict[str, Any]:
        """Envia uma mensagem através do Barramento."""

        prioridades_validas = [
            "CRITICA",
            "ALTA",
            "NORMAL",
            "BAIXA"
        ]

        if prioridade not in prioridades_validas:
            prioridade = "NORMAL"

        mensagem = {
            "id": self._gerar_id_mensagem(),
            "origem": origem,
            "destino": destino,
            "tipo": tipo,
            "conteudo": conteudo,
            "prioridade": prioridade,
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "status": "ENVIADA",
            "tentativas": 0
        }

        self.mensagens.append(mensagem)
        self.mensagens_enviadas += 1

        if prioridade == "CRITICA":
            self.fila_critica.append(mensagem)

        elif prioridade == "ALTA":
            self.fila_alta.append(mensagem)

        elif prioridade == "BAIXA":
            self.fila_baixa.append(mensagem)

        else:
            self.fila_normal.append(mensagem)

        self.ultima_atividade = datetime.now()

        self.registrar(
            "Mensagem enviada: "
            f"{origem} -> {destino} "
            f"(ID: {mensagem['id']})"
        )

        self.registrar_evento(
            f"Mensagem enviada de {origem} para {destino}",
            "OK",
            "NORMAL"
        )

        return mensagem

    def receber_mensagem(
        self,
        mensagem: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Recebe e processa uma mensagem."""

        if not mensagem or not isinstance(mensagem, dict):
            self.registrar(
                "Erro: mensagem inválida para recebimento"
            )

            return {
                "status": "ERRO",
                "motivo": "Mensagem inválida"
            }

        mensagem["status"] = "RECEBIDA"

        mensagem["recebido_em"] = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.mensagens_recebidas += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            "Mensagem recebida: "
            f"{mensagem.get('origem', 'desconhecido')} -> "
            f"{mensagem.get('destino', 'desconhecido')} "
            f"(ID: {mensagem.get('id', 'sem_id')})"
        )

        return mensagem

    def broadcast(
        self,
        origem: str,
        tipo: str,
        conteudo: Any
    ) -> int:
        """Envia uma mensagem para os componentes conectados."""

        total_enviados = 0

        destinos = (
            self.modulos_conectados
            + self.agentes_conectados
            + self.motores_conectados
            + self.sistemas_conectados
        )

        if not destinos:
            self.registrar(
                "Broadcast: nenhum destino conectado"
            )
            return 0

        for destino in destinos:
            try:
                self.enviar_mensagem(
                    origem,
                    destino,
                    tipo,
                    conteudo,
                    "NORMAL"
                )

                total_enviados += 1

            except Exception as erro:
                self.registrar(
                    f"Erro no broadcast para {destino}: {erro}"
                )

        self.broadcasts_realizados += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            "Broadcast realizado: "
            f"{origem} -> {total_enviados} destinatários"
        )

        return total_enviados

    def processar_filas(self) -> int:
        """Processa as filas de mensagens por prioridade."""

        total_processadas = 0

        filas_prioridade = [
            ("CRITICA", self.fila_critica),
            ("ALTA", self.fila_alta),
            ("NORMAL", self.fila_normal),
            ("BAIXA", self.fila_baixa),
            ("MANUTENCAO", self.fila_manutencao),
            ("SINCRONIZACAO", self.fila_sincronizacao),
            ("RECUPERACAO", self.fila_recuperacao),
            ("AUDITORIA", self.fila_auditoria),
            ("APRENDIZADO", self.fila_aprendizado),
            ("EXPANSAO", self.fila_expansao)
        ]

        for nome_fila, fila in filas_prioridade:

            while fila:

                mensagem = fila.pop(0)

                try:
                    self.receber_mensagem(mensagem)
                    total_processadas += 1

                except Exception as erro:
                    self.registrar(
                        "Erro ao processar mensagem da fila "
                        f"{nome_fila}: {erro}"
                    )

                    mensagem["status"] = (
                        "ERRO_PROCESSAMENTO"
                    )

                    mensagem["erro"] = str(erro)

        self.ultima_atividade = datetime.now()

        if total_processadas > 0:
            self.registrar(
                "Filas processadas: "
                f"{total_processadas} mensagens"
            )

        return total_processadas
