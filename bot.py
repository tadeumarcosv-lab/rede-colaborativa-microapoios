from flask import Flask, request
import requests
import sqlite3

app = Flask(__name__)

TOKEN = "SEU_TOKEN_AQUI"

# =========================
# 🧠 BANCO DE DADOS
# =========================

conn = sqlite3.connect("usuarios.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    chat_id INTEGER PRIMARY KEY,
    estado TEXT,
    nome TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    interesse TEXT
)
""")

conn.commit()

def get_usuario(chat_id):
    cursor.execute("SELECT estado, nome FROM usuarios WHERE chat_id = ?", (chat_id,))
    result = cursor.fetchone()
    if result:
        return result
    return ("inicio", None)

def salvar_usuario(chat_id, estado, nome):
    cursor.execute("""
    INSERT OR REPLACE INTO usuarios (chat_id, estado, nome)
    VALUES (?, ?, ?)
    """, (chat_id, estado, nome))
    conn.commit()

def salvar_lead(nome, interesse):
    cursor.execute("""
    INSERT INTO leads (nome, interesse)
    VALUES (?, ?)
    """, (nome, interesse))
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

def processar(texto, estado, nome):

    texto = texto.lower().strip()

    # RESET GLOBAL
    if texto in ["oi", "olá", "ola", "/start", "start"]:
        return (
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações",
            "menu",
            None
        )

    # INTELIGÊNCIA
    if "participar" in texto:
        texto = "2"
    elif "funciona" in texto:
        texto = "1"

    # MENU
    if estado == "menu":

        if texto == "1":
            return (
                "📌 Como funciona:\n"
                "A rede conecta pessoas para apoio financeiro colaborativo.\n\n"
                "Deseja participar? (sim/não)",
                "explicou",
                nome
            )

        elif texto == "2":
            return (
                "🤝 Vamos direto para participação!\n\n"
                "Deseja entrar agora? (sim/não)",
                "participar",
                nome
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu", nome)

    # EXPLICAÇÃO
    elif estado == "explicou":

        if texto == "sim":
            return (
                "🤝 Vamos direto para participação!\n\n"
                "Deseja entrar agora? (sim/não)",
                "participar",
                nome
            )
        else:
            return ("Responda com 'sim' para continuar.", "explicou", nome)

    # PARTICIPAR
    elif estado == "participar":

        if texto == "sim":
            return (
                "Perfeito! 🙌\n\n"
                "Para continuar, me diga seu nome:",
                "nome",
                nome
            )

        elif texto == "nao":
            return ("Tudo bem! Digite 'oi' quando quiser voltar.", "inicio", None)

        else:
            return ("Responda com 'sim' ou 'não'.", "participar", nome)

    # PEGAR NOME
    elif estado == "nome":

        nome = texto.capitalize()

        return (
            f"Ótimo, {nome}! 👏\n\n"
            "Você quer:\n"
            "1 - Receber informações\n"
            "2 - Entrar assim que abrir\n\n"
            "Digite 1 ou 2:",
            "interesse",
            nome
        )

    # INTERESSE
    elif estado == "interesse":

        if texto == "1":
            salvar_lead(nome, "info")
            return (
                f"Perfeito, {nome}! Você receberá informações 📩",
                "fim",
                nome
            )

        elif texto == "2":
            salvar_lead(nome, "prioridade")
            return (
                f"Excelente, {nome}! 🚀\nVocê está na lista de prioridade.",
                "fim",
                nome
            )

        else:
            return ("Digite 1 ou 2.", "interesse", nome)

    # FINAL
    elif estado == "fim":
        return ("Digite 'oi' para recomeçar.", "inicio", None)

    return ("Digite 'oi' para começar.", "inicio", None)

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

        resposta, novo_estado, novo_nome = processar(texto, estado, nome)

        salvar_usuario(chat_id, novo_estado, novo_nome)

        enviar(chat_id, resposta)

    return "ok"

# =========================
# 🌐 PAINEL WEB
# =========================

@app.route('/leads')
def painel():
    cursor.execute("SELECT nome, interesse FROM leads")
    dados = cursor.fetchall()

    html = "<h2>📊 Leads capturados</h2><ul>"

    for nome, interesse in dados:
        html += f"<li>👤 {nome} - {interesse}</li>"

    html += "</ul>"

    return html

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
