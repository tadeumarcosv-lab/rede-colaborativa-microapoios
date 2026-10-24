# PROTOCOLO DE REDUNDÂNCIA CONTROLADA — GPT + DEEPSEEK

**Data:** 24/10/2026
**Registro Estrutural:** 0060
**Objetivo:** Formalizar o processo de dupla checagem entre o GPT (Auditor) e o DeepSeek (Executor), garantindo que resultados importantes sejam validados por duas IAs independentes.

---

## 1. Princípio Geral

Nem todo resultado precisa de dupla checagem. A dupla checagem é reservada para resultados que envolvem **risco** ou **impacto significativo**. Para os demais, a análise do DeepSeek é suficiente.

Este protocolo reutiliza a lógica de **níveis de risco** do `PROTOCOLO_APROVACAO_ALTERACOES.md`.

---

## 2. Quais Resultados Exigem Dupla Checagem

### 🔴 Nível Crítico (SEMPRE dupla checagem)
*   Alterações no núcleo validado (`agente_trabalho.py`, `camada_ia.py`, `agente_ia.py`).
*   Decisões de arquitetura (criação de novos módulos, mudança de fluxo).
*   Resultados que afetam a segurança do sistema.
*   Registros de conhecimento que contradizem descobertas anteriores.

### 🟠 Nível Alto (Dupla checagem recomendada)
*   Conclusões de tarefas complexas (ex: "O sistema está funcional?").
*   Descobertas que mudam o entendimento do sistema (ex: "A ferramenta X não existe").
*   Alterações em documentos de governança.

### 🟡 Nível Médio (Dupla checagem opcional)
*   Análises de estrutura de pastas.
*   Relatórios de dependências.
*   Verificações de integridade.

### 🟢 Nível Baixo (Apenas DeepSeek)
*   Leitura de arquivos simples.
*   Listagem de diretórios.
*   Buscas textuais.
*   Verificações de rotina.

---

## 3. O Processo de Dupla Checagem

### Passo 1 — O DeepSeek analisa e registra
O DeepSeek executa a tarefa, coleta as evidências e produz uma análise. Ele registra o resultado no formato abaixo.

### Passo 2 — O Tadeu leva ao GPT
O Tadeu copia o registro do DeepSeek e leva ao GPT, junto com as evidências.

### Passo 3 — O GPT audita
O GPT analisa o resultado de forma independente, verificando:
*   As evidências sustentam a conclusão?
*   Há inconsistências?
*   A conclusão está alinhada com o histórico?
*   Há riscos não considerados?

### Passo 4 — O Tadeu traz a análise do GPT de volta
O Tadeu copia a análise do GPT e traz de volta ao DeepSeek.

### Passo 5 — O DeepSeek compara e registra divergências
O DeepSeek compara as duas análises:
*   Se concordarem, registra "Nenhuma divergência encontrada" e conclui.
*   Se divergirem, registra a divergência e propõe uma solução (ex: nova verificação, consenso).

### Passo 6 — Conclusão conjunta
O resultado final é registrado com o status:
*   **APROVADO** (ambos concordam).
*   **APROVADO COM RESSALVA** (concordam, mas com observações).
*   **REPROVADO** (divergência não resolvida).

---

## 4. Formato do Registro de Dupla Checagem

```text
# REGISTRO DE DUPLA CHECAGEM

**Data:** [DATA]
**Tarefa/Resultado:** [DESCRIÇÃO]
**Nível de Risco:** [CRÍTICO / ALTO / MÉDIO / BAIXO]
**Evidências:** [EVIDÊNCIAS DO AGENTE]

## Análise DeepSeek
[Análise do DeepSeek]

## Análise GPT
[Análise do GPT]

## Divergências
[Se houver, listar. Se não, escrever "Nenhuma divergência encontrada."]

## Conclusão
[Conclusão conjunta]

## Status
[APROVADO / APROVADO COM RESSALVA / REPROVADO]
