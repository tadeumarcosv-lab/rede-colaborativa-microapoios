from flask import Flask, request
import requests

app = Flask(__name__)

# 🔥 COLE SEU TOKEN AQUI (ENTRE ASPAS)
TOKEN = "SEU_TOKEN_AQUI"

usuarios = {}
leads = []

# 📩 ENVIAR MENSAGEM
def enviar_mensagem(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

# 🤖 PROCESSAMENTO
def processar_mensagem(chat_id, texto):
    estado = usuarios.get(chat_id, "inicio")

    if texto == "/start":
        usuarios[chat_id] = "inicio"
        enviar_mensagem(chat_id, "Olá 👋\n\nDigite:\n👉 Quero participar\n👉 Como funciona")
        return

    if "como funciona" in texto.lower():
        enviar_mensagem(chat_id, "Funciona com ajuda entre pessoas com pequenos valores.")
        return

    if "quero participar" in texto.lower():
        usuarios[chat_id] = "nome"
        enviar_mensagem(chat_id, "Qual seu nome?")
        return

    if estado == "nome":
        usuarios[chat_id] = {"etapa": "interesse", "nome": texto}
        enviar_mensagem(chat_id, "Escolha:\n1 - Curiosidade\n2 - Renda extra")
        return

    if isinstance(estado, dict):
        nome = estado["nome"]

        if texto == "1":
            interesse = "curiosidade"
        elif texto == "2":
            interesse = "renda extra"
        else:
            enviar_mensagem(chat_id, "Digite 1 ou 2")
            return

        leads.append({
            "nome": nome,
            "interesse": interesse
        })

        usuarios[chat_id] = "fim"

        enviar_mensagem(chat_id, f"Pronto {nome}! ✅\nVocê entrou como: {interesse}")
        return

# 🌐 HOME
@app.route("/")
def home():
    return "BOT SIMPLES ATIVO 🚀"

# 📊 VER LEADS
@app.route("/leads")
def ver_leads():
    html = "<h2>📊 Leads Capturados</h2>"

    if not leads:
        return html + "<p>Nenhum lead ainda.</p>"

    for lead in leads:
        html += f"<p>👤 {lead['nome']}<br>🔥 {lead['interesse']}</p><hr>"

    return html

# 🚀 WEBHOOK (SEM TRAVAR)
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        processar_mensagem(chat_id, texto)

    return "ok"
