from gerenciador_ocorrencias import GerenciadorOcorrencias


class AgenteReparador:

    def __init__(self):

        self.ocorrencias = GerenciadorOcorrencias()

    def analisar_problema(self, agente, problema):

        registro = self.ocorrencias.registrar(
            "REPARO",
            f"Problema detectado em {agente}: {problema}"
        )

        return {
            "agente": agente,
            "problema": problema,
            "status": "registrado"
        }

    def preparar_reparo(self, agente):

        return f"Plano de reparo preparado para {agente}"


if __name__ == "__main__":

    reparador = AgenteReparador()

    print(
        reparador.analisar_problema(
            "pesquisa_avancada",
            "agente indisponivel"
        )
    )

    print(
        reparador.preparar_reparo(
            "pesquisa_avancada"
        )
  )
