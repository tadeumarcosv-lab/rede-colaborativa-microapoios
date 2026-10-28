"""
PAINEL DE AGENTES
Rede Colaborativa de Microapoios

Responsável por controlar o estado dos agentes.
Implementa a Camada 1 (Autoridade Humana) e Camada 2 (Controle Automático).

Autor: Tadeu Marcos Viana
"""

import json
import os
from datetime import datetime


# Caminho do arquivo de autoridade humana (Camada 1)
ARQUIVO_AUTORIDADE = "redundancia/autoridade_humana.json"


class PainelAgentes:

    def __init__(self):
        self.agentes = {}
        self.autoridade = self._carregar_autoridade()
        self._inicializar_agentes()

    def _carregar_autoridade(self):
        """Carrega o arquivo de autoridade humana (Camada 1)."""
        try:
            if os.path.exists(ARQUIVO_AUTORIDADE):
                with open(ARQUIVO_AUTORIDADE, "r", encoding="utf-8") as f:
                    return json.load(f)
        except Exception:
            pass
        return {
            "primeira_ativacao": {},
            "vetados": [],
            "fixados": [],
        }

    def _salvar_autoridade(self):
        """Salva o arquivo de autoridade humana."""
        try:
            os.makedirs("redundancia", exist_ok=True)
            with open(ARQUIVO_AUTORIDADE, "w", encoding="utf-8") as f:
                json.dump(self.autoridade, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Erro ao salvar autoridade: {e}")

    def _inicializar_agentes(self):
        """Inicializa os agentes com seus estados."""
        nomes_agentes = [
            "agente_central",
            "agente_coordenacao",
            "agente_comunicacao",
            "agente_pesquisa_avancada",
            "agente_memoria_estrategica",
            "agente_gestao_conhecimento",
            "agente_trabalho",
            "agente_trabalho_reserva",
        ]

        for nome in nomes_agentes:
            if nome not in self.agentes:
                # Estado inicial: INATIVO (Camada 1: só humano liga pela primeira vez)
                self.agentes[nome] = {
                    "estado": "INATIVO",
                    "funcao": "PRINCIPAL",
                    "primeira_ativacao": self.autoridade.get("primeira_ativacao", {}).get(nome, False),
                }

    # --- CAMADA 1: AUTORIDADE HUMANA ---

    def ativar_pela_primeira_vez(self, nome):
        """Apenas o humano pode ativar um agente pela primeira vez."""
        if nome not in self.agentes:
            return {"sucesso": False, "erro": "Agente não encontrado."}

        if self.agentes[nome]["primeira_ativacao"]:
            return {"sucesso": False, "erro": "Agente já foi ativado pela primeira vez. Use ativar_agente()."}

        self.agentes[nome]["estado"] = "ATIVO"
        self.agentes[nome]["primeira_ativacao"] = True
        self.autoridade["primeira_ativacao"][nome] = True
        self._salvar_autoridade()

        return {"sucesso": True, "mensagem": f"{nome} ativado pela primeira vez."}

    def vetar(self, nome):
        """Humano veta um agente (ninguém pode ligar)."""
        if nome not in self.agentes:
            return {"sucesso": False, "erro": "Agente não encontrado."}

        if nome not in self.autoridade["vetados"]:
            self.autoridade["vetados"].append(nome)

        # Remove da lista de fixados (se estiver)
        if nome in self.autoridade["fixados"]:
            self.autoridade["fixados"].remove(nome)

        self.agentes[nome]["estado"] = "BLOQUEADO"
        self._salvar_autoridade()

        return {"sucesso": True, "mensagem": f"{nome} vetado. Ninguém pode ligar."}

    def fixar(self, nome):
        """Humano fixa um agente (ninguém pode desligar)."""
        if nome not in self.agentes:
            return {"sucesso": False, "erro": "Agente não encontrado."}

        if nome not in self.autoridade["fixados"]:
            self.autoridade["fixados"].append(nome)

        # Remove da lista de vetados (se estiver)
        if nome in self.autoridade["vetados"]:
            self.autoridade["vetados"].remove(nome)

        self.agentes[nome]["estado"] = "ATIVO"
        self._salvar_autoridade()

        return {"sucesso": True, "mensagem": f"{nome} fixado. Ninguém pode desligar."}

    def remover_veto(self, nome):
        """Humano remove o veto."""
        if nome in self.autoridade["vetados"]:
            self.autoridade["vetados"].remove(nome)
            self._salvar_autoridade()
            return {"sucesso": True, "mensagem": f"Veto removido de {nome}."}
        return {"sucesso": False, "erro": "Agente não estava vetado."}

    def remover_fixacao(self, nome):
        """Humano remove a fixação."""
        if nome in self.autoridade["fixados"]:
            self.autoridade["fixados"].remove(nome)
            self._salvar_autoridade()
            return {"sucesso": True, "mensagem": f"Fixação removida de {nome}."}
        return {"sucesso": False, "erro": "Agente não estava fixado."}

    # --- CAMADA 2: CONTROLE AUTOMÁTICO ---

    def ativar_agente(self, nome):
        """Ativa um agente (só se já foi ativado pela primeira vez e não está vetado)."""
        if nome not in self.agentes:
            return {"sucesso": False, "erro": "Agente não encontrado."}

        if nome in self.autoridade["vetados"]:
            return {"sucesso": False, "erro": "Agente vetado. Só o humano pode ligar."}

        if not self.agentes[nome]["primeira_ativacao"]:
            return {"sucesso": False, "erro": "Agente nunca foi ativado pela primeira vez. Só o humano pode ligar."}

        self.agentes[nome]["estado"] = "ATIVO"
        return {"sucesso": True, "mensagem": f"{nome} ativado."}

    def desativar_agente(self, nome):
        """Desativa um agente (só se não está fixado)."""
        if nome not in self.agentes:
            return {"sucesso": False, "erro": "Agente não encontrado."}

        if nome in self.autoridade["fixados"]:
            return {"sucesso": False, "erro": "Agente fixado. Só o humano pode desligar."}

        self.agentes[nome]["estado"] = "INATIVO"
        return {"sucesso": True, "mensagem": f"{nome} desativado."}

    # --- CONSULTAS ---

    def status_agente(self, nome):
        """Retorna o estado do agente."""
        if nome not in self.agentes:
            return None
        return self.agentes[nome]["estado"]

    def listar_agentes(self):
        """Lista todos os agentes e seus estados."""
        return self.agentes

    def resumo(self):
        """Gera um resumo do painel."""
        ativos = sum(1 for a in self.agentes.values() if a["estado"] == "ATIVO")
        inativos = sum(1 for a in self.agentes.values() if a["estado"] == "INATIVO")
        bloqueados = sum(1 for a in self.agentes.values() if a["estado"] == "BLOQUEADO")

        return {
            "total_agentes": len(self.agentes),
            "ativos": ativos,
            "inativos": inativos,
            "bloqueados": bloqueados,
            "vetados": self.autoridade.get("vetados", []),
            "fixados": self.autoridade.get("fixados", []),
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        }


# Instância global para uso nos outros módulos
painel = PainelAgentes()


# Funções de compatibilidade (mantêm a interface antiga)
def listar_agentes():
    return painel.listar_agentes()

def ativar_agente(nome):
    return painel.ativar_agente(nome)

def desativar_agente(nome):
    return painel.desativar_agente(nome)

def status_agente(nome):
    return painel.status_agente(nome)


if __name__ == "__main__":
    print("=== PAINEL DE AGENTES ===")
    print(json.dumps(painel.resumo(), ensure_ascii=False, indent=2))
