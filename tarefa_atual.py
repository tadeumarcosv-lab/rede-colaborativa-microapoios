import json
import os
import hashlib

from agente_trabalho import AgenteTrabalho
from gerenciador_memoria import GerenciadorMemoria


def gerar_resumo_markdown(resultado: dict) -> str:
    """Gera um resumo em Markdown para o GitHub Step Summary."""
    linhas = []
    linhas.append("## Resultado da Tarefa\n")
    linhas.append(f"**Status:** `{resultado.get('status', 'N/A')}`\n")
    linhas.append(f"**Confiança:** `{resultado.get('confianca', 'N/A')}`\n")
    linhas.append(f"**Task ID:** `{resultado.get('task_id', 'N/A')}`\n")
    linhas.append(f"**Run ID:** `{resultado.get('run_id', 'N/A')}`\n")
    linhas.append(f"**Iterações:** {resultado.get('iteracoes', 0)}\n")
    linhas.append(f"**Ferramentas executadas:** {resultado.get('chamadas_ferramentas', 0)}\n")
    linhas.append(f"**Duração:** {resultado.get('duracao_ms', 0)} ms\n")

    linhas.append("\n### Resposta\n")
    linhas.append(f"{resultado.get('resposta', 'Sem resposta.')}\n")

    evidencias = resultado.get("evidencias", [])
    if evidencias:
        linhas.append("\n### Evidências\n")
        for ev in evidencias:
            linhas.append(f"- **{ev.get('evidencia_id', '?')}** | Ferramenta: `{ev.get('ferramenta', '?')}` | Origem: `{ev.get('origem', '?')}`")
            linhas.append(f"  - SHA-256: `{ev.get('sha256', '?')}`")
            linhas.append(f"  - Data: {ev.get('data', '?')}\n")

    observacoes = resultado.get("observacoes", [])
    if observacoes:
        linhas.append("\n### Observações\n")
        for obs in observacoes:
            linhas.append(f"- {obs}\n")

    alertas = resultado.get("alertas", [])
    if alertas:
        linhas.append("\n### Alertas\n")
        for al in alertas:
            linhas.append(f"- ⚠️ {al}\n")

    return "\n".join(linhas)


def carregar_contexto_memoria() -> str:
    """Carrega o memoria.json e retorna um resumo do conhecimento registrado."""
    try:
        gerenciador = GerenciadorMemoria()
        gerenciador.carregar()
        conhecimentos = gerenciador.obter_conhecimento()
        if conhecimentos:
            resumo = "### Conhecimento já registrado na memória:\n"
            for item in conhecimentos[-5:]:
                resumo += f"- {json.dumps(item, ensure_ascii=False)}\n"
            return resumo
    except Exception:
        pass
    return ""


def calcular_hash_arquivo(caminho: str) -> str:
    """Calcula o hash SHA-256 de um arquivo."""
    try:
        with open(caminho, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return ""


def main():
    instrucao = os.environ.get("INSTRUCAO", "").strip()

    if not instrucao:
        print(json.dumps({
            "erro": "Nenhuma instrução foi fornecida no campo 'instrucao'.",
            "status": "NAO_EXECUTADO"
        }, ensure_ascii=False, indent=2))
        return

    # --- AUTOVERIFICAÇÃO 1: Verificar se memoria.json existe ---
    caminho_memoria = "memoria.json"
    memoria_existe = os.path.exists(caminho_memoria)
    print(json.dumps({
        "autoverificacao": "1. memoria.json existe",
        "resultado": memoria_existe
    }, ensure_ascii=False))

    # --- AUTOVERIFICAÇÃO 2: Hash antes da execução ---
    hash_antes = calcular_hash_arquivo(caminho_memoria) if memoria_existe else ""
    print(json.dumps({
        "autoverificacao": "2. Hash antes da execução",
        "hash": hash_antes
    }, ensure_ascii=False))

    # --- Injeção do contexto da memória ---
    contexto = carregar_contexto_memoria()
    if contexto:
        instrucao_final = f"{contexto}\n\n### Instrução do usuário:\n{instrucao}"
    else:
        instrucao_final = instrucao

    # --- Execução do agente ---
    agente = AgenteTrabalho()
    resultado = agente.executar(
        tarefa=instrucao_final,
        criterio_conclusao="Responda à instrução fornecida pelo usuário da melhor forma possível, usando as ferramentas disponíveis e o contexto da memória (se houver).",
    )

    # --- AUTOVERIFICAÇÃO 3: Hash depois da execução ---
    hash_depois = calcular_hash_arquivo(caminho_memoria) if memoria_existe else ""
    hash_mudou = hash_antes != hash_depois
    print(json.dumps({
        "autoverificacao": "3. Hash depois da execução",
        "hash": hash_depois,
        "mudou": hash_mudou
    }, ensure_ascii=False))

    # --- AUTOVERIFICAÇÃO 4: Resultado é JSON válido? ---
    resultado_valido = isinstance(resultado, dict) and "status" in resultado
    print(json.dumps({
        "autoverificacao": "4. Resultado é JSON válido",
        "resultado": resultado_valido
    }, ensure_ascii=False))

    # --- Adiciona as autoverificações ao resultado ---
    resultado["autoverificacoes"] = {
        "memoria_existe": memoria_existe,
        "hash_antes": hash_antes,
        "hash_depois": hash_depois,
        "hash_mudou": hash_mudou,
        "resultado_valido": resultado_valido
    }

    # 1. Imprime o JSON completo nos logs
    print(json.dumps(resultado, ensure_ascii=False, indent=2))

    # 2. Gera o resumo no GitHub Step Summary
    caminho_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if caminho_summary:
        try:
            resumo = gerar_resumo_markdown(resultado)
            with open(caminho_summary, "a", encoding="utf-8") as f:
                f.write(resumo)
        except Exception as e:
            print(f"Erro ao gerar Step Summary: {e}")


if __name__ == "__main__":
    main()
