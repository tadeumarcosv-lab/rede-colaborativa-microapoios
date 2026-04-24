from flask import Flask, request
import requests
import os
import sqlite3

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")

# =========================
# 🧠 BANCO DE DADOS (MEMÓRIA)
# =========================

conn = sqlite3.connect("usuarios.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    chat_id INTEGER PRIMARY KEY,
    estado TEXT
)
""")

conn.commit()

def get_estado(chat_id):
    cursor.execute("SELECT estado FROM usuarios WHERE chat_id = ?", (chat_id,))
    resultado = cursor.fetchone()
    return resultado[0] if resultado else "inicio"

def salvar_estado(chat_id, estado):
    cursor.execute("""
    INSERT OR REPLACE INTO usuarios (chat_id, estado)
    VALUES (?, ?)
    """, (chat_id, estado))
    conn.commit()

# =========================
# 🤖 ENVIO DE MENSAGEM
# =========================

def enviar(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

# =========================
# 🧠 CÉREBRO DO BOT
# =========================

def processar_mensagem(texto, estado):
    texto = texto.lower()

    if estado == "inicio":
        if texto in ["oi", "olá", "ola", "start"]:
            return (
                "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
                "Digite:\n"
                "1 - Como funciona\n"
                "2 - Participar\n"
                "3 - Informações",
                "menu"
            )
        else:
            return ("Digite 'oi' para começar.", "inicio")

    elif estado == "menu":
        if texto == "1":
            return (
                "📌 Como funciona:\n"
                "A rede conecta pessoas para apoio financeiro colaborativo.",
                "explicou"
            )

        elif texto == "2":
            return (
                "🤝 Participar:\n"
                "Você pode começar entendendo o sistema.",
                "participar"
            )

        elif texto == "3":
            return (
                "ℹ️ Informações:\n"
                "Projeto colaborativo, ético e em evolução.",
                "info"
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu")

    elif estado == "explicou":
        if texto in ["sim", "quero"]:
            return (
                "Ótimo! Vamos avançar para participação.",
                "participar"
            )
        else:
            return ("Digite 'sim' para continuar.", "explicou")

    else:
        return ("Digite 'oi' para reiniciar.", "inicio")

# =========================
# 🔗 WEBHOOK
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        estado = get_estado(chat_id)

        resposta, novo_estado = processar_mensagem(texto, estado)

        salvar_estado(chat_id, novo_estado)

        enviar(chat_id, resposta)

    return "ok"

# =========================
# 🏠 ROTA PRINCIPAL
# =========================

@app.route('/')
def home():
    return "Bot online"

# =========================
# ❤️ HEALTHCHECK
# =========================

@app.route('/healthcheck')
def health():
    return "ok", 200

# =========================
# 🚀 START
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
