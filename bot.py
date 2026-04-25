from flask import Flask, request
import requests
import os
import sqlite3

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")

# =========================
# 🧠 BANCO DE DADOS
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
# 📤 ENVIO (COM PROTEÇÃO)
# =========================

def enviar(chat_id, texto):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, json={
            "chat_id": chat_id,
            "text": texto
        }, timeout=10)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

# =========================
# 🧠 CÉREBRO
# =========================

def processar_mensagem(texto, estado):

    if not texto:
        return ("Digite algo para continuar.", estado)

    texto = texto.lower().strip()

    # 🔍 INTELIGÊNCIA BÁSICA
    if any(p in texto for p in ["participar", "entrar", "quero participar"]):
        texto = "2"
    elif any(p in texto for p in ["como funciona", "funciona", "explicar"]):
        texto = "1"
    elif any(p in texto for p in ["info", "informação", "informacoes"]):
        texto = "3"
    elif texto in ["quero", "ok", "claro", "sim", "s"]:
        texto = "sim"
    elif texto in ["não", "nao", "n"]:
        texto = "nao"

    # 🔹 INÍCIO
    if estado == "inicio":
        if texto in ["oi", "olá", "ola", "/start", "start"]:
            return (
                "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
                "Você pode escrever normalmente ou usar o menu:\n\n"
                "1 - Como funciona\n"
                "2 - Participar\n"
                "3 - Informações",
                "menu"
            )
        else:
            return ("Digite 'oi' para começar.", "inicio")

    # 🔹 MENU
    elif estado == "menu":
        if texto == "1":
            return (
                "📌 Como funciona:\n"
                "A rede conecta pessoas para apoio financeiro colaborativo.\n\n"
                "Deseja participar? (sim/não)",
                "explicou"
            )

        elif texto == "2":
            return (
                "🤝 Participar:\n"
                "Você pode começar entendendo o sistema.\n\n"
                "Deseja continuar? (sim/não)",
                "participar"
            )

        elif texto == "3":
            return (
                "ℹ️ Informações:\n"
                "Projeto colaborativo, ético e em evolução.",
                "menu"
            )

        else:
            return ("Você pode escrever livremente ou escolher 1, 2 ou 3.", "menu")

    # 🔹 APÓS EXPLICAÇÃO
    elif estado == "explicou":
        if texto == "sim":
            return (
                "Ótimo! Vamos para participação.\n\n"
                "Você quer entrar na rede agora? (sim/não)",
                "participar"
            )
        else:
            return ("Responda com 'sim' se quiser continuar.", "explicou")

    # 🔹 PARTICIPAÇÃO
    elif estado == "participar":
        if texto == "sim":
            return (
                "✅ Perfeito! Você demonstrou interesse em participar.\n\n"
                "Em breve o sistema terá cadastro automático.\n"
                "Fique atento às novidades!",
                "fim"
            )
        elif texto == "nao":
            return (
                "Tudo bem 😊\n\n"
                "Você pode voltar quando quiser.\n"
                "Digite 'oi' para recomeçar.",
                "inicio"
            )
        else:
            return ("Responda com 'sim' ou 'não'.", "participar")

    # 🔹 FINAL
    elif estado == "fim":
        return (
            "✅ Fluxo concluído!\n\n"
            "Digite 'oi' para começar novamente.",
            "inicio"
        )

    # 🔹 SEGURANÇA
    else:
        return ("Digite 'oi' para reiniciar.", "inicio")

# =========================
# 🔗 WEBHOOK (COM PROTEÇÃO)
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
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
    except Exception as e:
        print("Erro no webhook:", e)
        return "erro", 500

# =========================
# 🏠 HOME
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