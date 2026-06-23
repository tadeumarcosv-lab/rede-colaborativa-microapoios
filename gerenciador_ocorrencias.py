HISTORICO_SISTEMA = []

class GerenciadorOcorrencias:

    def registrar(self, tipo, mensagem):

        ocorrencia = {
            "tipo": tipo,
            "mensagem": mensagem
        }

        HISTORICO_SISTEMA.append(ocorrencia)

        return ocorrencia

    def listar(self):

        return HISTORICO_SISTEMA

    def quantidade(self):

        return len(HISTORICO_SISTEMA)


if __name__ == "__main__":

    gestor = GerenciadorOcorrencias()

    gestor.registrar(
        "TESTE",
        "Primeira ocorrência registrada"
    )

    print(gestor.listar())
