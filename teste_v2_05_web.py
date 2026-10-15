"""
TESTE 5 — AGENTE DE TRABALHO V2

Objetivo:
Validar a capacidade do AgenteTrabalho V2 de utilizar a ferramenta
pesquisar_web para obter informações reais na Web.

O teste deve verificar:
- uso real da ferramenta pesquisar_web;
- realização de pesquisa na Web;
- obtenção de resultados reais;
- conclusão baseada nos resultados obtidos;
- ausência de resultados inventados.

Registro estrutural de referência: 0122
"""

import json

from agente_trabalho import AgenteTrabalho


def main():
    agente = AgenteTrabalho()

    resultado = agente.executar(
        tarefa=(
            "Pesquise na Web o texto 'Python 3.11 release date' "
            "e informe os resultados encontrados, identificando "
            "as fontes ou páginas retornadas pela pesquisa."
        ),
        criterio_conclusao=(
            "A ferramenta pesquisar_web deve ser utilizada para "
            "realizar a pesquisa. A resposta deve informar somente "
            "resultados realmente obtidos pela ferramenta, "
            "identificando as fontes ou páginas encontradas. "
            "Não invente resultados nem fontes."
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
