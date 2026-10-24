# BIBLIOTECA DE TAREFAS PADRONIZADAS — AGENTE V2

**Data:** 24/10/2026
**Registro Estrutural:** 0056
**Objetivo:** Fornecer prompts prontos para copiar e colar na interface do agente, evitando retrabalho e padronizando as instruções.

**Como usar:** Copie o prompt desejado, cole no campo de instrução do workflow "Conversar com Agente" e execute.

---

## 1. Ler Arquivo

Objetivo: Ler o conteúdo de um arquivo do repositório.

Prompt:
Leia o arquivo [NOME_DO_ARQUIVO] e me mostre o conteúdo completo.

Exemplo:
Leia o arquivo agente_ia.py e me mostre o conteúdo completo.

---

## 2. Listar Arquivos

Objetivo: Listar os arquivos de um diretório.

Prompt:
Liste os arquivos do diretório [DIRETORIO] e me mostre a lista completa.

Exemplo:
Liste os arquivos do diretório docs/ e me mostre a lista completa.

---

## 3. Buscar Texto

Objetivo: Procurar um termo em um arquivo ou diretório.

Prompt:
Use a ferramenta buscar_texto para procurar o termo "[TERMO]" no arquivo [NOME_DO_ARQUIVO]. Me mostre as linhas onde o termo aparece.

Exemplo:
Use a ferramenta buscar_texto para procurar o termo "registrar_conhecimento" no arquivo agente_trabalho.py. Me mostre as linhas onde o termo aparece.

---

## 4. Extrair Metadados

Objetivo: Extrair informações estruturais de um arquivo .py.

Prompt:
Use a ferramenta extrair_metadados no arquivo [NOME_DO_ARQUIVO] e me mostre a lista de funções e classes definidas nele.

Exemplo:
Use a ferramenta extrair_metadados no arquivo agente_trabalho.py e me mostre a lista de funções e classes definidas nele.

---

## 5. Registrar Conhecimento

Objetivo: Registrar uma descoberta na memória persistente.

Prompt:
Use a ferramenta registrar_conhecimento para registrar a seguinte informação: categoria="[CATEGORIA]", dado={"descricao": "[DESCRICAO]"}, status="[STATUS]", confianca="[CONFIANCA]", evidencias=[EVIDENCIAS].

Exemplo:
Use a ferramenta registrar_conhecimento para registrar a seguinte informação: categoria="teste_fase_4", dado={"descricao": "Teste de registro da Fase 4"}, status="fato_verificado", confianca="alta", evidencias=["E001"].

---

## 6. Consultar Memória

Objetivo: Verificar se um conhecimento já foi registrado.

Prompt:
Leia o arquivo memoria.json e me diga se existe a categoria "[CATEGORIA]". Se existir, me mostre o conteúdo registrado.

Exemplo:
Leia o arquivo memoria.json e me diga se existe a categoria "teste_fase_3_persistencia_final". Se existir, me mostre o conteúdo registrado.

---

## 7. Verificar Estrutura (Funções e Classes)

Objetivo: Verificar se uma função ou classe existe em um arquivo .py.

Prompt:
Use a ferramenta extrair_metadados no arquivo [NOME_DO_ARQUIVO] e me diga se existe a função "[NOME_DA_FUNCAO]". Se existir, me mostre a assinatura dela.

Exemplo:
Use a ferramenta extrair_metadados no arquivo agente_trabalho.py e me diga se existe a função "registrar_conhecimento". Se existir, me mostre a assinatura dela.

---

## 8. Comparar Documentação × Código (Fase 6 - Autoverificação)

Objetivo: Verificar se a documentação corresponde ao código.

Prompt:
Leia o arquivo [DOCUMENTO.md] e me diga se ele menciona a função "[NOME_DA_FUNCAO]". Depois, leia o arquivo [CODIGO.py] e me diga se a função realmente existe.

Exemplo:
Leia o arquivo docs/VALIDACAO_V2_AGENTE_TRABALHO.md e me diga se ele menciona a função "registrar_conhecimento". Depois, leia o arquivo agente_trabalho.py e me diga se a função realmente existe.

