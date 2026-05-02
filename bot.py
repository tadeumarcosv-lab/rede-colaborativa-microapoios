from flask import Flask, request
import requests
import os
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

usuarios = {}

# 🔥 BANCO PROFISSIONAL
def inicializar_banco():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    interesse TEXT,
                    origem TEXT,
                    UNIQUE (nome, interesse)
                )
            """)

inicializar_banco()


# 🤖 RESPOSTAS MAIS HUMANAS
def responder_inteligente(texto):
    texto = texto.lower()

    if "seguro" in texto or "golpe" in texto:
        return "Entendo sua preocupação. Aqui não existe promessa de lucro nem empresa. É apenas uma troca voluntária entre pessoas usando valores pequenos."

    if "como funciona" in texto:
        return "Funciona assim: você cria um grupo no WhatsApp, envia pequenos valores (centavos até R$1) para algumas pessoas e também pode receber. É um modelo simples de colaboração."

    if "quem pode participar" in texto:
        return "Qualquer pessoa pode participar: estudantes, trabalhadores, aposentados. Não tem restrição."

    if "participar" in texto:
        return "Perfeito. Vamos começar. Você quer participar? (Sim/Não)"

    return None


# 💾 SALVAR LEAD COM ORIGEM
def salvar_lead(nome, interesse, origem="telegram"):
    nome = nome.strip().lower()
    interesse = interesse.strip().lower()

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO leads (nome, interesse, origem)
                VALUES (%s, %s, %s)
                ON CONFLICT (nome, interesse) DO NOTHING
            """, (nome, interesse, origem))


@app.route("/")
def home():
    return "SISTEMA DE CAPTAÇÃO ATIVO 🚀"


@app.route("/leads")
def ver_leads():
    html = "<h2>📊 Leads Capturados</h2>"

    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nome, interesse, origem FROM leads")
            dados = cur.fetchall()

            if not dados:
                return html + "<p>Nenhum lead ainda.</p>"

            for nome, interesse, origem in dados:
                html += f"<p>👤 {nome.capitalize()}<br>🔥 {interesse}<br>🌐 {origem}</p><hr>"

    return html


def responder(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": texto})


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
        responder(chat_id, "Olá! Posso te explicar ou te ajudar a participar.")

    elif estado == "inicio" and "participar" in texto.lower():
        usuarios[chat_id] = "confirmar"
        responder(chat_id, "Você quer participar? (Sim/Não)")

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

        responder(chat_id, "Perfeito! Você entrou no sistema.")
        usuarios[chat_id] = "fim"

    return "ok"
