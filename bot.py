import os
import sqlite3
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

# ================= BANCO (FIXO NO RENDER) =================
DB_PATH = "/tmp/leads.db"

def criar_banco():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            interesse TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_lead(nome, interesse):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (nome, interesse) VALUES (?, ?)", (nome, interesse))
    conn.commit()
    conn.close()

def listar_leads():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, interesse FROM leads")
    dados = cursor.fetchall()
    conn.close()
    return dados

criar_banco()

# ================= TELEGRAM =================
def enviar_mensagem(chat_id, texto):
    requests.post(URL, json={
        "chat_id": chat_id,
        "text": texto
    })

def processar_mensagem(texto, chat_id):
    texto = texto.lower().strip()

    # RESET GLOBAL
    if texto in ["oi", "olá", "ola", "/start"]:
        usuarios[chat_id] = {"estado": "menu"}
        return """👋 Olá! Bem-vindo à Rede de Apoio Financeiro Colaborativo 🤝

Digite o que você quer saber ou escolha:

1 - Como funciona
2 - Quero participar
3 - Dúvidas
"""

    # ================= SUPER INTELIGÊNCIA =================

    respostas = {
        "o que é": "É uma rede de apoio financeiro baseada em microdoações voluntárias via Pix.",
        "como funciona": "Você envia pequenos valores e recebe de outras pessoas. Simples, colaborativo e contínuo.",
        "é golpe": "Não. Não há promessa de lucro nem empresa. É ajuda voluntária.",
        "é seguro": "Sim, pois usa valores baixos e transparência.",
        "é legal": "Sim, são transferências voluntárias entre pessoas.",
        "precisa pagar": "Não. Você só envia se quiser.",
        "tem taxa": "Não existe taxa.",
        "quem pode participar": "Qualquer pessoa com WhatsApp e Pix.",
        "precisa cadastro": "Não precisa cadastro.",
        "tem dono": "Não. É descentralizado.",
        "grupo": "Você cria um grupo no WhatsApp com seu Pix.",
        "pix": "O Pix é usado para enviar pequenos valores.",
        "vale a pena": "Vale para quem busca ajuda mútua simples.",
        "tem risco": "O risco é baixo pois os valores são pequenos.",
        "funciona mesmo": "Funciona com continuidade das pessoas.",
        "posso sair": "Sim, a qualquer momento.",
    }

    for chave in respostas:
        if chave in texto:
            return respostas[chave]

    # ================= FLUXO =================

    if "participar" in texto or texto == "2":
        usuarios[chat_id] = {"estado": "fluxo"}
        return "🤝 Quer entrar agora? (sim/não)"

    if chat_id not in usuarios:
        usuarios[chat_id] = {"estado": "menu"}

    estado = usuarios[chat_id]["estado"]

    if estado == "fluxo":
        if texto == "sim":
            usuarios[chat_id]["estado"] = "nome"
            return "Perfeito! Qual seu nome?"
        elif texto in ["não", "nao"]:
            usuarios[chat_id]["estado"] = "menu"
            return "Tudo bem 😊"
        else:
            return "Responda com sim ou não."

    elif estado == "nome":
        usuarios[chat_id]["nome"] = texto.capitalize()
        usuarios[chat_id]["estado"] = "escolha"
        return f"{usuarios[chat_id]['nome']}, você quer:\n1 - Informações\n2 - Prioridade"

    elif estado == "escolha":
        nome = usuarios[chat_id]["nome"]

        if texto == "1":
            salvar_lead(nome, "informações")
            return "Você será informado 👍"

        elif texto == "2":
            salvar_lead(nome, "prioridade")
            return "Você entrou na prioridade 🚀"

        else:
            return "Digite 1 ou 2."

    return "Digite 2 para participar ou faça uma pergunta."

# ================= WEBHOOK =================
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        resposta = processar_mensagem(texto, chat_id)
        enviar_mensagem(chat_id, resposta)

    return "ok"

# ================= PAINEL =================
@app.route("/leads")
def leads():
    dados = listar_leads()

    if not dados:
        return "Nenhum lead ainda."

    html = "<h2>📊 Leads Capturados</h2>"

    for nome, interesse in dados:
        html += f"<p>👤 Nome: {nome}<br>🔥 Interesse: {interesse}</p>"

    return html

# ================= HOME =================
@app.route("/")
def home():
    return "SISTEMA 100% ATIVO 🚀"

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
