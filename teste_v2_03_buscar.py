"""
TESTE 3 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de utilizar a ferramenta
buscar_texto para localizar ocorrências reais de um texto no
repositório.

Registro estrutural de referência: 0117
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Procure no repositório todas as ocorrências do texto "
            "MAX_ITERACOES e informe quais arquivos e linhas "
            "contêm esse texto."
        ),
        criterio_conclusao=(
            "A ferramenta buscar_texto deve ser utilizada para "
            "pesquisar o texto MAX_ITERACOES. A resposta deve "
            "apresentar somente ocorrências realmente encontradas "
            "pela ferramenta, identificando arquivo e número da linha, "
            "sem inventar resultados."
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
