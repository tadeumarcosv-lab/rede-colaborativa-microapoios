from flask import Flask, request
import requests

app = Flask(__name__)

# 🔥 COLE SEU TOKEN AQUI
TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"

usuarios = {}
leads = []

def enviar(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": texto})

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/leads")
def ver_leads():
    html = "<h2>📊 Leads Capturados</h2>"

    if not leads:
        return html + "<p>Nenhum lead ainda.</p>"

    for l in leads:
        html += f"<p>👤 {l['nome']}<br>🔥 {l['interesse']}</p><hr>"

    return html

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    texto = data["message"].get("text", "").lower()

    estado = usuarios.get(chat_id)

    # INÍCIO
    if texto == "/start":
        usuarios[chat_id] = "inicio"
        enviar(chat_id, "Olá 👋\nDigite:\n👉 Quero participar")
        return "ok"

    # ENTRAR
    if "participar" in texto:
        usuarios[chat_id] = "nome"
        enviar(chat_id, "Qual seu nome?")
        return "ok"

    # NOME
    if estado == "nome":
        usuarios[chat_id] = {"etapa": "interesse", "nome": texto}
        enviar(chat_id, "Escolha:\n1 - Curiosidade\n2 - Renda extra")
        return "ok"

    # INTERESSE
    if isinstance(estado, dict):
        nome = estado["nome"]

        if texto == "1":
            interesse = "curiosidade"
        elif texto == "2":
            interesse = "renda extra"
        else:
            enviar(chat_id, "Digite 1 ou 2")
            return "ok"

        leads.append({
            "nome": nome,
            "interesse": interesse
        })

        usuarios[chat_id] = "fim"

        enviar(chat_id, f"Pronto {nome}! ✅\nInteresse: {interesse}")
        return "ok"

    return "ok"
