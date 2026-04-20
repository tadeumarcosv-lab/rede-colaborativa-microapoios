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

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")

        enviar(chat_id, f"Você disse: {texto}")

    return "ok"

@app.route('/')
def home():
    return "Bot online"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
