from flask import Flask, request
import requests
import os
import psycopg2

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

# =========================
# 🧠 CONEXÃO POSTGRES
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

def get_usuario(chat_id):
    cursor.execute("SELECT estado, nome, interesse FROM usuarios WHERE chat_id = %s", (chat_id,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado
    return ("inicio", None, None)

def salvar_usuario(chat_id, estado, nome=None, interesse=None):
    cursor.execute("""
    INSERT INTO usuarios (chat_id, estado, nome, interesse)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (chat_id) DO UPDATE SET
        estado = EXCLUDED.estado,
        nome = COALESCE(EXCLUDED.nome, usuarios.nome),
        interesse = COALESCE(EXCLUDED.interesse, usuarios.interesse)
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

    texto_original = texto
    texto = texto.lower().strip()

    # 🔍 INTELIGÊNCIA
    if any(p in texto for p in ["participar", "entrar"]):
        texto = "2"
    elif any(p in texto for p in ["como funciona", "funciona"]):
        texto = "1"

    # 🔹 INÍCIO
    if estado == "inicio":
        if texto in ["oi", "olá", "ola", "/start"]:
            return (
                "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
                "1 - Como funciona\n"
                "2 - Participar\n"
                "3 - Informações",
                "menu",
                nome,
                interesse
            )
        else:
            return ("Digite 'oi' para começar.", "inicio", nome, interesse)

    # 🔹 MENU
    elif estado == "menu":
        if texto == "1":
            return (
                "📌 Como funciona:\nA rede conecta pessoas para apoio financeiro colaborativo.\n\nDeseja participar? (sim/não)",
                "explicou",
                nome,
                interesse
            )

        elif texto == "2":
            return (
                "🤝 Vamos direto para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar",
                nome,
                interesse
            )

        elif texto == "3":
            return (
                "ℹ️ Projeto colaborativo, ético e em evolução.",
                "menu",
                nome,
                interesse
            )

        else:
            return ("Escolha 1, 2 ou 3.", "menu", nome, interesse)

    # 🔹 EXPLICAÇÃO
    elif estado == "explicou":
        if texto in ["sim", "s"]:
            return (
                "🤝 Vamos para participação!\n\nDeseja entrar agora? (sim/não)",
                "participar",
                nome,
                interesse
            )
        else:
            return ("Digite 'sim' para continuar.", "explicou", nome, interesse)

    # 🔹 PARTICIPAÇÃO
    elif estado == "participar":
        if texto in ["sim", "s"]:
            return (
                "Perfeito! 🙌\n\nMe diga seu nome:",
                "captura_nome",
                nome,
                interesse
            )
        else:
            return ("Digite 'sim' para continuar.", "participar", nome, interesse)

    # 🔹 NOME
    elif estado == "captura_nome":
        nome = texto_original.strip().title()
        return (
            f"Ótimo, {nome}! 👏\n\n1 - Receber informações\n2 - Entrar assim que abrir\n\nDigite 1 ou 2:",
            "captura_interesse",
            nome,
            interesse
        )

    # 🔹 INTERESSE
    elif estado == "captura_interesse":
        if texto == "1":
            interesse = "info"
        elif texto == "2":
            interesse = "prioridade"
        else:
            return ("Digite 1 ou 2.", "captura_interesse", nome, interesse)

        return (
            f"Perfeito, {nome}! 🚀\nVocê está registrado.\n\nDigite 'oi' para recomeçar.",
            "fim",
            nome,
            interesse
        )

    # 🔹 FINAL
    elif estado == "fim":
        return ("Digite 'oi' para começar novamente.", "inicio", nome, interesse)

    return ("Digite 'oi' para reiniciar.", "inicio", nome, interesse)

# =========================
# 🔗 WEBHOOK
# =========================

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        # 🔍 COMANDO /LEADS
        if texto == "/leads":
            cursor.execute("SELECT nome, interesse FROM usuarios")
            dados = cursor.fetchall()

            if not dados:
                enviar(chat_id, "Nenhum lead ainda.")
            else:
                lista = "📊 Leads capturados:\n\n"
                for nome, interesse in dados:
                    lista += f"👤 {nome} - {interesse}\n"

                enviar(chat_id, lista)

            return "ok"

        estado, nome, interesse = get_usuario(chat_id)

        resposta, novo_estado, novo_nome, novo_interesse = processar_mensagem(
            texto, estado, nome, interesse
        )

        salvar_usuario(chat_id, novo_estado, novo_nome, novo_interesse)

        enviar(chat_id, resposta)

    return "ok"

# =========================
# 🚀 START
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
