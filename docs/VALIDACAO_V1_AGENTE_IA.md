# VALIDAÇÃO V1 — PRIMEIRO AGENTE DE IA

🔢 Registro estrutural: 0289

**Data da validação:** 07/10/2026

**Status:** VALIDADO NOS CAMINHOS TESTADOS

**Versão do AgenteIA:** 0.1.0

**Versão da CamadaIA:** 0.1.0

**Provedor operacional:** Groq

**Modelo utilizado:** `openai/gpt-oss-20b`

**Ambiente do agente:** `dev`

---

## 1. OBJETIVO DO REGISTRO

Este documento registra formalmente a primeira validação real do núcleo inicial de Inteligência Artificial da Rede Colaborativa de Microapoios.

A validação teve como objetivo verificar, de forma controlada e observável, se os componentes:

- `agente_ia.py`
- `camada_ia.py`
- `gerenciador_memoria.py`
- `registro_central_eventos.py`

conseguem executar o caminho mínimo definido para a V1:

**solicitação → AgenteIA → CamadaIA → provedor de IA → resposta → verificação → memória → evento → evidência**

O teste foi realizado por meio do laboratório permanente:

`teste_agente_ia.py`

e executado pelo workflow manual:

`.github/workflows/teste_v1_manual.yml`

---

## 2. MÉTODO DE EXECUÇÃO

A execução foi realizada pelo GitHub Actions por meio de execução manual do workflow:

**Teste V1 - Agente de IA**

O workflow executou:

1. checkout do repositório;
2. preparação do Python;
3. verificação da estrutura mínima;
4. verificação da versão do Python;
5. instalação das dependências;
6. verificação da dependência `requests`;
7. verificação da sintaxe dos arquivos V1;
8. verificação da presença do segredo `GROQ_API_KEY`;
9. verificação da configuração do modelo;
10. confirmação do modo padrão do laboratório;
11. execução do laboratório permanente;
12. diagnóstico final da execução.

O workflow foi configurado para execução manual e realizou somente uma chamada real ao provedor no modo padrão.

---

## 3. IDENTIFICAÇÃO DA EXECUÇÃO

**Workflow:** `Teste V1 - Agente de IA`

**Execução:** `#1`

**Commit testado:** `89cd6e615a1e5feca9418e7820cc21174a2dd60e`

**Branch:** `main`

**Resultado do GitHub Actions:** `Success`

**Duração aproximada do job:** 9 segundos

---

## 4. RESULTADO GERAL DO LABORATÓRIO

O laboratório apresentou:

- **83 verificações realizadas**
- **83 verificações aprovadas**
- **0 verificações reprovadas**

Resultado registrado pelo próprio laboratório:

**TODAS AS VERIFICAÇÕES REALIZADAS FORAM APROVADAS**

Esse resultado deve ser interpretado como validação dos componentes e caminhos efetivamente testados, e não como validação integral de todo o sistema da Rede.

---

## 5. TESTES DE ESTRUTURA

Foram aprovados:

- instanciamento do `AgenteIA`;
- status do `AgenteIA`;
- versão `0.1.0`;
- disponibilidade de `AgenteIA.executar`;
- conexão com `CamadaIA`;
- instanciamento da `CamadaIA`;
- status da `CamadaIA`;
- versão `0.1.0`;
- provedor definido como `groq`;
- disponibilidade de `CamadaIA.consultar`;
- endpoint da Groq;
- timeout definido em 30 segundos.

Resultado: **APROVADO**

---

## 6. TESTES DE ENTRADA E CONTROLE

Foram testadas entradas inválidas e vazias.

### Entrada não-string

Resultado: `FALHA`

O comportamento foi considerado correto porque a entrada inválida foi rejeitada de forma controlada.

### Entrada vazia

Resultado: `FALHA`

O comportamento foi considerado correto porque a solicitação vazia foi rejeitada de forma controlada.

Também foi comprovada a geração de `task_id`.

Resultado geral: **APROVADO**

---

