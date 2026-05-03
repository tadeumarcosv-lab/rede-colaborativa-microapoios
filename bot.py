from flask import Flask, request
import requests

app = Flask(__name__)

# 🔥 COLOQUE SEU TOKEN AQUI (OBRIGATÓRIO)
TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"

# 🤖 RESPOSTAS AUTOMÁTICAS
def responder_inteligente(texto):
    texto = texto.lower()

    if "seguro" in texto or "golpe" in texto:
        return "Fica tranquilo. Aqui não existe promessa de lucro. É apenas colaboração voluntária entre pessoas."

    if "como funciona" in texto:
        return "Funciona assim: pessoas ajudam outras com pequenos valores. É uma rede colaborativa simples."

    if "quem pode participar" in texto:
        return "Qualquer pessoa pode participar."

    if "quero participar" in texto:
        return "Perfeito. Você quer participar? (Sim/Não)"

    return None


@app.route("/")
def home():
    return "VERSAO NOVA ATIVA 2 🚀"


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

    resposta = responder_inteligente(texto)

    if resposta:
        enviar_mensagem(chat_id, resposta)
    else:
        enviar_mensagem(chat_id, "Digite: Como funciona / Quero participar")

    return "ok"
