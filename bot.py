from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"
ADMIN_ID = "6245630965"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

WHATSAPP_LINK = "https://wa.me/5531991150767?text=Quero%20participar%20da%20Rede%20de%20Apoio%20Financeiro%20Colaborativo"

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "").lower()

        estado = usuarios.get(chat_id, "inicio")

        # 🔹 INÍCIO
        if texto == "/start":
            usuarios[chat_id] = "menu"
            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Bem-vindo 👇

1 - Ver resumo geral
2 - Entender passo a passo
3 - Falar comigo no WhatsApp 📱
""")

        # 🔹 MENU PRINCIPAL
        elif estado == "menu":
            if texto == "1":
                usuarios[chat_id] = "menu"
                responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Resumo geral 👇

É um sistema onde pessoas se ajudam financeiramente de forma organizada, através de micro apoios entre participantes.

Objetivo: criar uma rede forte de ajuda mútua.

Escolha:

2 - Ver passo a passo
3 - Falar no WhatsApp 📱
""")

            elif texto == "2":
                usuarios[chat_id] = "passo1"
                responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Passo 1 👇

A rede conecta pessoas dispostas a ajudar e receber ajuda.

Digite OK para continuar.
""")

            elif texto == "3":
                responder(chat_id,
f"""Rede de Apoio Financeiro Colaborativo

Fale comigo diretamente no WhatsApp 👇

{WHATSAPP_LINK}
""")

            else:
                responder(chat_id, "Digite 1, 2 ou 3.")

        # 🔹 PASSO A PASSO
        elif estado == "passo1":
            if "ok" in texto:
                usuarios[chat_id] = "passo2"
                responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Passo 2 👇

Cada pessoa contribui com pequenos valores para ajudar outras.

Digite OK para continuar.
""")

        elif estado == "passo2":
            if "ok" in texto:
                usuarios[chat_id] = "nome"
                responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Passo 3 👇

Agora vamos finalizar seu cadastro.

Qual seu nome?
""")

        # 🔹 CAPTURA NOME
        elif estado == "nome":
            nome = texto

            salvar_lead(nome)
            enviar_para_admin(nome)

            usuarios[chat_id] = "fim"

            responder(chat_id,
f"""Rede de Apoio Financeiro Colaborativo

Prazer, {nome}! 👇

Cadastro concluído ✅

Se quiser acelerar sua entrada, fale comigo no WhatsApp:

{WHATSAPP_LINK}
""")

        else:
            responder(chat_id, "Digite /start para começar.")

    return "ok"


def responder(chat_id, mensagem):
    requests.post(URL, json={
        "chat_id": chat_id,
        "text": mensagem
    })


def salvar_lead(nome):
    with open("leads.txt", "a") as arquivo:
        arquivo.write(f"{nome} - interessado\n")


def enviar_para_admin(nome):
    mensagem = f"""📥 Novo Lead

Nome: {nome}
Status: interessado"""

    requests.post(URL, json={
        "chat_id": ADMIN_ID,
        "text": mensagem
    })
