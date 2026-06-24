from gerenciador_ocorrencias import (
    GerenciadorOcorrencias
)

from agente_arquiteto import (
    AgenteArquiteto
)


class AgenteEvolucao:

    def __init__(self):
        self.ocorrencias = (
            GerenciadorOcorrencias()
        )

        self.arquiteto = (
            AgenteArquiteto()
        )

    def analisar_evolucao(self):

        plano = (
            self.arquiteto.gerar_plano()
        )

        melhorias = []

        for sugestao in plano["sugestoes"]:

            melhorias.append(
                f"Melhoria aprovada: {sugestao}"
            )

        return melhorias

    def gerar_plano_evolucao(self):

        melhorias = (
            self.analisar_evolucao()
        )

        plano = {
            "melhorias": melhorias,
            "quantidade": len(melhorias)
        }

        self.ocorrencias.registrar(
            "EVOLUCAO",
            "Plano de evolução gerado"
        )

        return plano


if __name__ == "__main__":

    evolucao = (
        AgenteEvolucao()
    )

    print(
        evolucao.gerar_plano_evolucao()
)
