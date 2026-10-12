"""
TESTE 2 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de utilizar a ferramenta
listar_arquivos para identificar os arquivos .py existentes
diretamente na raiz do repositório.

Registro estrutural de referência: 0110
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Liste todos os arquivos .py que existem diretamente "
            "na raiz do repositório e informe quantos são."
        ),
        criterio_conclusao=(
            "A ferramenta listar_arquivos deve ser utilizada com "
            "o diretório raiz '.'. O resultado deve identificar "
            "os arquivos .py que estão diretamente na raiz, "
            "sem incluir arquivos dentro de subdiretórios, e "
            "informar a quantidade total encontrada."
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
