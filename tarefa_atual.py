import json
import os

from agente_trabalho import AgenteTrabalho


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


def main():
    instrucao = os.environ.get("INSTRUCAO", "").strip()

    if not instrucao:
        print(json.dumps({
            "erro": "Nenhuma instrução foi fornecida no campo 'instrucao'.",
            "status": "NAO_EXECUTADO"
        }, ensure_ascii=False, indent=2))
        return

    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=instrucao,
        criterio_conclusao="Responda à instrução fornecida pelo usuário da melhor forma possível, usando as ferramentas disponíveis.",
    )

    # 1. Imprime o JSON completo nos logs (comportamento anterior)
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
