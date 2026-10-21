import json
import os

from agente_trabalho import AgenteTrabalho


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

    print(json.dumps(resultado, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
