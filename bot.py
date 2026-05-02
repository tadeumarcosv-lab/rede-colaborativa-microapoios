from flask import Flask, request
import requests
import os
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

usuarios = {}

# 🔥 IA MAIS COMPLETA BASEADA NO SEU PROJETO
def responder_inteligente(texto):
    texto = texto.lower().strip()

    respostas = {
        "seguro": "Sim. É seguro porque não envolve cadastro, empresa ou promessa de lucro. É uma troca voluntária entre pessoas.",

        "como funciona": "Você cria um grupo no WhatsApp, envia pequenos valores via Pix para até 10 pessoas e recebe também. Isso cria um ciclo colaborativo simples e contínuo.",

        "golpe": "Não é golpe porque não existe promessa de lucro, nem obrigação. Tudo é voluntário e transparente.",

        "pirâmide": "Não é pirâmide. Não há hierarquia, nem entrada obrigatória, nem ganhos garantidos.",

        "pix": "Os valores são pequenos, de centavos até R$1, justamente para ser acessível a qualquer pessoa.",

        "quem pode participar": "Qualquer pessoa pode participar: estudantes, trabalhadores, aposentados.",

        "precisa pagar": "Não há taxa. Você só envia valores pequenos se quiser participar da dinâmica.",

        "quanto ganha": "Não é um sistema de ganho financeiro. É ajuda mútua contínua entre pessoas.",

        "vale a pena": "Vale para quem acredita em colaboração, constância e ajuda entre pessoas.",

        "funciona mesmo": "Funciona na medida da participação. Quanto mais pessoas colaboram, mais ativo o sistema fica.",

        "grupo": "Você precisa criar um grupo no WhatsApp com seu nome e sua chave Pix para iniciar sua rede.",

        "comprovante": "Os comprovantes devem ser postados no grupo para manter transparência.",

        "participar": "Perfeito. Vamos começar. Você deseja participar? (Sim/Não)"
    }

    for chave in respostas:
        if chave in texto:
            return respostas[chave]

    return "Posso te explicar melhor como funciona ou te ajudar a participar. O que você quer saber?"

# 🔹 SALVAR LEAD SEM DUPLICAR
def salvar_lead(nome, interesse):
    nome = nome.strip().lower()
    interesse = interesse.strip().lower()

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:

            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    interesse TEXT,
                    UNIQUE (nome, interesse)
                )
            """)

            cur.execute("""
                INSERT INTO leads (nome, interesse)
                VALUES (%s, %s)
                ON CONFLICT (nome, interesse) DO NOTHING
            """, (nome, interesse))

# 🔹 HOME
@app.route("/")
def home():
    return "IA MAXIMA ATIVA 🚀"

# 🔹 PAINEL
@app.route("/leads")
def ver_leads():
    html = "<h2>📊 Leads Capturados</h2>"

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nome, interesse FROM leads")
            dados = cur.fetchall()

            if not dados:
                return html + "<p>Nenhum lead ainda.</p>"

            for nome, interesse in dados:
                html += f"<p>👤 Nome: {nome.capitalize()}<br>🔥 Interesse: {interesse}</p><hr>"

    return html

# 🔹 ENVIAR RESPOSTA
def responder(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": texto})

# 🔹 WEBHOOK
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" not in data:
        return "ok"

    chat_id = data["message"]["chat"]["id"]
    texto = data["message"].get("text", "")

    resposta_auto = responder_inteligente(texto)
    if resposta_auto:
        responder(chat_id, resposta_auto)

    estado = usuarios.get(chat_id, "inicio")

    if texto == "/start":
        usuarios[chat_id] = "inicio"
        responder(chat_id, "Olá! Quer entender como funciona ou participar?")

    elif estado == "inicio" and "participar" in texto.lower():
        usuarios[chat_id] = "confirmar"
        responder(chat_id, "Você deseja participar? (Sim/Não)")

    elif estado == "confirmar" and texto.lower() == "sim":
        usuarios[chat_id] = "nome"
        responder(chat_id, "Qual seu nome?")

    elif estado == "nome":
        usuarios[chat_id] = {"nome": texto}
        responder(chat_id, "Qual seu nível de interesse?\n1 - conhecer\n2 - prioridade")

    elif isinstance(usuarios.get(chat_id), dict):
        nome = usuarios[chat_id]["nome"]
        interesse = "prioridade" if texto == "2" else "curiosidade"

        salvar_lead(nome, interesse)

        responder(chat_id, "Perfeito! Você foi registrado com sucesso.")
        usuarios[chat_id] = "fim"

    return "ok"
