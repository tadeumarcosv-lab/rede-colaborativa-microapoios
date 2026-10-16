"""
TESTE 6 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de executar uma tarefa
composta utilizando três ferramentas diferentes e concluir a tarefa
assim que as evidências necessárias forem obtidas.

Ferramentas exigidas:
- ler_arquivo;
- extrair_metadados;
- buscar_texto.

Cada ferramenta deve ser utilizada uma única vez.

O teste não deve modificar nenhum arquivo do repositório.

Registro estrutural de referência: 0123
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Execute uma tarefa composta sobre o arquivo agente_ia.py "
            "na raiz do repositório. "
            "Use exatamente uma vez a ferramenta ler_arquivo para "
            "verificar o arquivo. "
            "Use exatamente uma vez a ferramenta extrair_metadados "
            "para obter o tamanho em bytes e a quantidade de linhas. "
            "Use exatamente uma vez a ferramenta buscar_texto para "
            "procurar o texto 'class AgenteIA'. "
            "Depois das três ferramentas fornecerem seus resultados, "
            "conclua imediatamente a tarefa. "
            "Não repita nenhuma ferramenta e não faça novas pesquisas."
        ),
        criterio_conclusao=(
            "A tarefa somente deve ser considerada concluída se "
            "ler_arquivo, extrair_metadados e buscar_texto tiverem "
            "sido utilizadas uma vez cada. "
            "Depois das três evidências, produza imediatamente a "
            "conclusão final. "
            "Informe somente dados realmente obtidos pelas ferramentas. "
            "Não invente valores, ocorrências ou fontes. "
            "Não repita chamadas de ferramentas depois de obter "
            "as três evidências necessárias."
        ),
    )

    print(
        json.dumps(
            resultado,
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
