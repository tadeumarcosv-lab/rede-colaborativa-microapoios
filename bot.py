from flask import Flask, request
import requests
import os
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

usuarios = {}

# 🔹 BASE COMPLETA DO SEU PROJETO (IA SIMULADA)
TEXTO_BASE = """
A Rede de Apoio Financeiro Colaborativo é um sistema baseado em microdoações voluntárias entre pessoas.
Não é empresa, não promete lucro e não exige cadastro.

Funciona assim:
- Você cria um grupo no WhatsApp
- Envia pequenos valores via Pix (centavos até R$1)
- Troca ajuda com até 10 pessoas
- Posta comprovantes no grupo

A base do sistema é:
confiança, simplicidade, continuidade e reciprocidade.

Não é enriquecimento rápido.
É ajuda mútua real entre pessoas.

Qualquer pessoa pode participar.
"""

def responder_inteligente(texto):
    texto = texto.lower()

    if "seguro" in texto:
        return "Sim. É seguro porque não envolve cadastro, empresa ou promessa de lucro. É apenas troca voluntária entre pessoas."

    if "como funciona" in texto:
        return "Funciona com microdoações via Pix entre pequenos grupos. Cada pessoa ajuda outras e recebe também, criando um ciclo colaborativo."

    if "é pirâmide" in texto or "golpe" in texto:
        return "Não é pirâmide porque não há promessa de lucro, nem entrada obrigatória. É apenas ajuda voluntária entre pessoas."

    if "participar" in texto:
        return "Perfeito. Vamos começar. Você deseja participar? (Sim/Não)"

    if "pix" in texto:
        return "Os valores são pequenos (centavos até R$1), justamente para ser acessível e sustentável."

    if "funciona mesmo" in texto:
        return "Funciona na medida da participação. Quanto mais pessoas colaboram, mais o sistema se mantém ativo."

    return None


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


@app.route("/")
def home():
    return "IA COMPLETA ATIVA 🚀"


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
