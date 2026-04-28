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

    if any(p in texto for p in ["participar", "entrar"]):
        texto = "2"
    elif "funciona" in texto:
        texto = "1"
    elif texto in ["sim", "s"]:
        texto = "sim"
    elif texto in ["não", "nao", "n"]:
        texto = "nao"

    # RESET GLOBAL
    if texto in ["oi", "/start", "start"]:
        return ("inicio", None, "menu", 
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "1 - Como funciona\n2 - Participar\n3 - Informações")

    if estado == "menu":
        if texto == "1":
            return (estado, None, "explicou",
                "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro.\n\nDeseja participar? (sim/não)")

        elif texto == "2":
            return (estado, None, "participar",
                "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)")

        else:
            return (estado, None, "menu", "Escolha 1, 2 ou 3.")

    elif estado == "explicou":
        if texto == "sim":
            return (estado, None, "participar",
                "Ótimo! Vamos participar.\nDeseja entrar agora? (sim/não)")
        else:
            return (estado, None, "explicou", "Responda sim ou não.")

    elif estado == "participar":
        if texto == "sim":
            return (estado, None, "nome",
                "Perfeito! 🙌\n\nMe diga seu nome:")
        else:
            return (estado, None, "inicio", "Digite 'oi' quando quiser voltar.")

    elif estado == "nome":
        return (estado, texto.title(), "interesse",
            f"Ótimo, {texto.title()}!\n\n1 - Receber informações\n2 - Entrar assim que abrir")

    elif estado == "interesse":
        if texto == "1":
            return (estado, None, "fim",
                "Você será avisado! 📩\nDigite 'oi' para recomeçar.")
        elif texto == "2":
            return (estado, None, "fim",
                "🚀 Você está na lista de prioridade!\nDigite 'oi' para recomeçar.")
        else:
            return (estado, None, "interesse", "Digite 1 ou 2.")

    return (estado, None, "inicio", "Digite 'oi' para começar.")

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

        estado_antigo, nome_novo, novo_estado, resposta = processar_mensagem(texto, estado)

        if nome_novo:
            nome = nome_novo

        salvar_usuario(chat_id, novo_estado, nome)

        enviar(chat_id, resposta)

    return "ok"

# =========================
# 👁️ VER LEADS
# =========================

@app.route('/leads')
def ver_leads():
    cursor.execute("SELECT nome FROM usuarios WHERE nome IS NOT NULL")
    dados = cursor.fetchall()

    if not dados:
        return "Nenhum lead ainda."

    return "<br>".join([f"👤 {d[0]}" for d in dados])

# =========================
# 🏠 HOME
# =========================

@app.route('/')
def home():
    return "Bot online"

# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
