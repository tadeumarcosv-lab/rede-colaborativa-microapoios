import os
from flask import Flask, request
import requests
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

# ================= BANCO =================
def conectar():
    return psycopg.connect(DATABASE_URL)

def criar_tabela():
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS leads (
                    id SERIAL PRIMARY KEY,
                    nome TEXT,
                    interesse TEXT
                )
            """)
criar_tabela()

def salvar_lead(nome, interesse):
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM leads WHERE nome = %s", (nome,))
            existe = cur.fetchone()

            if not existe:
                cur.execute(
                    "INSERT INTO leads (nome, interesse) VALUES (%s, %s)",
                    (nome, interesse)
                )

def listar_leads():
    with conectar() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT nome, interesse FROM leads")
            return cur.fetchall()

# ================= TELEGRAM =================
def enviar_mensagem(chat_id, texto):
    requests.post(URL, json={
        "chat_id": chat_id,
        "text": texto
    })

def processar_mensagem(texto, chat_id):
    texto = texto.lower().strip()

    if texto in ["oi", "olá", "ola", "/start"]:
        usuarios[chat_id] = {"estado": "menu"}
        return """👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝

1 - Como funciona
2 - Participar
3 - Informações"""

    if "participar" in texto:
        usuarios[chat_id] = {"estado": "fluxo"}
        return "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)"

    if chat_id not in usuarios:
        usuarios[chat_id] = {"estado": "menu"}

    estado = usuarios[chat_id]["estado"]

    if estado == "menu":
        if texto == "1":
            usuarios[chat_id]["estado"] = "fluxo"
            return "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro colaborativo.\n\nDeseja participar? (sim/não)"

        elif texto == "2":
            usuarios[chat_id]["estado"] = "fluxo"
            return "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)"

        elif texto == "3":
            return "ℹ️ Mais informações em breve."

        else:
            return "Escolha 1, 2 ou 3."

    elif estado == "fluxo":
        if texto == "sim":
            usuarios[chat_id]["estado"] = "nome"
            return "Perfeito! 🙌\n\nPara continuar, me diga seu nome:"
        elif texto in ["não", "nao"]:
            usuarios[chat_id]["estado"] = "menu"
            return "Tudo bem 😊\n\nDigite 1, 2 ou 3."
        else:
            return "Responda com 'sim' ou 'não'."

    elif estado == "nome":
        usuarios[chat_id]["nome"] = texto.capitalize()
        usuarios[chat_id]["estado"] = "escolha"

        return f"Ótimo, {usuarios[chat_id]['nome']}! 👏\n\nVocê quer:\n1 - Receber informações\n2 - Entrar assim que abrir\n\nDigite 1 ou 2:"

    elif estado == "escolha":
        nome = usuarios[chat_id]["nome"]

        if texto == "1":
            salvar_lead(nome, "informações")
            usuarios[chat_id]["estado"] = "menu"
            return f"Perfeito, {nome}! 📩 Você receberá mais informações.\n\nDigite 'oi' para recomeçar."

        elif texto == "2":
            salvar_lead(nome, "prioridade")
            usuarios[chat_id]["estado"] = "menu"
            return f"Excelente, {nome}! 🚀\nVocê está na lista de prioridade.\n\nDigite 'oi' para recomeçar."

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
        html += f"<p>👤 Nome: {nome}<br>🔥 Interesse: {interesse}</p><hr>"

    return html

# ================= HOME =================
@app.route("/")
def home():
    return "POSTGRESQL ATIVO 🚀"

# ================= RUN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
