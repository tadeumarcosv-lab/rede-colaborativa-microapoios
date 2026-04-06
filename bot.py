import os
import logging
from flask import Flask, request
import telegram

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telegram.Bot(token=TOKEN)

logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()
        if data and "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "")
            resposta = f"Olá! Você disse: {text}\n\nQuer saber mais sobre a Rede de Apoio Financeiro Colaborativo?"
            bot.send_message(chat_id=chat_id, text=resposta)
        return "OK", 200
    except Exception as e:
        print(f"Erro: {e}")
        return "Erro", 500

@app.route('/')
def home():
    return "Servidor do bot está online!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
