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
    estado TEXT,
    nome TEXT,
    interesse TEXT
)
""")
conn.commit()

def get_usuario(chat_id):
    cursor.execute("SELECT estado, nome FROM usuarios WHERE chat_id = ?", (chat_id,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado
    return ("inicio", None)

def salvar_usuario(chat_id, estado, nome=None, interesse=None):
    cursor.execute("""
    INSERT OR REPLACE INTO usuarios (chat_id, estado, nome, interesse)
    VALUES (?, ?, ?, ?)
    """, (chat_id, estado, nome, interesse))
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
# 🧠 CÉREBRO
# =========================

def processar_mensagem(texto, estado, nome):

    if not texto:
        return ("Digite algo para continuar.", estado, nome)

    texto = texto.lower().strip()

    # 🔍 INTELIGÊNCIA
    if any(p in texto for p in ["participar", "entrar"]):
        texto = "2"
    elif any(p in texto for p in ["como funciona", "funciona"]):
        texto = "1"
    elif any(p in texto for p in ["info", "informação"]):
        texto = "3"

    # 🔹 INÍCIO
    if estado == "inicio":
        if texto in ["oi", "olá", "ola", "/start", "start"]:
            return (
                "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
                "1 - Como funciona\n"
                "2 - Participar\n"
                "3 - Informações",
                "menu",
                nome
            )
        else:
            return ("Digite 'oi' para começar.", "inicio", nome)

    # 🔹 MENU
    elif estado == "menu":
        if texto == "1":
            return (
                "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro colaborativo.\n\nDeseja participar? (sim/não)",
                "explicou",
                nome
            )

        elif texto == "2":
            return (
                "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar",
                nome
            )

        elif texto == "3":
            return (
                "ℹ️ Projeto colaborativo, ético e em evolução.",
                "menu",
                nome
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu", nome)

    # 🔹 APÓS EXPLICAÇÃO
    elif estado == "explicou":
        if texto == "sim":
            return (
                "🤝 Vamos para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar",
                nome
            )
        else:
            return ("Responda com 'sim' para continuar.", "explicou", nome)

    # 🔹 PARTICIPAÇÃO
    elif estado == "participar":
        if texto in ["sim", "s"]:
            return (
                "Perfeito! 🙌\n\nPara continuar, me diga seu nome:",
                "captura_nome",
                nome
            )
        elif texto in ["não", "nao", "n"]:
            return (
                "Tudo bem 😊\nDigite 'oi' quando quiser voltar.",
                "inicio",
                nome
            )
        else:
            return ("Responda com 'sim' ou 'não'.", "participar", nome)

    # 🔹 CAPTURA NOME
    elif estado == "captura_nome":
        nome = texto.capitalize()
        return (
            f"Ótimo, {nome}! 👏\n\nVocê quer:\n1 - Receber informações\n2 - Entrar assim que abrir\n\nDigite 1 ou 2:",
            "captura_interesse",
            nome
        )

    # 🔹 CAPTURA INTERESSE
    elif estado == "captura_interesse":
        if texto == "1":
            return (
                f"Perfeito, {nome}! 👍\nVocê será avisado com novidades.\n\nDigite 'oi' para recomeçar.",
                "fim",
                nome
            )
        elif texto == "2":
            return (
                f"Excelente, {nome}! 🚀\nVocê está na lista de prioridade.\n\nDigite 'oi' para recomeçar.",
                "fim",
                nome
            )
        else:
            return ("Digite 1 ou 2.", "captura_interesse", nome)

    # 🔹 FINAL
    elif estado == "fim":
        return ("Digite 'oi' para começar novamente.", "inicio", nome)

    else:
        return ("Digite 'oi' para reiniciar.", "inicio", nome)

# =========================
# 🔗 WEBHOOK
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        estado, nome = get_usuario(chat_id)

        resposta, novo_estado, novo_nome = processar_mensagem(texto, estado, nome)

        salvar_usuario(chat_id, novo_estado, novo_nome)

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
