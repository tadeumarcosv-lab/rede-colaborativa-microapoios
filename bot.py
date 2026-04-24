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


