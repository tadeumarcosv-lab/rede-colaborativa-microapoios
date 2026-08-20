"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE COLABORATIVA DE MICROAPOIOS

Autor:
Tadeu Marcos Viana

Implementação executável baseada no documento:
BARRAMENTO_HIBRIDO_INTELIGENTE_DA_REDE.md

Versão: 1.2 - Fundação Permanente + Operação + Redundância +
Descoberta + Registro + Comunicação

Responsabilidades:
- Gerenciar todos os tipos de barramentos da Rede
- Registrar e conectar componentes, módulos, agentes, motores e sistemas
- Fornecer comunicação padronizada entre componentes
- Manter operação contínua
- Manter redundância operacional
- Realizar descoberta automática de componentes
- Monitorar integridade
- Processar filas
- Registrar eventos e memória quando disponíveis
- Servir como fundação para futuras expansões
- Preservar compatibilidade com a arquitetura existente

Princípio estrutural:
Este módulo constitui a fundação executável do Barramento.
Novas capacidades devem ser acrescentadas incrementalmente,
sem quebrar os mecanismos existentes.
"""

from datetime import datetime
import time
from typing import List, Dict, Any, Optional
import uuid
import importlib
import inspect


class BarramentoHibridoInteligenteDaRede:
    """
    Classe principal do Barramento Híbrido Inteligente da Rede.

    Arquitetura:

    1. Barramento Inteligente Principal
    2. Barramento Reserva
    3. Barramento Emergencial
    4. Barramentos Especializados
    5. Barramentos Locais
    6. Barramentos Temporários
    7. Registro de componentes
    8. Comunicação
    9. Filas
    10. Heartbeat
    11. Monitoramento
    12. Sincronização
    13. Redundância
    14. Descoberta automática
    15. Integridade
    16. Operação contínua

    Esta classe foi estruturada para permitir expansão futura
    sem necessidade de reconstrução do núcleo já existente.
    """

    def __init__(self):
        """Inicializa o Barramento Híbrido Inteligente."""

        # ==========================================================
        # 1. IDENTIDADE E STATUS
        # ==========================================================

        self.status = "ATIVO"
        self.nome = "Barramento Híbrido Inteligente da Rede"
        self.versao = "1.2"
        self.tipo = "Híbrido Inteligente"

        # ==========================================================
        # 2. CONTROLE OPERACIONAL
        # ==========================================================

        self.operacao_continua = False
        self.ciclos = 0
        self.inicio = None
        self.fim = None
        self.tempo_total = None
        self.ultima_execucao = None
        self.ultima_atividade = None

        # ==========================================================
        # 3. BARRAMENTO INTELIGENTE PRINCIPAL
        # ==========================================================

        self.barramento_principal = {
            "nome": "Barramento Inteligente Principal",
            "tipo": "PRINCIPAL",
            "status": "ATIVO",
            "ativo": True,
            "prioridade": 1,
            "heartbeat": None,
            "ultima_verificacao": None,
            "ultima_sincronizacao": None,
            "funcoes": [
                "Comunicação central",
                "Registro de componentes",
                "Descoberta automática",
                "Roteamento inteligente",
                "Coordenação operacional"
            ]
        }

        # ==========================================================
        # 4. BARRAMENTO RESERVA
        # ==========================================================

        self.barramento_reserva = {
            "nome": "Barramento Reserva",
            "tipo": "RESERVA",
            "status": "EM ESPERA",
            "ativo": True,
            "prioridade": 2,
            "heartbeat": None,
            "ultima_verificacao": None,
            "ultima_sincronizacao": None,
            "funcoes": [
                "Redundância do principal",
                "Assumir em caso de falha",
                "Sincronização contínua"
            ]
        }

        # ==========================================================
        # 5. BARRAMENTO EMERGENCIAL
        # ==========================================================

        self.barramento_emergencial = {
            "nome": "Barramento Emergencial",
            "tipo": "EMERGENCIAL",
            "status": "PRONTO",
            "ativo": True,
            "prioridade": 3,
            "heartbeat": None,
            "ultima_verificacao": None,
            "ultima_sincronizacao": None,
            "funcoes": [
                "Último recurso",
                "Operação mínima",
                "Recuperação de falhas críticas"
            ]
        }

        # ==========================================================
        # 6. BARRAMENTOS ESPECIALIZADOS
        # ==========================================================

        self.barramentos_especializados = {

            "memoria": {
                "nome": "Barramento de Memória",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Centraliza memória persistente",
                "integracao": "GerenciadorMemoria"
            },

            "eventos": {
                "nome": "Barramento de Eventos",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Centraliza eventos da Rede",
                "integracao": "RegistroCentralEventos"
            },

            "auditoria": {
                "nome": "Barramento de Auditoria",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Auditoria contínua",
                "integracao": "SistemaDeAuditoria"
            },

            "aprendizado": {
                "nome": "Barramento de Aprendizado",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Centraliza aprendizado contínuo",
                "integracao": "MotorDeAprendizado"
            },

            "recuperacao": {
                "nome": "Barramento de Recuperação",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Recuperação de falhas",
                "integracao": "SistemaDeRecuperacao"
            },

            "expansao": {
                "nome": "Barramento de Expansão",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Adição de novos módulos",
                "integracao": "GeradorAutonomoDeComponentes"
            },

            "diagnostico": {
                "nome": "Barramento de Diagnóstico",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Diagnóstico de falhas",
                "integracao": "SistemaDeMonitoramento"
            },

            "sincronizacao": {
                "nome": "Barramento de Sincronização",
                "tipo": "ESPECIALIZADO",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "funcao": "Sincronização entre módulos",
                "integracao": "OrquestradorCentral"
            }
        }

        # ==========================================================
        # 7. BARRAMENTOS LOCAIS
        # ==========================================================

        self.barramentos_locais = {

            "kernel": {
                "nome": "Barramento Local - Kernel",
                "tipo": "LOCAL",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "responsavel": "KernelDaRede"
            },

            "supervisor": {
                "nome": "Barramento Local - Supervisor",
                "tipo": "LOCAL",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "responsavel": "SupervisorGeral"
            },

            "orquestrador": {
                "nome": "Barramento Local - Orquestrador",
                "tipo": "LOCAL",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "responsavel": "OrquestradorCentralDaRede"
            },

            "diretor": {
                "nome": "Barramento Local - Diretor",
                "tipo": "LOCAL",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "responsavel": "DiretorAutonomoDaRede"
            },

            "planejador": {
                "nome": "Barramento Local - Planejador",
                "tipo": "LOCAL",
                "status": "ATIVO",
                "heartbeat": None,
                "ultima_verificacao": None,
                "ultima_sincronizacao": None,
                "responsavel": "PlanejadorMestreDeExpansaoDaRede"
            }
        }

        # ==========================================================
        # 8. BARRAMENTOS TEMPORÁRIOS
        # ==========================================================

        self.barramentos_temporarios = {}
        self.proximo_id_temporario = 1

        # ==========================================================
        # 9. COMPONENTES CONECTADOS
        # ==========================================================

        self.componentes_conectados = []
        self.modulos_conectados = []
        self.agentes_conectados = []
        self.motores_conectados = []
        self.sistemas_conectados = []
        self.integradores_conectados = []
        self.barramentos_conectados = []

        # ==========================================================
        # 10. ESTATÍSTICAS E HISTÓRICO
        # ==========================================================

        self.historico_execucoes = []
        self.resumo_operacional = {}

        self.total_componentes_registrados = 0
        self.total_barramentos_criados = 0
        self.total_falhas_detectadas = 0
        self.total_recuperacoes_realizadas = 0

        # ==========================================================
        # 11. SISTEMA DE MENSAGENS
        # ==========================================================

        self.mensagens = []

        self.mensagens_enviadas = 0
        self.mensagens_recebidas = 0
        self.broadcasts_realizados = 0
        self.trocas_automaticas = 0
        self.heartbeats_realizados = 0
        self.sincronizacoes_realizadas = 0

        # ==========================================================
        # 12. FILAS INTELIGENTES
        # ==========================================================

        self.fila_critica = []
        self.fila_alta = []
        self.fila_normal = []
        self.fila_baixa = []

        self.fila_manutencao = []
        self.fila_sincronizacao = []
        self.fila_recuperacao = []
        self.fila_auditoria = []
        self.fila_aprendizado = []
        self.fila_expansao = []

        # ==========================================================
        # 13. MONITORAMENTO
        # ==========================================================

        self.monitoramento_intervalo = 10
        self.ultimo_monitoramento = None

        self.falhas_detectadas = []
        self.barramentos_falhos = []

        # ==========================================================
        # 14. HEARTBEAT
        # ==========================================================

        self.heartbeat_intervalo = 5
        self.ultimo_heartbeat = None

        # Compatibilidade com nomenclatura anterior
        self.heartbeat_ultimo = None

        # ==========================================================
        # 15. DESCOBERTA AUTOMÁTICA
        # ==========================================================

        self.descoberta_automatica_ativa = False
        self.ultima_descoberta = None

        self.total_descobertas_realizadas = 0
        self.total_componentes_descobertos = 0

        self.componentes_descobertos = []
        self.componentes_ignorados = []

        # ==========================================================
        # 16. COMPONENTES CONHECIDOS
        # ==========================================================

        self.componentes_conhecidos = {

            "modulos": [
                "kernel",
                "gerenciador_inicializacao",
                "supervisor_geral",
                "orquestrador_central_da_rede",
                "diretor_autonomo_da_rede",
                "planejador_mestre_de_expansao_da_rede",
                "gerador_autonomo_de_componentes_da_rede",
                "motor_de_planejamento",
                "motor_de_construcao",
                "motor_de_verificacao",
                "motor_de_aprendizado"
            ],

            "sistemas": [
                "sistema_executor_da_rede",
                "sistema_de_monitoramento_da_rede",
                "sistema_de_recuperacao_da_rede",
                "sistema_de_evolucao_autonoma",
                "sistema_de_memoria_persistente",
                "sistema_de_auditoria_da_rede"
            ],

            "integradores": [
                "integrador_dos_motores",
                "integrador_dos_sistemas",
                "integrador_operacional_principal",
                "integrador_da_memoria",
                "integrador_da_rede",
                "integrador_de_autoconstrucao",
                "integrador_de_autocorrecao",
                "integrador_de_comunicacao",
                "integrador_de_decisoes",
                "integrador_do_aprendizado",
                "integrador_dos_agentes"
            ],

            "agentes": [
                "agente_central",
                "agente_coordenacao",
                "agente_comunicacao",
                "agente_pesquisa_avancada",
                "agente_memoria_estrategica",
                "agente_gestao_conhecimento",
                "agente_observador",
                "agente_auditor",
                "agente_arquiteto",
                "agente_construtor",
                "agente_reparador"
            ],

            "barramentos": [
                "barramento_hibrido_inteligente_da_rede"
            ]
        }

        # ==========================================================
        # 17. COMPONENTES DESCOBERTOS POR TIPO
        # ==========================================================

        self.modulos_descobertos = []
        self.sistemas_descobertos = []
        self.integradores_descobertos = []
        self.agentes_descobertos = []
        self.barramentos_descobertos = []

        # ==========================================================
        # 18. PONTOS DE EXPANSÃO FUTURA
        # ==========================================================

        self.fabrica_barramentos_ativa = False

        self.arquitetura_fractal_ativa = False
        self.dna_estrutural = None

        self.autoevolucao_ativa = False
        self.sistema_autoevolucao = None

        self.balanceamento_carga_ativa = False

        self.roteamento_inteligente_ativa = False

        self.filas_inteligentes_ativa = False
        self.filas = {}

        self.eleicao_automatica_ativa = False
        self.coordenador_atual = None

        self.recuperacao_automatica_ativa = False

        # ==========================================================
        # 19. SISTEMA DE AUTOEVOLUÇÃO DO BARRAMENTO
        # ==========================================================

        self.sab_ativa = False
        self.sab_ciclos = 0
        self.sab_ultima_analise = None
        self.sab_melhores_ideias = []

        # ==========================================================
        # 20. SISTEMA DE SUGESTÕES
        # ==========================================================

        self.sistema_sugestoes_ativa = False
        self.sugestoes = []

        # ==========================================================
        # 21. SISTEMA DE CONSENSO
        # ==========================================================

        self.sistema_consenso_ativa = False
        self.consenso_pendente = []

        # ==========================================================
        # 22. REGISTRO DE COMPONENTES
        # ==========================================================

        self.registro_componentes = {}

        self.total_modulos_registrados = 0
        self.total_sistemas_registrados = 0
        self.total_agentes_registrados = 0
        self.total_motores_registrados = 0
        self.total_integradores_registrados = 0
        self.total_barramentos_registrados = 0

    # ============================================================
    # MÉTODOS DE REGISTRO
    # ============================================================

    def registrar(self, mensagem: str) -> None:
        """
        Registra uma mensagem no histórico operacional.
        """

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
        """
        Tenta registrar evento no Registro Central de Eventos.

        A integração é opcional nesta fase.
        Caso o módulo ainda não esteja disponível, o Barramento
        continua funcionando.
        """

        try:
            from registro_central_eventos import RegistroCentralEventos

            registro = RegistroCentralEventos()

            if hasattr(registro, "registrar"):
                registro.registrar(
                    origem="Barramento Híbrido Inteligente",
                    destino="Rede",
                    responsavel="Sistema",
                    descricao=descricao,
                    resultado=resultado,
                    importancia=importancia
                )

        except Exception as e:
            self.registrar(
                f"Registro Central de Eventos indisponível: {e}"
            )

    def registrar_memoria(self, descricao: str) -> None:
        """
        Tenta registrar informação na memória persistente.
        """

        try:
            from gerenciador_memoria import GerenciadorMemoria

            memoria = GerenciadorMemoria()

            if hasattr(memoria, "adicionar_historico"):
                memoria.adicionar_historico(descricao)

        except Exception as e:
            self.registrar(
                f"Gerenciador de Memória indisponível: {e}"
            )

    # ============================================================
    # HEARTBEAT
    # ============================================================

    def atualizar_heartbeat(self) -> None:
        """
        Atualiza o heartbeat de todos os barramentos conhecidos.
        """

        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        self.ultimo_heartbeat = agora
        self.heartbeat_ultimo = agora

        self.heartbeats_realizados += 1

        # Principal
        self.barramento_principal["heartbeat"] = agora
        self.barramento_principal["ultima_verificacao"] = agora

        # Reserva
        self.barramento_reserva["heartbeat"] = agora
        self.barramento_reserva["ultima_verificacao"] = agora

        # Emergencial
        self.barramento_emergencial["heartbeat"] = agora
        self.barramento_emergencial["ultima_verificacao"] = agora

        # Especializados
        for barramento in self.barramentos_especializados.values():
            barramento["heartbeat"] = agora
            barramento["ultima_verificacao"] = agora

        # Locais
        for barramento in self.barramentos_locais.values():
            barramento["heartbeat"] = agora
            barramento["ultima_verificacao"] = agora

        # Temporários
        for barramento in self.barramentos_temporarios.values():
            barramento["heartbeat"] = agora
            barramento["ultima_verificacao"] = agora

        self.ultima_atividade = datetime.now()

    def verificar_heartbeat(self, tipo: str = "PRINCIPAL") -> bool:
        """
        Verifica heartbeat de um grupo de barramentos.
        """

        tipo = tipo.upper()

        if tipo == "PRINCIPAL":
            return self.barramento_principal["heartbeat"] is not None

        if tipo == "RESERVA":
            return self.barramento_reserva["heartbeat"] is not None

        if tipo == "EMERGENCIAL":
            return self.barramento_emergencial["heartbeat"] is not None

        if tipo == "ESPECIALIZADO":
            return all(
                b["heartbeat"] is not None
                for b in self.barramentos_especializados.values()
            )

        if tipo == "LOCAL":
            return all(
                b["heartbeat"] is not None
                for b in self.barramentos_locais.values()
            )

        if tipo == "TEMPORARIO":
            return all(
                b["heartbeat"] is not None
                for b in self.barramentos_temporarios.values()
            )

        return False

    def verificar_heartbeat_todos(self) -> Dict[str, Any]:
        """
        Verifica heartbeat de todos os grupos.
        """

        resultado = {
            "principal": self.verificar_heartbeat("PRINCIPAL"),
            "reserva": self.verificar_heartbeat("RESERVA"),
            "emergencial": self.verificar_heartbeat("EMERGENCIAL"),
            "especializados": self.verificar_heartbeat("ESPECIALIZADO"),
            "locais": self.verificar_heartbeat("LOCAL"),
            "temporarios": self.verificar_heartbeat("TEMPORARIO"),
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        }

        self.registrar(
            f"Verificação de heartbeat concluída: {resultado}"
        )

        return resultado

    # ============================================================
    # SISTEMA DE MENSAGENS
    # ============================================================

    def _gerar_id_mensagem(self) -> str:
        """Gera identificador único de mensagem."""

        return str(uuid.uuid4())[:8]

    def enviar_mensagem(
        self,
        origem: str,
        destino: str,
        tipo: str,
        conteudo: Any,
        prioridade: str = "NORMAL"
    ) -> Dict[str, Any]:
        """
        Envia uma mensagem através do Barramento.
        """

        prioridades_validas = [
            "CRITICA",
            "ALTA",
            "NORMAL",
            "BAIXA"
        ]

        prioridade = prioridade.upper()

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
            f"Mensagem enviada: {origem} -> {destino} "
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
        """
        Recebe e processa uma mensagem.
        """

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
        """
        Envia mensagem para todos os componentes conectados.
        """

        total_enviados = 0

        destinos = []

        destinos.extend(self.modulos_conectados)
        destinos.extend(self.agentes_conectados)
        destinos.extend(self.motores_conectados)
        destinos.extend(self.sistemas_conectados)
        destinos.extend(self.integradores_conectados)
        destinos.extend(self.barramentos_conectados)

        # Remove duplicidades preservando a ordem.
        destinos = list(dict.fromkeys(destinos))

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

            except Exception as e:

                self.registrar(
                    f"Erro no broadcast para {destino}: {e}"
                )

        self.broadcasts_realizados += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Broadcast realizado: {origem} -> "
            f"{total_enviados} destinatários"
        )

        return total_enviados

    def processar_filas(self) -> int:
        """
        Processa as filas de mensagens por prioridade.
        """

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

                except Exception as e:

                    self.registrar(
                        f"Erro ao processar mensagem da fila "
                        f"{nome_fila}: {e}"
                    )

                    mensagem["status"] = "ERRO_PROCESSAMENTO"
                    mensagem["erro"] = str(e)

        self.ultima_atividade = datetime.now()

        if total_processadas > 0:
            self.registrar(
                f"Filas processadas: "
                f"{total_processadas} mensagens"
            )

        return total_processadas

    # ============================================================
    # IDENTIFICAÇÃO DE COMPONENTES
    # ============================================================

    def _identificar_tipo_componente(self, nome: str) -> str:
        """
        Identifica o tipo do componente pelo nome.
        """

        nome_lower = nome.lower()

        for tipo, lista in self.componentes_conhecidos.items():

            for item in lista:

                if nome_lower == item.lower():
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

    # ============================================================
    # REGISTRO DE COMPONENTES
    # ============================================================

    def registrar_componente(
        self,
        nome: str,
        referencia: Any = None,
        tipo: str = None
    ) -> Dict[str, Any]:
        """
        Registra componente no Barramento.
        """

        if not nome:
            raise ValueError(
                "O nome do componente não pode ser vazio."
            )

        if nome in self.registro_componentes:

            componente_existente = self.registro_componentes[nome]

            # Atualiza referência se uma nova referência foi fornecida.
            if referencia is not None:
                componente_existente["referencia"] = referencia

            self.registrar(
                f"Componente {nome} já está registrado"
            )

            return componente_existente

        if tipo is None:
            tipo = self._identificar_tipo_componente(nome)

        componente = {
            "id": str(uuid.uuid4()),
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

    def conectar_componente(self, nome: str) -> bool:
        """
        Conecta componente registrado ao Barramento.
        """

        if nome not in self.registro_componentes:

            self.registrar(
                f"Componente {nome} não encontrado para conexão"
            )

            return False

        componente = self.registro_componentes[nome]

        if componente["status"] == "CONECTADO":

            self.registrar(
                f"Componente {nome} já está conectado"
            )

            return True

        componente["status"] = "CONECTADO"

        componente["ultima_atividade"] = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self._adicionar_componente_lista(
            self.componentes_conectados,
            nome
        )

        tipo = componente["tipo"]

        if tipo == "modulos":
            self._adicionar_componente_lista(
                self.modulos_conectados,
                nome
            )

        elif tipo == "agentes":
            self._adicionar_componente_lista(
                self.agentes_conectados,
                nome
            )

        elif tipo == "motores":
            self._adicionar_componente_lista(
                self.motores_conectados,
                nome
            )

        elif tipo == "sistemas":
            self._adicionar_componente_lista(
                self.sistemas_conectados,
                nome
            )

        elif tipo == "integradores":
            self._adicionar_componente_lista(
                self.integradores_conectados,
                nome
            )

        elif tipo == "barramentos":
            self._adicionar_componente_lista(
                self.barramentos_conectados,
                nome
            )

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Componente conectado: {nome}"
        )

        return True

    @staticmethod
    def _adicionar_componente_lista(
        lista: List[str],
        nome: str
    ) -> None:
        """
        Adiciona nome à lista sem duplicação.
        """

        if nome not in lista:
            lista.append(nome)

    def desconectar_componente(self, nome: str) -> bool:
        """
        Desconecta componente do Barramento.
        """

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

        componente["ultima_atividade"] = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        listas = [
            self.componentes_conectados,
            self.modulos_conectados,
            self.agentes_conectados,
            self.motores_conectados,
            self.sistemas_conectados,
            self.integradores_conectados,
            self.barramentos_conectados
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
        """
        Lista componentes registrados.
        """

        if tipo is None:
            return list(
                self.registro_componentes.values()
            )

        return [
            componente
            for componente in self.registro_componentes.values()
            if componente["tipo"] == tipo
        ]

    def obter_componente(
        self,
        nome: str
    ) -> Optional[Dict[str, Any]]:
        """
        Obtém componente pelo nome.
        """

        return self.registro_componentes.get(nome)

    # ============================================================
    # MONITORAMENTO
    # ============================================================

    def monitorar(self) -> Dict[str, Any]:
        """
        Realiza monitoramento geral do Barramento.
        """

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.ultimo_monitoramento = agora

        barramentos_ativos = 0
        barramentos_inativos = 0

        grupos = [
            self.barramento_principal,
            self.barramento_reserva,
            self.barramento_emergencial
        ]

        grupos.extend(
            self.barramentos_especializados.values()
        )

        grupos.extend(
            self.barramentos_locais.values()
        )

        grupos.extend(
            self.barramentos_temporarios.values()
        )

        for barramento in grupos:

            if barramento.get("ativo", False):

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
            "componentes_registrados": (
                self.total_componentes_registrados
            ),
            "componentes_conectados": (
                len(self.componentes_conectados)
            ),
            "mensagens_enviadas": self.mensagens_enviadas,
            "mensagens_recebidas": self.mensagens_recebidas,
            "filas_pendentes": filas_pendentes,
            "falhas_detectadas": self.total_falhas_detectadas,
            "recuperacoes_realizadas": (
                self.total_recuperacoes_realizadas
            )
        }

        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Monitoramento realizado: {resultado}"
        )

        return resultado

    def obter_status(self) -> Dict[str, Any]:
        """
        Retorna status atual do Barramento.
        """

        return {
            "nome": self.nome,
            "versao": self.versao,
            "status": self.status,
            "operacao_continua": self.operacao_continua,
            "ciclos": self.ciclos,

            "barramento_principal":
                self.barramento_principal["status"],

            "barramento_reserva":
                self.barramento_reserva["status"],

            "barramento_emergencial":
                self.barramento_emergencial["status"],

            "componentes_registrados":
                self.total_componentes_registrados,

            "componentes_conectados":
                len(self.componentes_conectados),

            "mensagens_enviadas":
                self.mensagens_enviadas,

            "mensagens_recebidas":
                self.mensagens_recebidas,

            "heartbeats_realizados":
                self.heartbeats_realizados,

            "ultima_atividade":
                (
                    self.ultima_atividade.strftime(
                        "%d/%m/%Y %H:%M:%S"
                    )
                    if self.ultima_atividade
                    else None
                ),

            "ultimo_heartbeat":
                self.ultimo_heartbeat
        }

    def obter_resumo_operacional(self) -> Dict[str, Any]:
        """
        Retorna resumo operacional.
        """

        return {
            "status": self.status,
            "versao": self.versao,
            "ciclos": self.ciclos,
            "componentes_registrados":
                self.total_componentes_registrados,
            "componentes_conectados":
                len(self.componentes_conectados),
            "mensagens_enviadas":
                self.mensagens_enviadas,
            "mensagens_recebidas":
                self.mensagens_recebidas,
            "broadcasts_realizados":
                self.broadcasts_realizados,
            "heartbeats_realizados":
                self.heartbeats_realizados,
            "sincronizacoes_realizadas":
                self.sincronizacoes_realizadas,
            "trocas_automaticas":
                self.trocas_automaticas,
            "total_falhas_detectadas":
                self.total_falhas_detectadas,
            "total_recuperacoes_realizadas":
                self.total_recuperacoes_realizadas,
            "total_descobertas_realizadas":
                self.total_descobertas_realizadas,
            "total_componentes_descobertos":
                self.total_componentes_descobertos
        }

    # ============================================================
    # SINCRONIZAÇÃO
    # ============================================================

    def sincronizar(self) -> Dict[str, Any]:
        """
        Sincroniza informações entre os barramentos.
        """

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.atualizar_heartbeat()

        barramentos = [
            self.barramento_principal,
            self.barramento_reserva,
            self.barramento_emergencial
        ]

        barramentos.extend(
            self.barramentos_especializados.values()
        )

        barramentos.extend(
            self.barramentos_locais.values()
        )

        barramentos.extend(
            self.barramentos_temporarios.values()
        )

        for barramento in barramentos:

            barramento["ultima_sincronizacao"] = agora

        self.sincronizacoes_realizadas += 1
        self.ultima_atividade = datetime.now()

        resultado = {
            "timestamp": agora,
            "status": "SINCRONIZADO",
            "barramentos_sincronizados": len(barramentos)
        }

        self.registrar(
            f"Sincronização realizada: {resultado}"
        )

        return resultado

    # ============================================================
    # REDUNDÂNCIA
    # ============================================================

    def alternar_barramento(
        self,
        destino: str = "RESERVA"
    ) -> bool:
        """
        Alterna o barramento operacional.

        Destinos:
        - RESERVA
        - EMERGENCIAL
        """

        destino = destino.upper()

        if destino not in [
            "RESERVA",
            "EMERGENCIAL"
        ]:

            self.registrar(
                f"Destino inválido para alternância: {destino}"
            )

            return False

        if destino == "RESERVA":

            if not self.barramento_reserva["ativo"]:

                self.registrar(
                    "Barramento Reserva não está disponível"
                )

                return False

            self.barramento_principal["ativo"] = False
            self.barramento_principal["status"] = "INATIVO"

            self.barramento_reserva["ativo"] = True
            self.barramento_reserva["status"] = "ATIVO"

            self.barramento_emergencial["ativo"] = True
            self.barramento_emergencial["status"] = "PRONTO"

        else:

            if not self.barramento_emergencial["ativo"]:

                self.registrar(
                    "Barramento Emergencial não está disponível"
                )

                return False

            self.barramento_principal["ativo"] = False
            self.barramento_principal["status"] = "INATIVO"

            self.barramento_reserva["ativo"] = True
            self.barramento_reserva["status"] = "EM ESPERA"

            self.barramento_emergencial["ativo"] = True
            self.barramento_emergencial["status"] = "ATIVO"

        self.trocas_automaticas += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Barramento operacional alternado para: {destino}"
        )

        self.registrar_evento(
            f"Alternância de barramento: {destino}",
            "OK",
            "ALTA"
        )

        return True

    def recuperar_barramento_principal(self) -> bool:
        """
        Recupera o Barramento Principal.
        """

        if self.barramento_principal["ativo"]:

            self.registrar(
                "Barramento Principal já está ativo"
            )

            return True

        self.barramento_principal["ativo"] = True
        self.barramento_principal["status"] = "ATIVO"

        self.barramento_principal["heartbeat"] = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        # O Reserva continua disponível para uma nova falha.
        self.barramento_reserva["ativo"] = True
        self.barramento_reserva["status"] = "EM ESPERA"

        # Emergencial retorna ao estado de prontidão.
        self.barramento_emergencial["ativo"] = True
        self.barramento_emergencial["status"] = "PRONTO"

        self.total_recuperacoes_realizadas += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            "Barramento Principal recuperado com sucesso"
        )

        self.registrar_evento(
            "Recuperação do Barramento Principal",
            "OK",
            "ALTA"
        )

        return True

    # ============================================================
    # BARRAMENTOS TEMPORÁRIOS
    # ============================================================

    def criar_barramento_temporario(
        self,
        nome: str,
        finalidade: str = "Operação temporária"
    ) -> Dict[str, Any]:
        """
        Cria barramento temporário.
        """

        identificador = (
            f"temporario_{self.proximo_id_temporario}"
        )

        self.proximo_id_temporario += 1

        barramento = {
            "id": identificador,
            "nome": nome,
            "tipo": "TEMPORARIO",
            "status": "ATIVO",
            "ativo": True,
            "finalidade": finalidade,
            "heartbeat": None,
            "ultima_verificacao": None,
            "ultima_sincronizacao": None,
            "criado_em": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        }

        self.barramentos_temporarios[
            identificador
        ] = barramento

        self.total_barramentos_criados += 1

        self.atualizar_heartbeat()

        self.registrar(
            f"Barramento temporário criado: {nome}"
        )

        return barramento

    def remover_barramento_temporario(
        self,
        identificador: str
    ) -> bool:
        """
        Remove barramento temporário.
        """

        if identificador not in self.barramentos_temporarios:

            self.registrar(
                f"Barramento temporário não encontrado: "
                f"{identificador}"
            )

            return False

        del self.barramentos_temporarios[
            identificador
        ]

        self.registrar(
            f"Barramento temporário removido: "
            f"{identificador}"
        )

        return True

    # ============================================================
    # CICLO OPERACIONAL
    # ============================================================

    def executar_ciclo(self) -> Dict[str, Any]:
        """
        Executa um ciclo operacional.
        """

        self.ciclos += 1

        self.ultima_execucao = datetime.now()
        self.ultima_atividade = datetime.now()

        # 1. Heartbeat
        self.atualizar_heartbeat()

        # 2. Filas
        filas_processadas = self.processar_filas()

        # 3. Monitoramento
        monitoramento = self.monitorar()

        # 4. Sincronização periódica
        if self.ciclos % 5 == 0:
            self.sincronizar()

        # 5. Integridade periódica
        integridade = None

        if self.ciclos % 10 == 0:
            integridade = self.verificar_integridade()

        resultado = {
            "ciclo": self.ciclos,
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "filas_processadas": filas_processadas,
            "monitoramento": monitoramento,
            "integridade": integridade
        }

        self.resumo_operacional = resultado

        self.registrar(
            f"Ciclo {self.ciclos} concluído"
        )

        return resultado

    # ============================================================
    # INTEGRIDADE
    # ============================================================

    def verificar_integridade(self) -> Dict[str, Any]:
        """
        Verifica a integridade estrutural do Barramento.
        """

        problemas = []

        # --------------------------------------------------------
        # Barramento principal
        # --------------------------------------------------------

        if not self.barramento_principal["ativo"]:

            problemas.append(
                "Barramento Principal inativo"
            )

        # --------------------------------------------------------
        # Registro de componentes
        # --------------------------------------------------------

        for nome, componente in (
            self.registro_componentes.items()
        ):

            if componente["status"] != "CONECTADO":
                continue

            referencia = componente.get("referencia")

            # Referência inexistente pode ser aceitável
            # durante o registro manual inicial.
            if referencia is None:
                continue

            if not inspect.isclass(
                referencia
            ) and not hasattr(
                referencia,
                "__dict__"
            ):

                problemas.append(
                    f"Referência inválida: {nome}"
                )

        # --------------------------------------------------------
        # Duplicidades
        # --------------------------------------------------------

        listas = {
            "componentes": self.componentes_conectados,
            "modulos": self.modulos_conectados,
            "agentes": self.agentes_conectados,
            "motores": self.motores_conectados,
            "sistemas": self.sistemas_conectados,
            "integradores": self.integradores_conectados,
            "barramentos": self.barramentos_conectados
        }

        for nome_lista, lista in listas.items():

            if len(lista) != len(set(lista)):

                problemas.append(
                    f"Duplicidade detectada na lista "
                    f"{nome_lista}"
                )

        resultado = {
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "status": (
                "OK"
                if not problemas
                else "ATENCAO"
            ),
            "problemas": problemas,
            "total_problemas": len(problemas)
        }

        if problemas:

            self.total_falhas_detectadas += len(
                problemas
            )

            self.falhas_detectadas.extend(
                problemas
            )

            self.registrar(
                f"Problemas detectados: {problemas}"
            )

        else:

            self.registrar(
                "Verificação de integridade concluída: OK"
            )

        return resultado

    # ============================================================
    # DESCOBERTA AUTOMÁTICA
    # ============================================================

    def _localizar_classe_no_modulo(
        self,
        modulo: Any,
        nome_modulo: str
    ) -> Optional[Any]:
        """
        Localiza uma classe apropriada dentro de um módulo.

        A versão anterior utilizava:
            nome.capitalize()

        Isso não funciona corretamente para nomes como:
            gerenciador_memoria
            motor_de_aprendizado

        Aqui a localização é feita de forma mais segura.
        """

        candidatos = []

        nome_base = nome_modulo.replace(
            "_",
            " "
        ).title().replace(
            " ",
            ""
        )

        candidatos.append(nome_base)

        candidatos.append(
            nome_modulo.replace(
                "_",
                ""
            ).capitalize()
        )

        for candidato in candidatos:

            if hasattr(
                modulo,
                candidato
            ):

                objeto = getattr(
                    modulo,
                    candidato
                )

                if inspect.isclass(objeto):
                    return objeto

        # Procura classes definidas no próprio módulo.
        classes = inspect.getmembers(
            modulo,
            inspect.isclass
        )

        classes_locais = [
            classe
            for _, classe in classes
            if getattr(
                classe,
                "__module__",
                None
            ) == modulo.__name__
        ]

        if len(classes_locais) == 1:
            return classes_locais[0]

        # Procura classe cujo nome contenha palavras do módulo.
        palavras = [
            palavra.lower()
            for palavra in nome_modulo.split("_")
            if palavra
        ]

        melhor_classe = None
        melhor_quantidade = 0

        for classe in classes_locais:

            nome_classe = classe.__name__.lower()

            quantidade = sum(
                1
                for palavra in palavras
                if palavra in nome_classe
            )

            if quantidade > melhor_quantidade:

                melhor_quantidade = quantidade
                melhor_classe = classe

        return melhor_classe

    def descobrir_componentes(
        self
    ) -> List[Dict[str, Any]]:
        """
        Realiza descoberta automática de componentes.

        A descoberta:
        - tenta importar o módulo;
        - procura sua classe;
        - cria a referência quando possível;
        - registra o componente;
        - mantém falhas isoladas para não interromper
          toda a descoberta.
        """

        descobertos = []

        self.descoberta_automatica_ativa = True

        # Evita acumular duplicações no histórico de descobertas.
        self.componentes_descobertos = []

        for tipo, lista in (
            self.componentes_conhecidos.items()
        ):

            for nome in lista:

                try:

                    modulo = importlib.import_module(
                        nome
                    )

                    classe = (
                        self._localizar_classe_no_modulo(
                            modulo,
                            nome
                        )
                    )

                    referencia = None

                    if classe is not None:

                        try:
                            referencia = classe()

                        except Exception as erro_instanciacao:

                            self.registrar(
                                f"Classe encontrada em "
                                f"{nome}, mas não foi possível "
                                f"instanciá-la: "
                                f"{erro_instanciacao}"
                            )

                    componente = (
                        self.registrar_componente(
                            nome,
                            referencia,
                            tipo
                        )
                    )

                    descobertos.append(
                        componente
                    )

                    self.componentes_descobertos.append(
                        componente
                    )

                    if tipo == "modulos":
                        self._adicionar_componente_lista(
                            self.modulos_descobertos,
                            nome
                        )

                    elif tipo == "sistemas":
                        self._adicionar_componente_lista(
                            self.sistemas_descobertos,
                            nome
                        )

                    elif tipo == "integradores":
                        self._adicionar_componente_lista(
                            self.integradores_descobertos,
                            nome
                        )

                    elif tipo == "agentes":
                        self._adicionar_componente_lista(
                            self.agentes_descobertos,
                            nome
                        )

                    elif tipo == "barramentos":
                        self._adicionar_componente_lista(
                            self.barramentos_descobertos,
                            nome
                        )

                    self.total_componentes_descobertos += 1

                    self.registrar(
                        f"Componente descoberto: "
                        f"{nome} (tipo: {tipo})"
                    )

                except ModuleNotFoundError:

                    self._adicionar_componente_lista(
                        self.componentes_ignorados,
                        nome
                    )

                    self.registrar(
                        f"Componente não encontrado: {nome}"
                    )

                except ImportError as erro:

                    self._adicionar_componente_lista(
                        self.componentes_ignorados,
                        nome
                    )

                    self.registrar(
                        f"Erro de importação em "
                        f"{nome}: {erro}"
                    )

                except Exception as erro:

                    self.registrar(
                        f"Erro ao descobrir "
                        f"{nome}: {erro}"
                    )

        self.total_descobertas_realizadas += 1

        self.ultima_descoberta = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.ultima_atividade = datetime.now()

        self.registrar(
            "Descoberta automática concluída: "
            f"{len(descobertos)} componentes encontrados"
        )

        return descobertos

    # ============================================================
    # OPERAÇÃO CONTÍNUA
    # ============================================================

    def iniciar(self) -> None:
        """
        Inicia operação contínua.
        """

        if self.operacao_continua:

            self.registrar(
                "Barramento já está em operação contínua"
            )

            return

        self.operacao_continua = True

        self.inicio = datetime.now()

        self.fim = None
        self.tempo_total = None

        self.status = "OPERACIONAL"

        self.atualizar_heartbeat()

        self.registrar(
            "Barramento iniciado em operação contínua"
        )

        self.registrar_evento(
            "Barramento iniciado",
            "OK",
            "ALTA"
        )

    def parar(self) -> None:
        """
        Para operação contínua.
        """

        if not self.operacao_continua:

            self.registrar(
                "Barramento não está em operação contínua"
            )

            return

        self.operacao_continua = False

        self.fim = datetime.now()

        if self.inicio:

            self.tempo_total = (
                self.fim - self.inicio
            ).total_seconds()

        else:

            self.tempo_total = None

        self.status = "PARADO"

        self.registrar(
            f"Barramento parado. "
            f"Tempo total: {self.tempo_total}s"
        )

        self.registrar_evento(
            "Barramento parado",
            "OK",
            "NORMAL"
        )

    def executar(self) -> None:
        """
        Executa o Barramento continuamente.

        A operação permanece ativa até que:
        - seja interrompida pelo usuário;
        - ocorra erro não tratado.
        """

        self.iniciar()

        try:

            while self.operacao_continua:

                self.executar_ciclo()

                time.sleep(1)

        except KeyboardInterrupt:

            self.registrar(
                "Operação interrompida pelo usuário"
            )

        except Exception as erro:

            self.registrar(
                f"Erro na operação contínua: {erro}"
            )

            self.registrar_evento(
                f"Erro na operação contínua: {erro}",
                "ERRO",
                "CRITICA"
            )

        finally:

            self.parar()


# ================================================================
# TESTE E DEMONSTRAÇÃO
# ================================================================

if __name__ == "__main__":

    print("=" * 60)
    print(
        "BARRAMENTO HÍBRIDO INTELIGENTE DA REDE"
    )
    print("=" * 60)

    print(
        "\nInicializando Barramento..."
    )

    barramento = (
        BarramentoHibridoInteligenteDaRede()
    )

    # ------------------------------------------------------------
    # STATUS INICIAL
    # ------------------------------------------------------------

    print("\nSTATUS INICIAL:")

    status = barramento.obter_status()

    for chave, valor in status.items():

        print(
            f"  {chave}: {valor}"
        )

    # ------------------------------------------------------------
    # REGISTRO MANUAL
    # ------------------------------------------------------------

    print(
        "\nREGISTRANDO COMPONENTES..."
    )

    barramento.registrar_componente(
        "kernel",
        None,
        "modulos"
    )

    barramento.registrar_componente(
        "supervisor_geral",
        None,
        "modulos"
    )

    barramento.registrar_componente(
        "orquestrador_central_da_rede",
        None,
        "modulos"
    )

    # ------------------------------------------------------------
    # CONEXÃO
    # ------------------------------------------------------------

    print(
        "\nCONECTANDO COMPONENTES..."
    )

    barramento.conectar_componente(
        "kernel"
    )

    barramento.conectar_componente(
        "supervisor_geral"
    )

    # ------------------------------------------------------------
    # LISTAGEM
    # ------------------------------------------------------------

    print(
        "\nLISTA DE COMPONENTES:"
    )

    for componente in (
        barramento.listar_componentes()
    ):

        print(
            f"  - {componente['nome']} "
            f"({componente['tipo']}) -> "
            f"{componente['status']}"
        )

    # ------------------------------------------------------------
    # MENSAGEM
    # ------------------------------------------------------------

    print(
        "\nENVIANDO MENSAGEM..."
    )

    mensagem = barramento.enviar_mensagem(
        "kernel",
        "supervisor_geral",
        "TESTE",
        {
            "dado": "valor"
        }
    )

    print(
        f"  Mensagem enviada: "
        f"ID {mensagem['id']}"
    )

    # ------------------------------------------------------------
    # FILAS
    # ------------------------------------------------------------

    print(
        "\nPROCESSANDO FILAS..."
    )

    processadas = (
        barramento.processar_filas()
    )

    print(
        f"  {processadas} mensagens processadas"
    )

    # ------------------------------------------------------------
    # HEARTBEAT
    # ------------------------------------------------------------

    print(
        "\nATUALIZANDO HEARTBEAT..."
    )

    barramento.atualizar_heartbeat()

    heartbeat = (
        barramento.verificar_heartbeat_todos()
    )

    print(
        f"  Heartbeat: {heartbeat}"
    )

    # ------------------------------------------------------------
    # SINCRONIZAÇÃO
    # ------------------------------------------------------------

    print(
        "\nSINCRONIZANDO..."
    )

    sincronizacao = (
        barramento.sincronizar()
    )

    print(
        f"  {sincronizacao}"
    )

    # ------------------------------------------------------------
    # CICLO
    # ------------------------------------------------------------

    print(
        "\nEXECUTANDO CICLO..."
    )

    resultado = (
        barramento.executar_ciclo()
    )

    print(
        f"  Ciclo {resultado['ciclo']} executado"
    )

    # ------------------------------------------------------------
    # INTEGRIDADE
    # ------------------------------------------------------------

    print(
        "\nVERIFICANDO INTEGRIDADE..."
    )

    integridade = (
        barramento.verificar_integridade()
    )

    print(
        f"  Status: {integridade['status']}"
    )

    # ------------------------------------------------------------
    # STATUS FINAL
    # ------------------------------------------------------------

    print(
        "\nSTATUS FINAL:"
    )

    status = barramento.obter_status()

    for chave, valor in status.items():

        print(
            f"  {chave}: {valor}"
        )

    # ------------------------------------------------------------
    # RESUMO
    # ------------------------------------------------------------

    print(
        "\nRESUMO OPERACIONAL:"
    )

    resumo = (
        barramento.obter_resumo_operacional()
    )

    for chave, valor in resumo.items():

        print(
            f"  {chave}: {valor}"
        )

    print(
        "\n" + "=" * 60
    )

    print(
        "Barramento Híbrido Inteligente da Rede "
        "está operacional."
    )

    print(
        "=" * 60
    )
