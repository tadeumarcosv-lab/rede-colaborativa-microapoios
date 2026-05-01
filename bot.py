import os
import psycopg
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

# ================= BANCO =================
def criar_banco():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    interesse TEXT
                )
            """)

def salvar_lead(nome, interesse):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO leads (nome, interesse) VALUES (%s, %s)",
                (nome, interesse)
            )

def listar_leads():
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nome, interesse FROM leads")
            return cur.fetchall()

criar_banco()

# ================= RESPOSTAS INTELIGENTES =================
def responder_inteligente(texto):
    if "seguro" in texto:
        return "🔐 Sim, é seguro.\n\nVocê decide com quem participar e os valores são baixos.\nNão há acesso a contas, senhas ou dados sensíveis."

    if "legal" in texto:
        return "⚖️ Sim, é legal.\n\nSão transferências voluntárias entre pessoas, usando Pix.\nNão envolve empresa nem promessa de lucro."

    if "piramide" in texto or "esquema" in texto:
        return "❌ Não é pirâmide.\n\nNão existe recrutamento obrigatório, nem níveis, nem promessa de ganho.\nÉ apenas colaboração entre pessoas."

    if "funciona" in texto:
        return "📌 Funciona assim:\n\nVocê cria um grupo, troca apoio com até 10 pessoas e reinveste parte.\nTudo simples e direto."

    if "ganhar" in texto or "dinheiro" in texto:
        return "💰 Não é para enriquecer.\n\nÉ um sistema de ajuda mútua para pequenas necessidades."

    if "começar" in texto or "como faço" in texto:
        return "🚀 Para começar:\n\n1. Crie um grupo no WhatsApp\n2. Convide até 10 pessoas\n3. Troque apoio via Pix\n4. Compartilhe comprovantes"

    return None

# ================= TELEGRAM =================
def enviar_mensagem(chat_id, texto):
    requests.post(URL, json={
        "chat_id": chat_id,
        "text": texto
    })

def processar_mensagem(texto, chat_id):
    texto = texto.lower().strip()

    # 🔁 RESET
    if texto in ["oi", "olá", "ola", "/start"]:
        usuarios[chat_id] = {"estado": "menu"}
        return """👋 Olá! Bem-vindo à Rede de Apoio Financeiro Colaborativo 🤝

1 - Como funciona
2 - Participar
3 - Dúvidas"""

    # 🧠 INTELIGENTE GLOBAL
    resposta = responder_inteligente(texto)
    if resposta:
        return resposta

    if "participar" in texto or texto == "2":
        usuarios[chat_id] = {"estado": "fluxo"}
        return "🤝 Quer entrar agora? (sim/não)"

    if chat_id not in usuarios:
        usuarios[chat_id] = {"estado": "menu"}

    estado = usuarios[chat_id]["estado"]

    # MENU
    if estado == "menu":
        if texto == "1":
            return "📌 A rede conecta pessoas para apoio financeiro simples via Pix."
        elif texto == "2":
            usuarios[chat_id]["estado"] = "fluxo"
            return "Quer entrar agora? (sim/não)"
        elif texto == "3":
            return "Pode me perguntar qualquer coisa 👍"
        else:
            return "Digite 1, 2 ou 3."

    # FLUXO
    elif estado == "fluxo":
        if texto == "sim":
            usuarios[chat_id]["estado"] = "nome"
            return "Perfeito! Qual seu nome?"
        elif texto in ["não", "nao"]:
            usuarios[chat_id]["estado"] = "menu"
            return "Tudo bem 😊"
        else:
            return "Responda com sim ou não."

    # NOME
    elif estado == "nome":
        usuarios[chat_id]["nome"] = texto.capitalize()
        usuarios[chat_id]["estado"] = "escolha"
        return "Você quer:\n1 - Receber informações\n2 - Entrar na prioridade"

    # ESCOLHA
    elif estado == "escolha":
        nome = usuarios[chat_id]["nome"]

        if texto == "1":
            salvar_lead(nome, "informações")
            return f"Perfeito, {nome}! Você receberá mais informações 👍"

        elif texto == "2":
            salvar_lead(nome, "prioridade")
            return f"Excelente, {nome}! Você está na prioridade 🚀"

        else:
            return "Digite 1 ou 2."

    return "Digite 'oi' para começar."

# ================= WEBHOOK =================
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        resposta = processar_mensagem(texto, chat_id)
        enviar_mensagem(chat_id, resposta)

    return "ok"

# ================= PAINEL =================
@app.route("/leads")
def leads():
    dados = listar_leads()

    if not dados:
        return "Nenhum lead ainda."

    html = "<h2>📊 Leads Capturados</h2>"

    for nome, interesse in dados:
        html += f"<p>👤 Nome: {nome}<br>🔥 Interesse: {interesse}</p>"

    return html

# ================= HOME =================
@app.route("/")
def home():
    return "BOT INTELIGENTE ATIVO 🚀"

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
