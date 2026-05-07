from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"
ADMIN_ID = "6245630965"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

WHATSAPP_LINK = "https://wa.me/5531991150767"

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "").lower()

        usuarios.setdefault(chat_id, "menu")

        # 🔹 START
        if texto == "/start":

            usuarios[chat_id] = "menu"

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Bem-vindo 👇

Escolha um assunto:

1 - O que é
2 - Como funciona
3 - Como criar seu grupo
4 - Segurança
5 - Reinvestimento
6 - Integração entre grupos
7 - Participar
8 - Falar comigo no WhatsApp 📱
""")

        # 🔹 MENU PRINCIPAL
        elif texto == "1":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

📖 O QUE É

Rede de apoio financeiro colaborativo entre parentes, amigos e pessoas diversas, baseada em microdoações voluntárias.

O objetivo é criar uma rede simples, descentralizada e acessível de ajuda mútua.
""")

        elif texto == "2":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

⚙ COMO FUNCIONA

1. Crie seu grupo no WhatsApp
2. Compartilhe o Texto Geral
3. Envie micro apoios via Pix
4. Receba apoios
5. Poste comprovantes
6. Troque links entre grupos
7. Continue o ciclo
""")

        elif texto == "3":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

📱 COMO CRIAR SEU GRUPO

Nome recomendado:

Rede de Apoio Financeiro Colaborativo – [Sua Chave Pix] – [Seu Primeiro Nome]

Configuração recomendada:

✔ Apenas administradores podem postar
✔ WhatsApp visível para contato
""")

        elif texto == "4":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

🔐 SEGURANÇA

Ao postar comprovantes, deixe visível apenas:

✔ Primeiro nome
✔ Banco
✔ Chave Pix

Evite divulgar dados desnecessários.
""")

        elif texto == "5":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

♻ REINVESTIMENTO

Sugestão prática:

✔ 50% do que receber → guardar
✔ 50% → reinvestir na rede

A força do sistema está na continuidade.
""")

        elif texto == "6":

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

🌐 INTEGRAÇÃO ENTRE GRUPOS

✔ Troque links dos grupos
✔ Adicione outros grupos
✔ Conecte pessoas

Isso cria uma rede interligada e descentralizada.
""")

        elif texto == "7":

            usuarios[chat_id] = "cadastro"

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

👤 PARTICIPAR

Qual seu primeiro nome?
""")

        elif texto == "8":

            responder(chat_id,
f"""Rede de Apoio Financeiro Colaborativo

📱 CONTATO

Qualquer dúvida, fale comigo no WhatsApp:

{WHATSAPP_LINK}
""")

        # 🔹 CADASTRO
        elif usuarios.get(chat_id) == "cadastro":

            nome = texto.title()

            salvar_lead(nome)
            enviar_para_admin(nome)

            usuarios[chat_id] = "menu"

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

✅ Cadastro recebido com sucesso.

Agora continue explorando os assuntos do sistema pelo menu.

Se necessário:

8 - Falar comigo no WhatsApp 📱
""")

        else:

            responder(chat_id,
"""Rede de Apoio Financeiro Colaborativo

Digite uma opção válida:

1 - O que é
2 - Como funciona
3 - Como criar seu grupo
4 - Segurança
5 - Reinvestimento
6 - Integração entre grupos
7 - Participar
8 - Falar comigo no WhatsApp 📱
""")

    return "ok"

def responder(chat_id, mensagem):

    requests.post(URL, json={
        "chat_id": chat_id,
        "text": mensagem
    })

def salvar_lead(nome):

    with open("leads.txt", "a") as arquivo:
        arquivo.write(f"{nome} - interessado\n")

def enviar_para_admin(nome):

    mensagem = f"""📥 Novo Lead

Nome: {nome}
Status: interessado"""

    requests.post(URL, json={
        "chat_id": ADMIN_ID,
        "text": mensagem
    })
