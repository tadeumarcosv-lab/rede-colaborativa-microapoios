    def obter_componentes(self):
        """
        Retorna a lista oficial de tipos de componentes que podem
        ser gerados pelo Gerador Autônomo.
        """

        return self.componentes

    def adicionar_componente(self, componente):
        """
        Registra um novo tipo de componente disponível para
        geração automática.
        """

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.registrar(
                f"Novo tipo de componente registrado: {componente}"
            )
