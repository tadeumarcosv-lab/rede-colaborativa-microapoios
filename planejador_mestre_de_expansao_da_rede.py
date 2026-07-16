    def listar_fontes(self):
        """
        Retorna a lista oficial de fontes utilizadas pelo
        Planejador Mestre de Expansão.
        """

        return self.fontes

    def adicionar_fonte(self, fonte):
        """
        Registra uma nova fonte oficial para utilização
        no planejamento da Rede.
        """

        if fonte not in self.fontes:

            self.fontes.append(fonte)

            self.registrar(f"Nova fonte registrada: {fonte}")
