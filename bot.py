import os
import sqlite3
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

# ================= BANCO =================
def criar_banco():
    conn = sqlite3.connect("leads.db")
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
    conn = sqlite3.connect("leads.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leads (nome, interesse) VALUES (?, ?)", (nome, interesse))
    conn.commit()
    conn.close()

def listar_leads():
    conn = sqlite3.connect("leads.db")
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

    # 🔁 RESET GLOBAL
    if texto in ["oi", "olá", "ola", "/start"]:
        usuarios[chat_id] = {"estado": "menu"}
        return """👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝

1 - Como funciona
2 - Participar
3 - Informações"""

    # 🔥 INTELIGÊNCIA GLOBAL (funciona em qualquer momento)
    if "participar" in texto:
        usuarios[chat_id] = {"estado": "fluxo"}
        return "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)"

    if "funciona" in texto:
        usuarios[chat_id] = {"estado": "fluxo"}
        return "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro colaborativo.\n\nDeseja participar? (sim/não)"

    if chat_id not in usuarios:
        usuarios[chat_id] = {"estado": "menu"}

    estado = usuarios[chat_id]["estado"]

    # MENU
    if estado == "menu":
        if texto == "1":
            usuarios[chat_id]["estado"] = "fluxo"
            return "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro colaborativo.\n\nDeseja participar? (sim/não)"

        elif texto == "2":
            usuarios[chat_id]["estado"] = "fluxo"
            return "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)"

        elif texto == "3":
            return "ℹ️ Mais informações em breve."

        else:
            return "Escolha 1, 2 ou 3."

    # FLUXO
    elif estado == "fluxo":
        if texto == "sim":
            usuarios[chat_id]["estado"] = "nome"
            return "Perfeito! 🙌\n\nPara continuar, me diga seu nome:"
        elif texto == "não" or texto == "nao":
            usuarios[chat_id]["estado"] = "menu"
            return "Tudo bem 😊\n\nDigite 1, 2 ou 3."
        else:
            return "Responda com 'sim' ou 'não'."

    # NOME
    elif estado == "nome":
        usuarios[chat_id]["nome"] = texto.capitalize()
        usuarios[chat_id]["estado"] = "escolha"

        return f"Ótimo, {usuarios[chat_id]['nome']}! 👏\n\nVocê quer:\n1 - Receber informações\n2 - Entrar assim que abrir\n\nDigite 1 ou 2:"

    # ESCOLHA FINAL
    elif estado == "escolha":
        nome = usuarios[chat_id]["nome"]

        if texto == "1":
            salvar_lead(nome, "informações")
            usuarios[chat_id]["estado"] = "menu"
            return f"Perfeito, {nome}! 📩 Você receberá mais informações.\n\nDigite 'oi' para recomeçar."

        elif texto == "2":
            salvar_lead(nome, "prioridade")
            usuarios[chat_id]["estado"] = "menu"
            return f"Excelente, {nome}! 🚀\nVocê está na lista de prioridade.\n\nDigite 'oi' para recomeçar."

        else:
            return "Digite 1 ou 2."

    return "Digite 'oi' para começar."

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

# ================= PAINEL WEB =================
@app.route("/leads")
def ver_leads():
    dados = listar_leads()

    if not dados:
        return "Nenhum lead ainda."

    html = "<h2>📊 Leads capturados:</h2>"

    for nome, interesse in dados:
        html += f"<p>👤 {nome} - {interesse}</p>"

    return html

# ================= HOME =================
@app.route("/")
def home():
    return "Bot online 🚀"

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
