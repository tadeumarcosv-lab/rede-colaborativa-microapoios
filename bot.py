def processar_mensagem(texto, estado):
texto = texto.lower()

# 🔍 INTELIGÊNCIA BÁSICA (interpretação de linguagem)
if "participar" in texto:
    texto = "2"
elif "funciona" in texto:
    texto = "1"
elif "informação" in texto or "info" in texto:
    texto = "3"
elif texto in ["quero", "ok", "claro", "sim"]:
    texto = "sim"

# 🔹 INÍCIO
if estado == "inicio":
    if texto in ["oi", "olá", "ola", "start"]:
        return (
            "👋 Olá! Bem-vindo à Rede Colaborativa de Microapoios 🤝\n\n"
            "Você pode escrever normalmente ou usar o menu:\n\n"
            "1 - Como funciona\n"
            "2 - Participar\n"
            "3 - Informações",
            "menu"
        )
    else:
        return ("Digite 'oi' para começar.", "inicio")

# 🔹 MENU
elif estado == "menu":
    if texto == "1":
        return (
            "📌 Como funciona:\n"
            "A rede conecta pessoas para apoio financeiro colaborativo.\n\n"
            "Deseja participar? (sim/não)",
            "explicou"
        )

    elif texto == "2":
        return (
            "🤝 Participar:\n"
            "Você pode começar entendendo o sistema.\n\n"
            "Deseja continuar? (sim/não)",
            "participar"
        )

    elif texto == "3":
        return (
            "ℹ️ Informações:\n"
            "Projeto colaborativo, ético e em evolução.",
            "menu"
        )

    else:
        return ("Você pode escrever livremente ou escolher 1, 2 ou 3.", "menu")

# 🔹 APÓS EXPLICAÇÃO
elif estado == "explicou":
    if texto == "sim":
        return (
            "Ótimo! Vamos para participação.\n\n"
            "Você quer entrar na rede agora? (sim/não)",
            "participar"
        )
    else:
        return ("Responda com 'sim' se quiser continuar.", "explicou")

# 🔹 PARTICIPAÇÃO
elif estado == "participar":
    if texto == "sim":
        return (
            "✅ Perfeito! Você demonstrou interesse em participar.\n\n"
            "Em breve o sistema terá cadastro automático.\n"
            "Fique atento às novidades!",
            "fim"
        )
    elif texto in ["não", "nao"]:
        return (
            "Tudo bem 😊\n\n"
            "Você pode voltar quando quiser.\n"
            "Digite 'oi' para recomeçar.",
            "inicio"
        )
    else:
        return ("Responda com 'sim' ou 'não'.", "participar")

# 🔹 FINAL
elif estado == "fim":
    return (
        "✅ Fluxo concluído!\n\n"
        "Digite 'oi' para começar novamente.",
        "inicio"
    )

# 🔹 SEGURANÇA
else:
    return ("Digite 'oi' para reiniciar.", "inicio")

            
