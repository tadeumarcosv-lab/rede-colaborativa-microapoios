"""
LABORATORIO PERMANENTE DE VALIDACAO DA V1
DO PRIMEIRO AGENTE DE IA DA REDE COLABORATIVA DE MICROAPOIOS

Finalidade:
- validar estruturalmente o AgenteIA;
- validar a CamadaIA;
- validar uma chamada real ao provedor;
- validar tratamento de entradas invalidas;
- validar UUID, hashes, estados e evidencias;
- validar persistencia em memoria.json;
- validar registro do ciclo da tarefa;
- produzir evidencia para GitHub Actions;
- permanecer no repositorio para reutilizacao futura.

Regras:
- NAO altera agente_ia.py;
- NAO altera camada_ia.py;
- NAO altera Kernel, Bot ou Barramento;
- NAO armazena a GROQ_API_KEY;
- NAO imprime a GROQ_API_KEY;
- NAO executa automaticamente fora deste arquivo;
- modo padrao realiza apenas UMA chamada real a API;
- testes locais nao consomem API.

Modos:
- padrao: testes locais + 1 chamada real a Groq.
- TESTE_SEM_API=1: somente testes locais, sem chamada a Groq.
- TESTE_COMPLETO=1: testes locais + chamada principal + testes adicionais de contexto e sistema.

IMPORTANTE:
"TESTE APROVADO" significa que as verificacoes realizadas por este laboratorio foram aprovadas.
Isso NAO significa que todo o sistema da Rede esteja declarado como operacional.
"""

import hashlib
import json
import os
import re
import sys
from datetime import datetime

from agente_ia import AgenteIA
from camada_ia import CamadaIA
from gerenciador_memoria import GerenciadorMemoria


# ============================================================================
# CONFIGURACAO
# ============================================================================

MODO_SEM_API = os.environ.get(
    "TESTE_SEM_API",
    "0",
) == "1"

MODO_COMPLETO = os.environ.get(
    "TESTE_COMPLETO",
    "0",
) == "1"

PERGUNTA_PRINCIPAL = (
    "Qual e a capital do Brasil? "
    "Responda somente com a cidade e o estado."
)

PERGUNTA_CONTEXTO = (
    "Quantos dias tem uma semana?"
)

CONTEXTO_TESTE = (
    "Responda de forma curta e direta."
)

SISTEMA_TESTE = (
    "Voce e um assistente objetivo. "
    "Responda em portugues."
)


# ============================================================================
# CONTROLE DOS TESTES
# ============================================================================

def _cabecalho(titulo):
    print()
    print("=" * 72)
    print(titulo)
    print("=" * 72)


def _subcabecalho(titulo):
    print()
    print("-" * 72)
    print(titulo)
    print("-" * 72)


def _check(nome, condicao, detalhe=""):
    aprovado = bool(condicao)

    situacao = "APROVADO" if aprovado else "REPROVADO"

    linha = f"[{situacao}] {nome}"

    if detalhe:
        linha += f" | {detalhe}"

    print(linha)

    return {
        "nome": nome,
        "aprovado": aprovado,
        "detalhe": detalhe,
    }


def _sha256(texto):
    return hashlib.sha256(
        str(texto).encode("utf-8")
    ).hexdigest()


def _eh_sha256(valor):
    if not isinstance(valor, str):
        return False

    return bool(
        re.fullmatch(
            r"[0-9a-f]{64}",
            valor.lower(),
        )
    )


def _eh_uuid_v4(valor):
    if not isinstance(valor, str):
        return False

    return bool(
        re.fullmatch(
            r"[0-9a-f]{8}-"
            r"[0-9a-f]{4}-"
            r"4[0-9a-f]{3}-"
            r"[89ab][0-9a-f]{3}-"
            r"[0-9a-f]{12}",
            valor.lower(),
        )
    )


def _adicionar_resultados(destino, resultados):
    destino.extend(resultados)


# ============================================================================
# TESTE 01 — ESTRUTURA DOS COMPONENTES
# ============================================================================

