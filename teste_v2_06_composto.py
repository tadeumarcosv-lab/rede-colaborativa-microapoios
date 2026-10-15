"""
TESTE 6 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de executar uma tarefa
composta utilizando mais de uma ferramenta e reunir as evidências
obtidas em uma única conclusão.

A tarefa deve utilizar:
- ler_arquivo;
- extrair_metadados;
- buscar_texto.

O teste não deve modificar nenhum arquivo do repositório.

Registro estrutural de referência: 0123
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Faça uma análise composta do arquivo agente_ia.py, "
            "que está na raiz do repositório. "
            "Primeiro leia o arquivo. "
            "Depois extraia seus metadados. "
            "Por fim, pesquise no repositório o texto 'class AgenteIA'. "
            "Informe, na conclusão, o nome do arquivo analisado, "
            "a quantidade de linhas, o tamanho em bytes e as "
            "ocorrências encontradas para 'class AgenteIA', "
            "identificando arquivo e linha quando houver."
        ),
        criterio_conclusao=(
            "A tarefa somente deve ser considerada concluída se "
            "forem utilizadas as ferramentas ler_arquivo, "
            "extrair_metadados e buscar_texto. "
            "A conclusão deve reunir somente informações obtidas "
            "pelas ferramentas, sem inventar valores ou ocorrências. "
            "As evidências devem permitir verificar a origem dos dados. "
            "Se alguma ferramenta falhar, informe a falha e não "
            "apresente como confirmado nenhum dado que não tenha "
            "sido verificado."
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
