from flask import Flask, request
import requests

app = Flask(__name__)

# 🔥 COLOQUE SEU TOKEN AQUI
TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"

# 🧠 MEMÓRIA TEMPORÁRIA
usuarios = {}
leads = []

# 🤖 RESPOSTAS AUTOMÁTICAS
def responder_inteligente(texto):
    texto = texto.lower()

    if "seguro" in texto or "golpe" in texto:
        return "Fica tranquilo. Aqui não existe promessa de lucro. É apenas colaboração voluntária."

    if "como funciona" in texto:
        return "Funciona assim: pessoas ajudam outras com pequenos valores. Simples e direto."

    if "quem pode participar" in texto:
        return "Qualquer pessoa pode participar."

    return None


@app.route("/")
def home():
    return "CAPTURA DE LEADS ATIVA 🚀"


@app.route("/leads")
def ver_leads():
    html = "<h2>📊 Leads Capturados</h2>"

    if not leads:
        return html + "<p>Nenhum lead ainda.</p>"

    for lead in leads:
        html += f"<p>👤 {lead['nome']}<br>🔥 {lead['interesse']}</p><hr>"

    return html


def enviar_mensagem(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    texto = data["message"].get("text", "")

    # 🔁 ESTADO DO USUÁRIO
    estado = usuarios.get(chat_id, "inicio")

    # 🔹 INÍCIO
    if texto == "/start":
        usuarios[chat_id] = "inicio"
        enviar_mensagem(chat_id, "Olá 👋\n\nDigite:\n👉 Quero participar\n👉 Como funciona")
        return "ok"

    # 🔹 RESPOSTAS INTELIGENTES
    resposta = responder_inteligente(texto)
    if resposta:
        enviar_mensagem(chat_id, resposta)
        return "ok"

    # 🔹 FLUXO DE CAPTAÇÃO
    if "quero participar" in texto.lower():
        usuarios[chat_id] = "nome"
        enviar_mensagem(chat_id, "Perfeito! Qual seu nome?")
        return "ok"

    elif estado == "nome":
        usuarios[chat_id] = {"etapa": "interesse", "nome": texto}
        enviar_mensagem(chat_id, "Qual seu interesse?\n1️⃣ Curiosidade\n2️⃣ Renda extra")
        return "ok"

    elif isinstance(estado, dict) and estado.get("etapa") == "interesse":
        nome = estado["nome"]

        if texto == "1":
            interesse = "curiosidade"
        elif texto == "2":
            interesse = "renda extra"
        else:
            enviar_mensagem(chat_id, "Digite 1 ou 2")
            return "ok"

        # 💾 SALVAR LEAD
        leads.append({
            "nome": nome,
            "interesse": interesse
        })

        usuarios[chat_id] = "finalizado"

        enviar_mensagem(chat_id, f"Pronto, {nome}! ✅\nVocê entrou como: {interesse}")
        return "ok"

    # 🔹 PADRÃO
    enviar_mensagem(chat_id, "Digite:\n👉 Quero participar\n👉 Como funciona")

    return "ok"