---

## 9. Verificar Hash de Arquivo

Objetivo: Verificar se um arquivo mudou desde a última leitura.

Prompt:
Leia o arquivo [NOME_DO_ARQUIVO] e me diga o hash SHA-256 do conteúdo. Depois, compare com o hash registrado na memória (se existir) e me diga se o arquivo mudou.

Exemplo:
Leia o arquivo agente_trabalho.py e me diga o hash SHA-256 do conteúdo. Depois, compare com o hash registrado na memória (se existir) e me diga se o arquivo mudou.

---

## 10. Verificar Dependências

Objetivo: Verificar quais arquivos importam um determinado módulo.

Prompt:
Use a ferramenta buscar_texto para procurar o termo "import [NOME_DO_MODULO]" em todos os arquivos .py do repositório. Me diga em quais arquivos ele aparece.

Exemplo:
Use a ferramenta buscar_texto para procurar o termo "import gerenciador_memoria" em todos os arquivos .py do repositório. Me diga em quais arquivos ele aparece.

---

## 11. Verificar se Função é Usada

Objetivo: Verificar se uma função é realmente usada no código.

Prompt:
Use a ferramenta buscar_texto para procurar o termo "[NOME_DA_FUNCAO]" em todos os arquivos .py do repositório. Me diga em quais arquivos e linhas ele aparece. Depois, me diga se a função é usada ou se é órfã.

Exemplo:
Use a ferramenta buscar_texto para procurar o termo "registrar_conhecimento" em todos os arquivos .py do repositório. Me diga em quais arquivos e linhas ele aparece. Depois, me diga se a função é usada ou se é órfã.

---

## 12. Gerar Relatório de Estrutura

Objetivo: Gerar um relatório com a estrutura de uma pasta.

Prompt:
Liste os arquivos da pasta "[DIRETORIO]" e, para cada arquivo .py, use a ferramenta extrair_metadados para listar as funções e classes. No final, me mostre um resumo.

Exemplo:
Liste os arquivos da pasta "nucleo_operacional" e, para cada arquivo .py, use a ferramenta extrair_metadados para listar as funções e classes. No final, me mostre um resumo.

---

## 13. Verificar Workflow

Objetivo: Verificar se um workflow existe e o que ele faz.

Prompt:
Leia o arquivo .github/workflows/[NOME_DO_WORKFLOW].yml e me diga qual é o nome do workflow, o gatilho (on) e os passos (steps) que ele executa.

Exemplo:
Leia o arquivo .github/workflows/conversar_com_agente.yml e me diga qual é o nome do workflow, o gatilho (on) e os passos (steps) que ele executa.

---

## 14. Verificar Memória

Objetivo: Verificar o estado geral da memória.

Prompt:
Leia o arquivo memoria.json e me diga quantos itens existem em cada categoria (historico, aprendizados, decisoes, conhecimento, contexto).

Exemplo:
Leia o arquivo memoria.json e me diga quantos itens existem em cada categoria (historico, aprendizados, decisoes, conhecimento, contexto).

---

## 15. Verificar Integridade

Objetivo: Verificar se um arquivo .py tem sintaxe válida.

Prompt:
Use a ferramenta extrair_metadados no arquivo [NOME_DO_ARQUIVO] e me diga se a sintaxe Python é válida. Se não for, me mostre o erro.

Exemplo:
Use a ferramenta extrair_metadados no arquivo agente_trabalho.py e me diga se a sintaxe Python é válida. Se não for, me mostre o erro.

---

## Referências Cruzadas

Localização: docs/BIBLIOTECA_TAREFAS.md
Estrutura responsável: Documentação / Núcleo Operacional
Documentos relacionados: INDICE_DOCUMENTOS.md, SYSTEM_INDEX.md, PLANO_MESTRE.md

---

## Princípio Final

"Informação organizada gera conhecimento. Conhecimento rastreável gera continuidade. Continuidade preservada reduz perdas, aumenta eficiência e fortalece a evolução sustentável do sistema."
