from flask import Flask, request
import requests
import os
import psycopg

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# =========================
# 🧠 BANCO POSTGRES
# =========================

conn = psycopg.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    chat_id TEXT,
    nome TEXT,
    interesse TEXT
)
""")
conn.commit()

# =========================
# 📤 ENVIO
# =========================

def enviar(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

# =========================
# 🧠 MEMÓRIA SIMPLES
# =========================

usuarios = {}

# =========================
# 🧠 CÉREBRO
# =========================

def processar_mensagem(chat_id, texto):

    if not texto:
        return "Digite algo para continuar."

    texto = texto.lower().strip()

    estado = usuarios.get(chat_id, "inicio")

    # 🔹 COMANDO LEADS
    if texto == "/leads":
        cursor.execute("SELECT nome, interesse FROM leads")
        dados = cursor.fetchall()

        if not dados:
            return "Nenhum lead ainda."

        resposta = "📊 Leads capturados:\n\n"
        for nome, interesse in dados:
            resposta += f"👤 {nome} - {interesse}\n"

        return resposta

    # 🔍 INTELIGÊNCIA
    if any(p in texto for p in ["participar", "entrar"]):
        texto = "2"
    elif any(p in texto for p in ["como funciona", "funciona"]):
        texto = "1"
    elif texto in ["sim", "s", "ok", "claro"]:
        texto = "sim"
    elif texto in ["não", "nao", "n"]:
        texto = "nao"

    # 🔹 INÍCIO
    if estado == "inicio":
        if texto in ["oi", "/start"]:
            usuarios[chat_id] = "menu"
            return (
                "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
                "1 - Como funciona\n"
                "2 - Participar\n"
                "3 - Informações"
            )
        else:
            return "Digite 'oi' para começar."

    # 🔹 MENU
    elif estado == "menu":
        if texto == "1":
            usuarios[chat_id] = "explicou"
            return (
                "📌 Como funciona:\n"
                "A rede conecta pessoas para apoio financeiro colaborativo.\n\n"
                "Deseja participar? (sim/não)"
            )

        elif texto == "2":
            usuarios[chat_id] = "participar"
            return "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)"

        elif texto == "3":
            return "ℹ️ Projeto colaborativo, ético e em evolução."

        else:
            return "Escolha 1, 2 ou 3."

    # 🔹 EXPLICAÇÃO
    elif estado == "explicou":
        if texto == "sim":
            usuarios[chat_id] = "participar"
            return "Ótimo!\n\nDeseja entrar agora? (sim/não)"
        else:
            return "Responda com 'sim' para continuar."

    # 🔹 PARTICIPAÇÃO
    elif estado == "participar":
        if texto == "sim":
            usuarios[chat_id] = "nome"
            return "Perfeito! 🙌\n\nPara continuar, me diga seu nome:"
        elif texto == "nao":
            usuarios[chat_id] = "inicio"
            return "Tudo bem 😊\nDigite 'oi' quando quiser voltar."
        else:
            return "Responda com 'sim' ou 'não'."

    # 🔹 NOME
    elif estado == "nome":
        usuarios[chat_id] = {"estado": "interesse", "nome": texto.title()}
        return (
            f"Ótimo, {texto.title()}! 👏\n\n"
            "Você quer:\n"
            "1 - Receber informações\n"
            "2 - Entrar assim que abrir\n\n"
            "Digite 1 ou 2:"
        )

    # 🔹 INTERESSE
    elif isinstance(estado, dict) and estado.get("estado") == "interesse":
        nome = estado.get("nome")

        if texto == "1":
            interesse = "informações"
        elif texto == "2":
            interesse = "prioridade"
        else:
            return "Digite 1 ou 2."

        # 💾 SALVAR NO BANCO
        cursor.execute(
            "INSERT INTO leads (chat_id, nome, interesse) VALUES (%s, %s, %s)",
            (str(chat_id), nome, interesse)
        )
        conn.commit()

        usuarios[chat_id] = "inicio"

        return f"Excelente, {nome}! 🚀\nVocê está na lista de {interesse}.\n\nDigite 'oi' para recomeçar."

    return "Digite 'oi' para começar."

# =========================
# 🔗 WEBHOOK
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        resposta = processar_mensagem(chat_id, texto)
        enviar(chat_id, resposta)

    return "ok"

# =========================
# 🏠 HOME
# =========================

@app.route('/')
def home():
    return "Bot online"

# =========================
# 🚀 START
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
