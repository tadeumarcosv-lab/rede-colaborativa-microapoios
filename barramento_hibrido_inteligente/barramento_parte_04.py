"""
BARRAMENTO HÍBRIDO INTELIGENTE DA REDE
PARTE 04 DE 04

Métodos:
- sincronização
- redundância
- recuperação
- ciclo operacional
- integridade
- descoberta automática
- operação contínua
- execução
- composição final da classe
- teste básico
"""

from datetime import datetime
import time

from barramento_parte_01 import BarramentoBase
from barramento_parte_02 import BarramentoComunicacaoMixin
from barramento_parte_03 import BarramentoComponentesMixin


class BarramentoOperacionalMixin:

    # ============================================
    # SINCRONIZAÇÃO
    # ============================================

    def sincronizar(self):
        """Sincroniza as informações entre os barramentos."""

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.atualizar_heartbeat()

        self.barramento_principal[
            "ultima_sincronizacao"
        ] = agora

        self.barramento_reserva[
            "ultima_sincronizacao"
        ] = agora

        self.barramento_emergencial[
            "ultima_sincronizacao"
        ] = agora

        for barramento in (
            self.barramentos_especializados.values()
        ):
            barramento["ultima_sincronizacao"] = agora

        for barramento in self.barramentos_locais.values():
            barramento["ultima_sincronizacao"] = agora

        self.sincronizacoes_realizadas += 1
        self.ultima_atividade = datetime.now()

        resultado = {
            "timestamp": agora,
            "status": "SINCRONIZADO",
            "barramentos_sincronizados": (
                3
                + len(self.barramentos_especializados)
                + len(self.barramentos_locais)
            )
        }

        self.registrar(
            f"Sincronização realizada: {resultado}"
        )

        return resultado

    # ============================================
    # REDUNDÂNCIA
    # ============================================

    def alternar_barramento(
        self,
        destino: str = "RESERVA"
    ) -> bool:
        """Alterna o barramento ativo."""

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
                    "Barramento Reserva não está ativo"
                )
                return False

            destino_barramento = self.barramento_reserva

        else:

            if not self.barramento_emergencial["ativo"]:
                self.registrar(
                    "Barramento Emergencial não está ativo"
                )
                return False

            destino_barramento = (
                self.barramento_emergencial
            )

        self.barramento_principal["ativo"] = False
        self.barramento_principal["status"] = "INATIVO"

        destino_barramento["ativo"] = True
        destino_barramento["status"] = "ATIVO"

        self.trocas_automaticas += 1
        self.ultima_atividade = datetime.now()

        self.registrar(
            f"Barramento alternado para: {destino}"
        )

        self.registrar_evento(
            f"Alternância de barramento: {destino}",
            "OK",
            "ALTA"
        )

        return True

    def recuperar_barramento_principal(self) -> bool:
        """Tenta recuperar o Barramento Principal."""

        if self.barramento_principal["ativo"]:

            self.registrar(
                "Barramento Principal já está ativo"
            )

            return True

        agora = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        self.barramento_principal["ativo"] = True
        self.barramento_principal["status"] = "ATIVO"
        self.barramento_principal["heartbeat"] = agora
        self.barramento_principal[
            "ultima_verificacao"
        ] = agora

        if self.barramento_reserva["ativo"]:

            self.barramento_reserva["ativo"] = False
            self.barramento_reserva[
                "status"
            ] = "EM ESPERA"

        if self.barramento_emergencial["ativo"]:

            self.barramento_emergencial["ativo"] = False
            self.barramento_emergencial[
                "status"
            ] = "PRONTO"

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

    # ============================================
    # CICLO OPERACIONAL
    # ============================================

    def executar_ciclo(self):
        """Executa um ciclo operacional."""

        self.ciclos += 1
        self.ultima_execucao = datetime.now()
        self.ultima_atividade = datetime.now()

        self.atualizar_heartbeat()

        filas_processadas = self.processar_filas()

        monitoramento = self.monitorar()

        if self.ciclos % 5 == 0:
            self.sincronizar()

        if self.ciclos % 10 == 0:
            self.verificar_integridade()

        resultado = {
            "ciclo": self.ciclos,
            "timestamp": datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
            "filas_processadas": filas_processadas,
            "monitoramento": monitoramento
        }

        self.resumo_operacional = resultado

        self.registrar(
            f"Ciclo {self.ciclos} concluído"
        )

        return resultado

    # ============================================
    # INTEGRIDADE
    # ============================================

    def verificar_integridade(self):
        """Verifica a integridade do Barramento."""

        problemas = []

        if not self.barramento_principal["ativo"]:
            problemas.append(
                "Barramento Principal inativo"
            )

        if not self.barramento_reserva["ativo"]:
            problemas.append(
                "Barramento Reserva inativo"
            )

        if not self.barramento_emergencial["ativo"]:
            problemas.append(
                "Barramento Emergencial inativo"
            )

        for nome, componente in (
            self.registro_componentes.items()
        ):

            if componente["status"] == "CONECTADO":

                referencia = componente["referencia"]

                if referencia is None:
                    problemas.append(
                        f"Componente {nome} sem referência"
                    )

                elif not hasattr(
                    referencia,
                    "executar"
                ):
                    problemas.append(
                        f"Componente {nome} "
                        "não possui método executar()"
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

            self.registrar(
                f"Problemas detectados: {problemas}"
            )

        return resultado

    # ============================================
    # DESCOBERTA AUTOMÁTICA
    # ============================================

    def descobrir_componentes(self):
        """Realiza descoberta automática."""

        descobertos = []

        for tipo, lista in (
            self.componentes_conhecidos.items()
        ):

            for nome in lista:

                try:

                    nome_classe = (
                        self.mapeamento_classes.get(
                            nome,
                            nome.capitalize()
                        )
                    )

                    modulo = importlib.import_module(
                        nome
                    )

                    if hasattr(
                        modulo,
                        nome_classe
                    ):

                        classe = getattr(
                            modulo,
                            nome_classe
                        )

                        referencia = classe()

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

                        self.total_componentes_descobertos += 1

                        self.registrar(
                            "Componente descoberto: "
                            f"{nome} "
                            f"(tipo: {tipo})"
                        )

                    else:

                        self.registrar(
                            f"Classe '{nome_classe}' "
                            f"não encontrada no módulo "
                            f"{nome}"
                        )

                        self.componentes_ignorados.append(
                            nome
                        )

                except ImportError:

                    self.registrar(
                        f"Componente não encontrado: {nome}"
                    )

                    self.componentes_ignorados.append(
                        nome
                    )

                except Exception as erro:

                    self.registrar(
                        f"Erro ao descobrir "
                        f"{nome}: {erro}"
                    )

        self.total_descobertas_realizadas += 1

        self.ultima_descoberta = (
            datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        )

        self.ultima_atividade = datetime.now()

        self.registrar(
            "Descoberta automática concluída: "
            f"{len(descobertos)} componentes encontrados"
        )

        return descobertos

    # ============================================
    # OPERAÇÃO CONTÍNUA
    # ============================================

    def iniciar(self):
        """Inicia a operação contínua."""

        if self.operacao_continua:

            self.registrar(
                "Barramento já está em operação contínua"
            )

            return

        self.operacao_continua = True
        self.inicio = datetime.now()
        self.status = "OPERACIONAL"

        self.registrar(
            "Barramento iniciado em operação contínua"
        )

        self.registrar_evento(
            "Barramento iniciado",
            "OK",
            "ALTA"
        )

    def parar(self):
        """Para a operação contínua."""

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

        self.status = "PARADO"

        self.registrar(
            "Barramento parado. "
            f"Tempo total: {self.tempo_total}s"
        )

        self.registrar_evento(
            "Barramento parado",
            "OK",
            "NORMAL"
        )

    def executar(self):
        """Executa o Barramento continuamente."""

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


# ============================================
# CLASSE FINAL DO PRIMEIRO CONJUNTO
# ============================================

class BarramentoHibridoInteligenteDaRede(
    BarramentoBase,
    BarramentoComunicacaoMixin,
    BarramentoComponentesMixin,
    BarramentoOperacionalMixin
):
    """
    Classe final do Barramento Híbrido Inteligente.

    A classe reúne as quatro partes físicas do primeiro
    conjunto sem duplicar a estrutura principal.
    """

    pass


# ============================================
# TESTE BÁSICO
# ============================================

if __name__ == "__main__":

    print("=" * 60)
    print("BARRAMENTO HÍBRIDO INTELIGENTE DA REDE")
    print("=" * 60)

    print("\nInicializando Barramento...")

    barramento = (
        BarramentoHibridoInteligenteDaRede()
    )

    print("\nSTATUS INICIAL:")

    status = barramento.obter_status()

    for chave, valor in status.items():
        print(f"  {chave}: {valor}")

    print("\nREGISTRANDO COMPONENTES...")

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

    print("\nCONECTANDO COMPONENTES...")

    barramento.conectar_componente("kernel")
    barramento.conectar_componente(
        "supervisor_geral"
    )

    print("\nLISTA DE COMPONENTES:")

    for componente in (
        barramento.listar_componentes()
    ):
        print(
            f"  - {componente['nome']} "
            f"({componente['tipo']}) "
            f"-> {componente['status']}"
        )

    print("\nENVIANDO MENSAGEM...")

    mensagem = barramento.enviar_mensagem(
        "kernel",
        "supervisor_geral",
        "TESTE",
        {"dado": "valor"}
    )

    print(
        f"  Mensagem enviada: "
        f"ID {mensagem['id']}"
    )

    print("\nPROCESSANDO FILAS...")

    processadas = (
        barramento.processar_filas()
    )

    print(
        f"  {processadas} mensagens processadas"
    )

    print("\nEXECUTANDO CICLO...")

    resultado = (
        barramento.executar_ciclo()
    )

    print(
        f"  Ciclo {resultado['ciclo']} executado"
    )

    print("\nSTATUS FINAL:")

    status = barramento.obter_status()

    for chave, valor in status.items():
        print(f"  {chave}: {valor}")

    print("\nRESUMO OPERACIONAL:")

    resumo = (
        barramento.obter_resumo_operacional()
    )

    for chave, valor in resumo.items():
        print(f"  {chave}: {valor}")

    print("\n" + "=" * 60)
    print(
        "Barramento Híbrido Inteligente "
        "da Rede está operacional."
    )
    print("=" * 60)
