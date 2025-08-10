import os
import shutil

# Vai para a pasta Downloads
downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# Pastas padrão do Windows
documentos = os.path.join(os.path.expanduser("~"), "Documents")
musicas = os.path.join(os.path.expanduser("~"), "Music")
fotos = os.path.join(os.path.expanduser("~"), "Pictures")
videos = os.path.join(os.path.expanduser("~"), "Videos")

# Pastas personalizadas
roms = os.path.join(downloads, "ROMs")
instaladores = os.path.join(downloads, "Instaladores")
compactados = os.path.join(downloads, "Compactados")

# Extensões gerais
categorias = {
    instaladores: [".exe", ".msi"],
    compactados: [".zip", ".rar", ".7z", ".tar", ".gz"],
    documentos: [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    musicas: [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    fotos: [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    videos: [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"]
}

# Subpastas para ROMs
roms_subpastas = {
    "3DS": [".3ds", ".cia"],
    "NDS": [".nds"],
    "SNES": [".smc", ".sfc"]
}

# Criar todas as pastas
for pasta in [instaladores, compactados, documentos, musicas, fotos, videos]:
    os.makedirs(pasta, exist_ok=True)

# Criar subpastas de ROMs
for subpasta in roms_subpastas.keys():
    os.makedirs(os.path.join(roms, subpasta), exist_ok=True)

# Organizar arquivos
for arquivo in os.listdir(downloads):
    caminho_arquivo = os.path.join(downloads, arquivo)

    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        movido = False

        # Verifica se é ROM
        for subpasta, extensoes in roms_subpastas.items():
            if extensao in extensoes:
                destino = os.path.join(roms, subpasta, arquivo)
                shutil.move(caminho_arquivo, destino)
                print(f"Movido: {arquivo} → ROMs/{subpasta}")
                movido = True
                break

        # Se não for ROM, verifica categorias gerais
        if not movido:
            for pasta, extensoes in categorias.items():
                if extensao in extensoes:
                    destino = os.path.join(pasta, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {pasta}")
                    break