## 7. IDENTIFICAÇÃO E EVIDÊNCIA DA TAREFA

Foi comprovado que a tarefa possui:

- `task_id`;
- UUID v4;
- versão do agente;
- versão da camada;
- ambiente;
- solicitação original;
- objetivo;
- status;
- etapa atual;
- início;
- última atividade;
- duração;
- resultado;
- verificação;
- evidência.

Também foi comprovada a utilização de SHA-256 para a solicitação.

Resultado: **APROVADO**

---

## 8. VALIDAÇÃO LOCAL DA CAMADA DE IA

Foi testada a validação local de prompt vazio.

Resultado:

- falha controlada;
- erro informado;
- provedor identificado;
- nenhuma chamada externa realizada durante essa validação local.

Resultado: **APROVADO**

---

## 9. SEGURANÇA BÁSICA

O laboratório verificou:

- nome conhecido da variável de ambiente da chave;
- presença da `GROQ_API_KEY` no ambiente;
- ausência da impressão do valor da chave.

A chave secreta não foi registrada no documento nem exposta no log.

Resultado: **APROVADO**

---

## 10. EXECUÇÃO REAL COM A GROQ

Foi realizada uma única chamada real ao provedor.

### Solicitação utilizada

> Qual e a capital do Brasil? Responda somente com a cidade e o estado.

### Resultado

**Brasília, Distrito Federal**

### Dados da execução

**Task ID:** `0415fc52-89fa-4a55-86e7-b8c080e78e01`

**Status:** `CONCLUIDA`

**Provedor:** `groq`

**Modelo:** `openai/gpt-oss-20b`

**Tempo da chamada:** `556 ms`

**Duração total da tarefa:** `557 ms`

**Tentativas:** `1`

### Verificações

`resposta_nao_vazia = true`

`provedor_identificado = true`

`chamada_provedor_sucesso = true`

Resultado: **APROVADO**

---

## 11. EVIDÊNCIAS CRIPTOGRÁFICAS

A execução produziu hash SHA-256 da solicitação:

`77278e048081a78b45a6e75533f8343ca01308be919855d98da2bf90f317abed`

Hash SHA-256 da resposta:

`0bd12d8cd5373d288162865f81e48c8b418ba10b8325746001466857260bdbd6`

Foi comprovado que:

- o hash da solicitação possui formato esperado;
- o hash da resposta possui formato esperado;
- o hash da resposta confere;
- a origem da evidência foi registrada como `groq_api`;
- o timestamp da resposta foi registrado.

Resultado: **APROVADO**

---

## 12. MEMÓRIA PERSISTENTE

Foi verificado o caminho de persistência da execução.

O laboratório comprovou:

- histórico retornado como lista;
- tarefa real encontrada no histórico;
- `task_id` correspondente localizado;
- estatísticas retornadas como dicionário;
- contador de solicitações válido.

Contador observado durante a validação: `8`

Resultado: **APROVADO**

Observação: O contador representa o estado da memória no ambiente utilizado durante o teste e não deve ser interpretado isoladamente como quantidade total histórica do projeto.

---

## 13. REGISTRO CENTRAL DE EVENTOS

Foi comprovada a existência de evento originado pelo `AgenteIA`.

Também foi localizado evento correspondente ao mesmo:

`task_id = 0415fc52-89fa-4a55-86e7-b8c080e78e01`

Foram encontrados os campos:

- `origem`;
- `destino`;
- `responsavel`;
- `descricao`;
- `resultado`;
- `importancia`.

Resultado: **APROVADO**

---

## 14. CADEIA FUNCIONAL COMPROVADA

A primeira execução real comprovou o seguinte caminho:

```text
SOLICITAÇÃO
↓
AgenteIA
↓
CamadaIA
↓
Groq API
↓
Modelo openai/gpt-oss-20b
↓
RESPOSTA
↓
VERIFICAÇÃO
↓
MEMÓRIA PERSISTENTE
↓
REGISTRO CENTRAL DE EVENTOS
↓
EVIDÊNCIAS
