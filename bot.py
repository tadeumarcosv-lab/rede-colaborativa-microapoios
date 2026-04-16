import os
from flask import Flask, request
from telegram import Bot

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
print("TOKEN AQUI:", TOKEN)

bot = Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("CHECKED 1550:", data)

    if data and "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        bot.send_message(chat_id=chat_id, text=text)

    return "OK", 200

@app.route('/')
def home():
    return "Bot online!", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
