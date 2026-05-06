from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        estado = usuarios.get(chat_id, "inicio")

        # 🔹 INÍCIO
        if texto == "/start":
            usuarios[chat_id] = "menu"
            responder(chat_id, "Bem-vindo!\n\nQuer participar?\n\n1 - Sim\n2 - Saber mais")

        # 🔹 MENU
        elif estado == "menu":
            if texto == "1":
                usuarios[chat_id] = "nome"
                responder(chat_id, "Qual seu nome?")
            elif texto == "2":
                responder(chat_id, "É um sistema de ajuda colaborativa entre pessoas.\n\nDigite 1 para participar.")
            else:
                responder(chat_id, "Digite 1 ou 2.")

        # 🔹 CAPTURA NOME + SALVA
        elif estado == "nome":
            nome = texto

            salvar_lead(nome)

            usuarios[chat_id] = "fim"
            responder(chat_id, f"Prazer, {nome}!\n\nCadastro salvo com sucesso ✅")

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
