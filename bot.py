from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7903734471:AAH87bQtPPyqjeBlwX2u7zTk262jkQZeSD8"
ADMIN_ID = "6245630965"

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

usuarios = {}

WHATSAPP_LINK = "https://wa.me/5531991150767?text=Ol%C3%A1%2C%20tenho%20d%C3%BAvidas%20sobre%20a%20Rede%20de%20Apoio%20Financeiro%20Colaborativo"

TOPICOS = {
    "1": """Rede de Apoio Financeiro Colaborativo

📖 TÓPICO 1 — O QUE É

Rede de apoio financeiro colaborativo entre parentes, amigos e pessoas diversas, baseada em microdoações voluntárias.

O objetivo é criar uma rede simples, descentralizada e acessível de ajuda mútua.

Funciona apenas com:

✔ WhatsApp
✔ Pix
✔ colaboração entre pessoas

Não é empresa.
Não possui dono.
Não exige cadastro formal.

Digite OK para continuar.""",

    "2": """Rede de Apoio Financeiro Colaborativo

⚙ TÓPICO 2 — COMO FUNCIONA

1. A pessoa organiza um espaço no WhatsApp
2. Compartilha o Texto Geral com pessoas próximas
3. Envia e recebe micro apoios via Pix
4. Posta comprovantes no espaço
5. Continua ajudando outras pessoas
6. A rede vai crescendo de forma colaborativa

A força do sistema está na continuidade e na colaboração entre as pessoas.

Digite OK para continuar.""",

    "3": """Rede de Apoio Financeiro Colaborativo

📱 TÓPICO 3 — COMO ORGANIZAR COM WHATSAPP

Nome recomendado para o espaço:

Rede de Apoio Financeiro Colaborativo – [Sua Chave Pix] – [Seu Primeiro Nome]

Organização recomendada:

✔ Apenas administradores podem postar
✔ WhatsApp visível para contato
✔ Compartilhe o Texto Geral com pessoas próximas

Digite OK para continuar.""",

    "4": """Rede de Apoio Financeiro Colaborativo

🔐 TÓPICO 4 — SEGURANÇA

Ao postar comprovantes, deixe visível apenas:

✔ Primeiro nome
✔ Banco
✔ Chave Pix

Evite divulgar:

✘ documentos
✘ senhas
✘ informações pessoais desnecessárias

A simplicidade também faz parte da segurança.

Digite OK para continuar.""",

    "5": """Rede de Apoio Financeiro Colaborativo

♻ TÓPICO 5 — REINVESTIMENTO

Sugestão prática 👇

✔ 50% → guardar para segurança pessoal
✔ 50% → reinvestir na rede ajudando outras pessoas

O reinvestimento ajuda a manter o ciclo funcionando e fortalece a continuidade da rede.

Mesmo pequenos valores podem ajudar várias pessoas ao longo do tempo.

Digite OK para continuar.""",

    "6": """Rede de Apoio Financeiro Colaborativo

🌐 TÓPICO 6 — INTEGRAÇÃO ENTRE GRUPOS

COMO A CONEXÃO ACONTECE 👇

1. A pessoa que está entrando organiza o próprio espaço no WhatsApp, coloca a chave Pix e o primeiro nome
2. Envia o link para quem convidou
3. A pessoa que convidou coloca o link dela já com o comprovante dentro, do ( link ) espaço de quem está entrando
4. Depois compartilha também o próprio espaço com quem está entrando

Com o tempo, vários espaços vão ficando conectados entre si.

Isso cria uma rede colaborativa descentralizada, com vários grupos interligados.

Digite OK para continuar.""",

    "7": """Rede de Apoio Financeiro Colaborativo

👤 TÓPICO 7 — PARTICIPAR

Se você entendeu a proposta e deseja participar:

✔ organize seu espaço no WhatsApp ( grupo de WhatsApp )
✔ coloque sua chave Pix e seu primeiro nome
✔ compartilhe o Texto Geral
✔ envie seu link para quem convidou você

A rede funciona através da continuidade, colaboração e organização entre as pessoas.

Digite seu primeiro nome.""",

    "8": f"""Rede de Apoio Financeiro Colaborativo

📱 TÓPICO 8 — CONTATO

O objetivo do sistema é funcionar de forma simples, organizada e colaborativa através do próprio bot e do Texto Geral.

O WhatsApp direto é apenas para dúvidas específicas ou dificuldades maiores.

Qualquer dúvida, fale comigo no WhatsApp 👇

Tadeu Marcos Viana

{WHATSAPP_LINK}

📱 (31) 9 9115-0767"""
}

MENU = """Rede de Apoio Financeiro Colaborativo

Bem-vindo 👇

Escolha um assunto, digitando um dos números abaixo:

1 - O que é
2 - Como funciona
3 - Como organizar com WhatsApp
4 - Segurança
5 - Reinvestimento
6 - Integração entre grupos
7 - Participar
8 - Contato 📱"""

@app.route("/")
def home():
    return "BOT ONLINE 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    if "message" in data:

        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "").strip()

        texto_lower = texto.lower()

        usuarios.setdefault(chat_id, {"topico": 1})

        # START
        if texto_lower == "/start":

            usuarios[chat_id]["topico"] = 1

            responder(chat_id, MENU)

        # TÓPICOS
        elif texto in TOPICOS:

            usuarios[chat_id]["topico"] = int(texto)

            responder(chat_id, TOPICOS[texto])

        # OK
        elif texto_lower == "ok":

            proximo = usuarios[chat_id]["topico"] + 1

            if str(proximo) in TOPICOS:

                usuarios[chat_id]["topico"] = proximo

                responder(chat_id, TOPICOS[str(proximo)])

            else:

                responder(chat_id, MENU)

        # PARTICIPAÇÃO
        elif usuarios[chat_id]["topico"] == 7:

            nome = texto.title()

            salvar_lead(nome)
            enviar_para_admin(nome)

            responder(chat_id,
f"""Rede de Apoio Financeiro Colaborativo

✅ Cadastro recebido com sucesso.

Agora continue organizando seu espaço e compartilhando o Texto Geral.

Qualquer dúvida:

{WHATSAPP_LINK}
""")

        else:

            responder(chat_id, MENU)

    return "ok"

def responder(chat_id, mensagem):

    requests.post(URL, json={
        "chat_id": chat_id,
        "text": mensagem
    })

def salvar_lead(nome):

    with open("leads.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - interessado\n")

def enviar_para_admin(nome):

    mensagem = f"""📥 Novo Lead

Nome: {nome}
Status: interessado"""

    requests.post(URL, json={
        "chat_id": ADMIN_ID,
        "text": mensagem
    })
