from flask import Flask, request
import requests
import os
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

usuarios = {}

def salvar_lead(nome, interesse):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    interesse TEXT
                )
            """)
            cur.execute("""
                SELECT * FROM leads WHERE nome = %s AND interesse = %s
            """, (nome, interesse))
            existente = cur.fetchone()

            if not existente:
                cur.execute("""
                    INSERT INTO leads (nome, interesse)
                    VALUES (%s, %s)
                """, (nome, interesse))

@app.route("/")
def home():
    return "VERSAO NOVA ATIVA 🚀"

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
                html += f"<p>👤 Nome: {nome}<br>🔥 Interesse: {interesse}</p><hr>"

    return html

def responder(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": texto})

def responder_inteligente(texto):
    texto = texto.lower()

    if "seguro" in texto:
        return "Sim. Não há cadastro, nem promessa de lucro. É uma rede voluntária baseada em confiança."

    if "como funciona" in texto:
        return "Você cria um grupo, envia pequenos valores via Pix para até 10 pessoas e recebe delas também."

    if "participar" in texto:
        return "Perfeito. Vamos começar! Você deseja participar? (Sim/Não)"

    return None

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

    elif isinstance(estado, dict) and "nome" in estado:
        nome = estado["nome"]
        interesse = "prioridade" if texto == "2" else "curiosidade"

        salvar_lead(nome, interesse)

        responder(chat_id, "Perfeito! Você foi registrado com sucesso.")
        usuarios[chat_id] = "fim"

    return "ok"
