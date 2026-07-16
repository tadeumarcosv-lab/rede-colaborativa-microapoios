    def listar_componentes(self):
        """
        Retorna a lista oficial de componentes supervisionados
        pelo Diretor Autônomo da Rede.
        """

        return self.componentes

    def adicionar_componente(self, componente):
        """
        Registra um novo componente sob supervisão do Diretor
        Autônomo.
        """

        if componente not in self.componentes:

            self.componentes.append(componente)

            self.registrar(f"Novo componente supervisionado: {componente}")