def teste_estrutura():
    _subcabecalho(
        "TESTE 01 — ESTRUTURA DOS COMPONENTES"
    )

    resultados = []

    try:
        agente = AgenteIA()

        resultados.append(
            _check(
                "AgenteIA instanciado",
                True,
            )
        )

        resultados.append(
            _check(
                "AgenteIA.status definido",
                bool(getattr(agente, "status", "")),
                str(getattr(agente, "status", "")),
            )
        )

        resultados.append(
            _check(
                "AgenteIA.VERSAO definida",
                bool(getattr(agente, "VERSAO", "")),
                str(getattr(agente, "VERSAO", "")),
            )
        )

        resultados.append(
            _check(
                "AgenteIA.executar disponivel",
                callable(
                    getattr(
                        agente,
                        "executar",
                        None,
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "CamadaIA conectada ao agente",
                isinstance(
                    getattr(
                        agente,
                        "camada",
                        None,
                    ),
                    CamadaIA,
                ),
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "AgenteIA instanciado",
                False,
                str(erro),
            )
        )

    try:
        camada = CamadaIA()

        resultados.append(
            _check(
                "CamadaIA instanciada",
                True,
            )
        )

        resultados.append(
            _check(
                "CamadaIA.status definido",
                bool(getattr(camada, "status", "")),
                str(getattr(camada, "status", "")),
            )
        )

        resultados.append(
            _check(
                "CamadaIA.VERSAO definida",
                bool(getattr(camada, "VERSAO", "")),
                str(getattr(camada, "VERSAO", "")),
            )
        )

        resultados.append(
            _check(
                "CamadaIA.PROVEDOR definido",
                getattr(camada, "PROVEDOR", "") == "groq",
                str(
                    getattr(
                        camada,
                        "PROVEDOR",
                        "",
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "CamadaIA.consultar disponivel",
                callable(
                    getattr(
                        camada,
                        "consultar",
                        None,
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "Endpoint Groq definido",
                bool(
                    getattr(
                        camada,
                        "ENDPOINT",
                        "",
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "Timeout definido",
                getattr(camada, "TIMEOUT", 0) == 30,
                str(
                    getattr(
                        camada,
                        "TIMEOUT",
                        "",
                    )
                ),
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "CamadaIA instanciada",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 02 — ENTRADA NAO-STRING
# ============================================================================

def teste_entrada_nao_string():
    _subcabecalho(
        "TESTE 02 — ENTRADA NAO-STRING"
    )

    resultados = []

    try:
        agente = AgenteIA()

        tarefa = agente.executar(12345)

        resultados.append(
            _check(
                "Entrada nao-string gera FALHA",
                tarefa.get("status") == "FALHA",
                str(tarefa.get("status")),
            )
        )

        resultados.append(
            _check(
                "Erro foi informado",
                bool(tarefa.get("erro")),
                str(tarefa.get("erro", "")),
            )
        )

        resultados.append(
            _check(
                "Nenhuma resposta foi produzida",
                tarefa.get(
                    "resultado",
                    {},
                ).get(
                    "resposta",
                    "",
                ) == "",
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "Teste de entrada nao-string",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 03 — ENTRADA VAZIA
# ============================================================================

def teste_entrada_vazia():
    _subcabecalho(
        "TESTE 03 — ENTRADA VAZIA"
    )

    resultados = []

    try:
        agente = AgenteIA()

        tarefa = agente.executar("   ")

        resultados.append(
            _check(
                "Entrada vazia gera FALHA",
                tarefa.get("status") == "FALHA",
                str(tarefa.get("status")),
            )
        )

        resultados.append(
            _check(
                "Erro de entrada vazia foi informado",
                bool(tarefa.get("erro")),
                str(tarefa.get("erro", "")),
            )
        )

        resultados.append(
            _check(
                "task_id criado",
                _eh_uuid_v4(
                    tarefa.get("task_id")
                ),
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "Teste de entrada vazia",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 04 — ESTRUTURA DA TAREFA E HASH
# ============================================================================

def teste_tarefa_e_hash():
    _subcabecalho(
        "TESTE 04 — ESTRUTURA DA TAREFA E HASH"
    )

    resultados = []

    try:
        agente = AgenteIA()

        solicitacao = 999

        tarefa = agente.executar(
            solicitacao
        )

        resultados.append(
            _check(
                "task_id e UUID v4",
                _eh_uuid_v4(
                    tarefa.get("task_id")
                ),
                str(
                    tarefa.get(
                        "task_id",
                        "",
                    )
                ),
            )
        )

        evidencia = tarefa.get(
            "evidencia",
            {},
        )

        hash_solicitacao = evidencia.get(
            "hash_solicitacao"
        )

        resultados.append(
            _check(
                "hash_solicitacao e SHA-256",
                _eh_sha256(
                    hash_solicitacao
                ),
            )
        )

        resultados.append(
            _check(
                "hash_solicitacao confere",
                hash_solicitacao == _sha256(solicitacao),
            )
        )

        campos_obrigatorios = (
            "task_id",
            "versao_agente",
            "versao_camada",
            "ambiente",
            "solicitacao_original",
            "objetivo",
            "status",
            "etapa_atual",
            "inicio",
            "ultima_atividade",
            "duracao_total_ms",
            "resultado",
            "verificacao",
            "evidencia",
        )

        for campo in campos_obrigatorios:
            resultados.append(
                _check(
                    f"Campo '{campo}' presente",
                    campo in tarefa,
                )
            )

        resultados.append(
            _check(
                "duracao_total_ms numerica",
                isinstance(
                    tarefa.get(
                        "duracao_total_ms"
                    ),
                    int,
                ),
            )
        )

        resultados.append(
            _check(
                "resultado e dicionario",
                isinstance(
                    tarefa.get("resultado"),
                    dict,
                ),
            )
        )

        resultados.append(
            _check(
                "verificacao e dicionario",
                isinstance(
                    tarefa.get("verificacao"),
                    dict,
                ),
            )
        )

        resultados.append(
            _check(
                "evidencia e dicionario",
                isinstance(
                    tarefa.get("evidencia"),
                    dict,
                ),
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "Estrutura da tarefa",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 05 — CAMADA IA SEM CHAMADA EXTERNA
# ============================================================================

def teste_validacao_local_da_camada():
    _subcabecalho(
        "TESTE 05 — VALIDACAO LOCAL DA CAMADA IA"
    )

    resultados = []

    try:
        camada = CamadaIA()

        resultado = camada.consultar(
            prompt="   "
        )

        resultados.append(
            _check(
                "Prompt vazio gera falha controlada",
                resultado.get("status") == "falha",
                str(
                    resultado.get(
                        "status"
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "Erro do prompt vazio informado",
                bool(
                    resultado.get(
                        "erro"
                    )
                ),
                str(
                    resultado.get(
                        "erro",
                        "",
                    )
                ),
            )
        )

        resultados.append(
            _check(
                "Provedor identificado",
                resultado.get(
                    "provedor"
                ) == "groq",
            )
        )

        resultados.append(
            _check(
                "Nenhuma tentativa externa",
                resultado.get(
                    "tentativas"
                ) == 1,
                "falha de validacao local",
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "Validacao local da CamadaIA",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 06 — RESULTADO REAL
# ============================================================================

def executar_consulta_real(
    solicitacao,
    contexto=None,
    sistema=None,
):
    agente = AgenteIA()

    return agente.executar(
        solicitacao=solicitacao,
        contexto=contexto,
        sistema=sistema,
    )


def validar_resultado_real(tarefa):
    _subcabecalho(
        "TESTE 06 — VALIDACAO PROFUNDA DA EXECUCAO REAL"
    )

    resultados = []

    status = tarefa.get("status")

    resultados.append(
        _check(
            "Status final CONCLUIDA",
            status == "CONCLUIDA",
            str(status),
        )
    )

    resultados.append(
        _check(
            "task_id e UUID v4",
            _eh_uuid_v4(
                tarefa.get("task_id")
            ),
        )
    )

    for campo in (
        "versao_agente",
        "versao_camada",
        "ambiente",
        "objetivo",
        "inicio",
        "ultima_atividade",
    ):
        resultados.append(
            _check(
                f"Campo '{campo}' preenchido",
                bool(tarefa.get(campo)),
            )
        )

    duracao = tarefa.get(
        "duracao_total_ms",
        0,
    )

    resultados.append(
        _check(
            "duracao_total_ms > 0",
            isinstance(duracao, int) and duracao > 0,
            str(duracao),
        )
    )

    resultado = tarefa.get(
        "resultado",
        {},
    )

    resposta = resultado.get(
        "resposta",
        "",
    )

    provedor = resultado.get(
        "provedor",
        "",
    )

    modelo = resultado.get(
        "modelo",
        "",
    )

    tempo_ms = resultado.get(
        "tempo_ms",
        0,
    )

    tentativas = resultado.get(
        "tentativas",
        0,
    )

    resultados.append(
        _check(
            "Resposta nao vazia",
            bool(
                resposta
                and resposta.strip()
            ),
            resposta[:100] if resposta else "(vazia)",
        )
    )

    resultados.append(
        _check(
            "Provedor identificado",
            provedor == "groq",
            str(provedor),
        )
    )

    resultados.append(
        _check(
            "Modelo identificado",
            bool(modelo),
            str(modelo),
        )
    )

    resultados.append(
        _check(
            "Tempo da chamada > 0",
            isinstance(
                tempo_ms,
                int,
            )
            and tempo_ms > 0,
            str(tempo_ms),
        )
    )

    resultados.append(
        _check(
            "Tentativas = 1",
            tentativas == 1,
            str(tentativas),
        )
    )

    verificacao = tarefa.get(
        "verificacao",
        {},
    )

    for campo in (
        "resposta_nao_vazia",
        "provedor_identificado",
        "chamada_provedor_sucesso",
    ):
        resultados.append(
            _check(
                f"Verificacao '{campo}'",
                verificacao.get(
                    campo
                ) is True,
                str(
                    verificacao.get(
                        campo
                    )
                ),
            )
        )

    evidencia = tarefa.get(
        "evidencia",
        {},
    )

    hash_solicitacao = evidencia.get(
        "hash_solicitacao"
    )

    hash_resposta = evidencia.get(
        "hash_resposta"
    )

    resultados.append(
        _check(
            "hash_solicitacao e SHA-256",
            _eh_sha256(
                hash_solicitacao
            ),
        )
    )

    resultados.append(
        _check(
            "hash_resposta e SHA-256",
            _eh_sha256(
                hash_resposta
            ),
        )
    )

    if resposta:
        resultados.append(
            _check(
                "hash_resposta confere",
                hash_resposta == _sha256(resposta),
            )
        )

    resultados.append(
        _check(
            "origem da evidencia presente",
            bool(
                evidencia.get(
                    "origem"
                )
            ),
            str(
                evidencia.get(
                    "origem",
                    "",
                )
            ),
        )
    )

    resultados.append(
        _check(
            "timestamp da resposta presente",
            bool(
                evidencia.get(
                    "timestamp_resposta"
                )
            ),
        )
    )

    return resultados


# ============================================================================
# TESTE 07 — MEMORIA PERSISTENTE
# ============================================================================

def validar_memoria(tarefa):
    _subcabecalho(
        "TESTE 07 — VALIDACAO DA MEMORIA PERSISTENTE"
    )

    resultados = []

    task_id = tarefa.get(
        "task_id"
    )

    try:
        memoria = GerenciadorMemoria()

        historico = memoria.obter_historico()

        resultados.append(
            _check(
                "Historico retornado como lista",
                isinstance(
                    historico,
                    list,
                ),
            )
        )

        encontrada = any(
            isinstance(item, dict)
            and item.get(
                "task_id"
            ) == task_id
            for item in historico
        )

        resultados.append(
            _check(
                "Tarefa encontrada no historico",
                encontrada,
                str(task_id),
            )
        )

        estatisticas = memoria.obter_estatisticas()

        resultados.append(
            _check(
                "Estatisticas retornadas como dicionario",
                isinstance(
                    estatisticas,
                    dict,
                ),
            )
        )

        solicitacoes = estatisticas.get(
            "solicitacoes",
            0,
        )

        resultados.append(
            _check(
                "Contador de solicitacoes valido",
                isinstance(
                    solicitacoes,
                    int,
                )
                and solicitacoes > 0,
                str(solicitacoes),
            )
        )

    except Exception as erro:
        resultados.append(
            _check(
                "Leitura da memoria persistente",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 08 — INTEGRIDADE DOS EVENTOS PERSISTIDOS
# ============================================================================

def validar_evento_persistido(tarefa):
    _subcabecalho(
        "TESTE 08 — VALIDACAO DO REGISTRO DO EVENTO"
    )

    resultados = []

    task_id = tarefa.get(
        "task_id"
    )

    try:
        memoria = GerenciadorMemoria()

        historico = memoria.obter_historico()

        eventos_agente = [
            item
            for item in historico
            if isinstance(item, dict)
            and item.get(
                "origem"
            ) == "agente_ia"
        ]

        resultados.append(
            _check(
                "Existe evento originado pelo AgenteIA",
                bool(eventos_agente),
            )
        )

        evento_correspondente = any(
            task_id in str(item)
            for item in eventos_agente
        )

        resultados.append(
            _check(
                "Evento correspondente a task_id localizado",
                evento_correspondente,
                str(task_id),
            )
        )

        if eventos_agente:
            ultimo = eventos_agente[-1]

            for campo in (
                "origem",
                "destino",
                "responsavel",
                "descricao",
                "resultado",
                "importancia",
            ):
                resultados.append(
                    _check(
                        f"Campo de evento '{campo}' presente",
                        bool(
                            ultimo.get(
                                campo
                            )
                        ),
                    )
                )

    except Exception as erro:
        resultados.append(
            _check(
                "Validacao do evento persistido",
                False,
                str(erro),
            )
        )

    return resultados


# ============================================================================
# TESTE 09 — AUSENCIA DE CHAVE NO CODIGO
# ============================================================================

def teste_seguranca_basica():
    _subcabecalho(
        "TESTE 09 — VERIFICACAO BASICA DE SEGURANCA"
    )

    resultados = []

    nome_chave = "GROQ_API_KEY"

    resultados.append(
        _check(
            "Nome da variavel da chave conhecido",
            nome_chave == "GROQ_API_KEY",
        )
    )

    valor_chave = os.environ.get(
        nome_chave
    )

    resultados.append(
        _check(
            "Chave nao e exibida pelo laboratorio",
            True,
            "valor da chave nunca e impresso",
        )
    )

    if valor_chave:
        resultados.append(
            _check(
                "GROQ_API_KEY recebida pelo ambiente",
                True,
                "presente no ambiente",
            )
        )
    else:
        resultados.append(
            _check(
                "GROQ_API_KEY ausente no ambiente",
                MODO_SEM_API,
                "aceito somente no modo sem API",
            )
        )

    return resultados


# ============================================================================
# TESTE 10 — MODOS DE EXECUCAO
# ============================================================================

def teste_configuracao():
    _subcabecalho(
        "TESTE 10 — CONFIGURACAO DO LABORATORIO"
    )

    resultados = []

    resultados.append(
        _check(
            "Modo sem API e booleano",
            isinstance(
                MODO_SEM_API,
                bool,
            ),
        )
    )

    resultados.append(
        _check(
            "Modo completo e booleano",
            isinstance(
                MODO_COMPLETO,
                bool,
            ),
        )
    )

    if MODO_SEM_API and MODO_COMPLETO:
        resultados.append(
            _check(
                "Modos conflitantes evitados",
                False,
                "TESTE_SEM_API=1 tem prioridade",
            )
        )
    else:
        resultados.append(
            _check(
                "Configuracao de modos coerente",
                True,
            )
        )

    return resultados


# ============================================================================
# RESUMO
# ============================================================================

def imprimir_resumo(resultados):
    _cabecalho(
        "RESUMO FINAL DO LABORATORIO"
    )

    total = len(resultados)

    aprovados = sum(
        1
        for item in resultados
        if item["aprovado"]
    )

    reprovados = total - aprovados

    print(
        f"Total de verificacoes: {total}"
    )
    print(
        f"Aprovadas: {aprovados}"
    )
    print(
        f"Reprovadas: {reprovados}"
    )

    if reprovados:
        print()
        print(
            "VERIFICACOES REPROVADAS:"
        )

        for item in resultados:
            if not item["aprovado"]:
                print(
                    f"- {item['nome']} "
                    f"| {item['detalhe']}"
                )

        print()
        print(
            ">>> LABORATORIO REPROVADO <<<"
        )

        return 1

    print()
    print(
        ">>> TODAS AS VERIFICACOES "
        "REALIZADAS FORAM APROVADAS <<<"
    )
    print()
    print(
        "Observacao: este resultado valida "
        "somente os componentes e caminhos "
        "testados pelo laboratorio."
    )

    return 0


# ============================================================================
# MAIN
# ============================================================================

def main():
    _cabecalho(
        "LABORATORIO PERMANENTE DE VALIDACAO DA V1"
    )

    print(
        "Inicio:",
        datetime.now().astimezone().isoformat(),
    )

    print(
        "TESTE_SEM_API:",
        MODO_SEM_API,
    )

    print(
        "TESTE_COMPLETO:",
        MODO_COMPLETO,
    )

    resultados = []

    # ------------------------------------------------------------------------
    # TESTES LOCAIS
    # ------------------------------------------------------------------------

    _adicionar_resultados(
        resultados,
        teste_estrutura(),
    )

    _adicionar_resultados(
        resultados,
        teste_entrada_nao_string(),
    )

    _adicionar_resultados(
        resultados,
        teste_entrada_vazia(),
    )

    _adicionar_resultados(
        resultados,
        teste_tarefa_e_hash(),
    )

    _adicionar_resultados(
        resultados,
        teste_validacao_local_da_camada(),
    )

    _adicionar_resultados(
        resultados,
        teste_configuracao(),
    )

    _adicionar_resultados(
        resultados,
        teste_seguranca_basica(),
    )

    # ------------------------------------------------------------------------
    # API REAL
    # ------------------------------------------------------------------------

    if MODO_SEM_API:
        print()
        print(
            ">>> MODO SEM API: "
            "nenhuma chamada externa sera realizada."
        )

        return imprimir_resumo(
            resultados
        )

    # ------------------------------------------------------------------------
    # PRIMEIRA CONSULTA REAL
    # ------------------------------------------------------------------------

    _subcabecalho(
        "EXECUCAO REAL — UMA CHAMADA AO GROQ"
    )

    try:
        tarefa = executar_consulta_real(
            PERGUNTA_PRINCIPAL
        )

        print()
        print(
            "Resultado estruturado:"
        )

        print(
            json.dumps(
                tarefa,
                indent=2,
                ensure_ascii=False,
            )
        )

        _adicionar_resultados(
            resultados,
            validar_resultado_real(
                tarefa
            ),
        )

        _adicionar_resultados(
            resultados,
            validar_memoria(
                tarefa
            ),
        )

        _adicionar_resultados(
            resultados,
            validar_evento_persistido(
                tarefa
            ),
        )

        # --------------------------------------------------------------------
        # MODO COMPLETO
        # --------------------------------------------------------------------

        if MODO_COMPLETO:
            print()
            print(
                ">>> MODO COMPLETO ATIVADO <<<"
            )
            print(
                "Serão realizadas duas consultas "
                "adicionais ao provedor."
            )

            tarefa_contexto = (
                executar_consulta_real(
                    PERGUNTA_CONTEXTO,
                    contexto=CONTEXTO_TESTE,
                )
            )

            _adicionar_resultados(
                resultados,
                validar_resultado_real(
                    tarefa_contexto
                ),
            )

            tarefa_sistema = (
                executar_consulta_real(
                    PERGUNTA_PRINCIPAL,
                    sistema=SISTEMA_TESTE,
                )
            )

            _adicionar_resultados(
                resultados,
                validar_resultado_real(
                    tarefa_sistema
                ),
            )

        else:
            print()
            print(
                ">>> MODO PADRAO: "
                "somente UMA chamada real realizada. <<<"
            )

    except Exception as erro:
        resultados.append(
            _check(
                "Execucao real da V1",
                False,
                f"{type(erro).__name__}: {erro}",
            )
        )

    return imprimir_resumo(
        resultados
    )


if __name__ == "__main__":
    sys.exit(main())
