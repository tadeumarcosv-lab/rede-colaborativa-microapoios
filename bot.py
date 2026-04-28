from flask import Flask, request
import requests
import os
import psycopg2

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# =========================
# 🧠 BANCO POSTGRES
# =========================

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    chat_id BIGINT PRIMARY KEY,
    estado TEXT,
    nome TEXT,
    interesse TEXT
)
""")
conn.commit()

# =========================
# 📥 ESTADO
# =========================

def get_usuario(chat_id):
    cursor.execute("SELECT estado, nome, interesse FROM usuarios WHERE chat_id = %s", (chat_id,))
    resultado = cursor.fetchone()
    return resultado if resultado else ("inicio", None, None)

def salvar_usuario(chat_id, estado, nome=None, interesse=None):
    cursor.execute("""
    INSERT INTO usuarios (chat_id, estado, nome, interesse)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (chat_id)
    DO UPDATE SET estado = EXCLUDED.estado,
                  nome = EXCLUDED.nome,
                  interesse = EXCLUDED.interesse
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

def processar_mensagem(texto, estado, nome, interesse):

    if not texto:
        return ("Digite algo para continuar.", estado, nome, interesse)

    texto = texto.lower().strip()

    # comandos especiais
    if texto == "/leads":
        cursor.execute("SELECT nome, interesse FROM usuarios WHERE nome IS NOT NULL")
        dados = cursor.fetchall()

        if not dados:
            return ("Nenhum lead ainda.", estado, nome, interesse)

        lista = "📊 Leads capturados:\n\n"
        for n, i in dados:
            lista += f"👤 {n} - {i}\n"

        return (lista, estado, nome, interesse)

    # inteligência
    if "participar" in texto:
        texto = "2"
    elif "funciona" in texto:
        texto = "1"

    # fluxo
    if estado == "inicio":
        return (
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações",
            "menu", nome, interesse
        )

    elif estado == "menu":
        if texto == "1":
            return (
                "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro.\n\nDeseja participar? (sim/não)",
                "explicou", nome, interesse
            )

        elif texto == "2":
            return (
                "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar", nome, interesse
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu", nome, interesse)

    elif estado == "explicou":
        if texto == "sim":
            return (
                "Ótimo! Deseja entrar agora? (sim/não)",
                "participar", nome, interesse
            )
        else:
            return ("Responda 'sim' para continuar.", "explicou", nome, interesse)

    elif estado == "participar":
        if texto == "sim":
            return ("Perfeito! 🙌\n\nMe diga seu nome:", "nome", nome, interesse)
        else:
            return ("Tudo bem! Digite 'oi' quando quiser.", "inicio", nome, interesse)

    elif estado == "nome":
        nome = texto.capitalize()
        return (
            f"Ótimo, {nome}! 👏\n\n"
            "1 - Receber informações\n"
            "2 - Entrar assim que abrir\n\nDigite 1 ou 2:",
            "interesse", nome, interesse
        )

    elif estado == "interesse":
        if texto == "1":
            interesse = "informações"
        elif texto == "2":
            interesse = "prioridade"
        else:
            return ("Digite 1 ou 2.", "interesse", nome, interesse)

        return (
            f"Excelente, {nome}! 🚀\nVocê está na lista de {interesse}.\n\nDigite 'oi' para recomeçar.",
            "inicio", nome, interesse
        )

    return ("Digite 'oi' para começar.", "inicio", nome, interesse)

# =========================
# 🔗 WEBHOOK
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        estado, nome, interesse = get_usuario(chat_id)

        resposta, novo_estado, nome, interesse = processar_mensagem(texto, estado, nome, interesse)

        salvar_usuario(chat_id, novo_estado, nome, interesse)

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
