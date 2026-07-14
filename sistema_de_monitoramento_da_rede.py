    def verificar_componentes(self):
        """
        Verifica os componentes atualmente registrados.

        Retorna uma lista com os componentes monitorados.
        Esta interface é utilizada pelo Motor de Aprendizado.
        """

        print("[MONITORAMENTO] Verificando componentes da Rede...")

        if hasattr(self, "componentes"):
            return self.componentes

        return []
