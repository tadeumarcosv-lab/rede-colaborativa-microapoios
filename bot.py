from flask import Flask, request
import requests
import os
import sqlite3

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")

# =========================
# 🧠 BANCO SQLITE
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
    r = cursor.fetchone()
    if r:
        return r
    return ("inicio", None)

def salvar_usuario(chat_id, estado=None, nome=None, interesse=None):
    atual = get_usuario(chat_id)

    estado = estado if estado else atual[0]
    nome = nome if nome else atual[1]

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

def processar_mensagem(texto, estado):

    texto = (texto or "").lower().strip()

    # 🔥 RESET GLOBAL (PRIORIDADE MÁXIMA)
    if texto in ["oi", "/start", "start"]:
        return (
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações",
            "menu",
            None,
            None
        )

    # 🔒 INTELIGÊNCIA SÓ NO MENU
    if estado == "menu":
        if any(p in texto for p in ["participar", "entrar"]):
            texto = "2"
        elif "funciona" in texto:
            texto = "1"

    # =========================
    # FLUXO
    # =========================

    if estado == "menu":

        if texto == "1":
            return (
                "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro.\n\nDeseja participar? (sim/não)",
                "explicou",
                None,
                None
            )

        elif texto == "2":
            return (
                "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar",
                None,
                None
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu", None, None)

    elif estado == "explicou":

        if texto in ["sim", "s"]:
            return (
                "Ótimo! Vamos participar.\nDeseja entrar agora? (sim/não)",
                "participar",
                None,
                None
            )
        else:
            return ("Responda com 'sim' ou 'não'.", "explicou", None, None)

    elif estado == "participar":

        if texto in ["sim", "s"]:
            return (
                "Perfeito! 🙌\n\nMe diga seu nome:",
                "nome",
                None,
                None
            )
        elif texto in ["nao", "não", "n"]:
            return (
                "Tudo bem 😊\nDigite 'oi' quando quiser voltar.",
                "inicio",
                None,
                None
            )
        else:
            return ("Responda com 'sim' ou 'não'.", "participar", None, None)

    elif estado == "nome":

        nome = texto.title()

        return (
            f"Ótimo, {nome}! 👏\n\nVocê quer:\n1 - Receber informações\n2 - Entrar assim que abrir\n\nDigite 1 ou 2:",
            "interesse",
            nome,
            None
        )

    elif estado == "interesse":

        if texto == "1":
            return (
                "Perfeito! Você receberá informações 📩\n\nDigite 'oi' para recomeçar.",
                "fim",
                None,
                "info"
            )

        elif texto == "2":
            return (
                "Excelente! 🚀 Você está na lista de prioridade.\n\nDigite 'oi' para recomeçar.",
                "fim",
                None,
                "prioridade"
            )

        else:
            return ("Digite 1 ou 2.", "interesse", None, None)

    elif estado == "fim":
        return ("Digite 'oi' para começar novamente.", "inicio", None, None)

    return ("Digite 'oi' para começar.", "inicio", None, None)

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

        resposta, novo_estado, nome_novo, interesse = processar_mensagem(texto, estado)

        if nome_novo:
            nome = nome_novo

        salvar_usuario(chat_id, novo_estado, nome, interesse)

        enviar(chat_id, resposta)

    return "ok"

# =========================
# 📊 VER LEADS
# =========================

@app.route('/leads')
def leads():
    cursor.execute("SELECT nome, interesse FROM usuarios WHERE nome IS NOT NULL")
    dados = cursor.fetchall()

    if not dados:
        return "Nenhum lead ainda."

    resposta = "📊 Leads capturados:\n\n"
    for nome, interesse in dados:
        resposta += f"👤 {nome} - {interesse}\n"

    return resposta

# =========================
# 🏠 HOME
# =========================

@app.route('/')
def home():
    return "Bot online"

# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
