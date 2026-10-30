import os
from pathlib import Path

# Pasta raiz do repositório
RAIZ = Path(__file__).resolve().parent

# Arquivo de saída (consolidado)
ARQUIVO_SAIDA = RAIZ / "docs" / "TODOS_OS_MD.md"

# Limite de tamanho por parte (em caracteres) para não estourar o GitHub
LIMITE_PARTE = 4_000_000  # ~4 MB por parte


def listar_md_raiz():
    """Lista todos os arquivos .md na raiz do repositório."""
    arquivos = []
    for item in RAIZ.iterdir():
        if item.is_file() and item.suffix.lower() == ".md":
            arquivos.append(item)
    return sorted(arquivos)


def ler_arquivo(caminho):
    """Lê o conteúdo de um arquivo .md."""
    try:
        return caminho.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"[ERRO AO LER O ARQUIVO: {e}]"


def main():
    arquivos = listar_md_raiz()

    if not arquivos:
        print("Nenhum arquivo .md encontrado na raiz.")
        return

    print(f"Encontrados {len(arquivos)} arquivos .md na raiz.")

    # Garante que a pasta docs existe
    ARQUIVO_SAIDA.parent.mkdir(parents=True, exist_ok=True)

    # Limpa o arquivo de saída (se existir)
    if ARQUIVO_SAIDA.exists():
        ARQUIVO_SAIDA.unlink()

    # Abre o arquivo de saída para escrita
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
        for i, arquivo in enumerate(arquivos, start=1):
            print(f"[{i}/{len(arquivos)}] Copiando: {arquivo.name}")

            conteudo = ler_arquivo(arquivo)

            # Escreve o separador
            saida.write(f"\n\n{'='*80}\n")
            saida.write(f"ARQUIVO: {arquivo.name}\n")
            saida.write(f"{'='*80}\n\n")

            # Escreve o conteúdo
            saida.write(conteudo)

            # Se o arquivo ficou muito grande, avisa
            if saida.tell() > LIMITE_PARTE:
                print(f"AVISO: O arquivo de saída passou de {LIMITE_PARTE} caracteres.")

    tamanho_final = ARQUIVO_SAIDA.stat().st_size
    print(f"Arquivo consolidado criado: {ARQUIVO_SAIDA} ({tamanho_final} bytes)")


if __name__ == "__main__":
    main()
