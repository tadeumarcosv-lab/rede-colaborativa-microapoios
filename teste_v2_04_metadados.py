"""
TESTE 4 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de utilizar a ferramenta
extrair_metadados para obter informações objetivas de um arquivo
existente no repositório.

O teste deve verificar:
- uso real da ferramenta extrair_metadados;
- identificação do arquivo solicitado;
- obtenção de metadados objetivos;
- conclusão com evidência;
- ausência de resultados inventados.

Registro estrutural de referência: 0121
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Extraia os metadados do arquivo agente_ia.py "
            "que está na raiz do repositório. Informe o nome "
            "do arquivo, a extensão e o tamanho em bytes."
        ),
        criterio_conclusao=(
            "A ferramenta extrair_metadados deve ser utilizada "
            "diretamente no arquivo agente_ia.py. "
            "A resposta deve informar somente dados realmente "
            "obtidos pela ferramenta, incluindo nome do arquivo, "
            "extensão e tamanho em bytes. "
            "Não invente nenhum valor."
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
