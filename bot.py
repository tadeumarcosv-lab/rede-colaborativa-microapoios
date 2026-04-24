from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")

def enviar(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

# 🧠 FUNÇÃO PRINCIPAL (CÉREBRO DO BOT)
def processar_mensagem(texto):
    texto = texto.lower()

    if texto in ["oi", "olá", "ola", "start"]:
        return (
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "Digite:\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações"
        )

    elif texto == "1":
        return (
            "📌 Como funciona:\n"
            "A rede conecta pessoas para apoio financeiro colaborativo, "
            "com base em transparência e cooperação."
        )

    elif texto == "2":
        return (
            "🤝 Participar:\n"
            "Você pode começar interagindo aqui e entender o funcionamento.\n"
            "Em breve teremos mais opções automatizadas."
        )

    elif texto == "3":
        return (
            "ℹ️ Informações:\n"
            "Este projeto é colaborativo, ético e em construção contínua."
        )

    elif texto == "ajuda":
        return (
            "🆘 Menu:\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações"
        )

    else:
        return "❓ Não entendi. Digite 'ajuda' para ver as opções."

# 🔗 WEBHOOK
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        resposta = processar_mensagem(texto)
        enviar(chat_id, resposta)

    return "ok"

# 🏠 ROTA PRINCIPAL
@app.route('/')
def home():
    return "Bot online"

# ❤️ HEALTHCHECK (IMPORTANTE)
@app.route('/healthcheck')
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
