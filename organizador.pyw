import os
import shutil
import time

def organizar():
    downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    roms = os.path.join(downloads, "ROMs")
    instaladores = os.path.join(downloads, "Instaladores")
    compactados = os.path.join(downloads, "Compactados")
    documentos = os.path.join(os.path.expanduser("~"), "Documents")
    musicas = os.path.join(os.path.expanduser("~"), "Music")
    fotos = os.path.join(os.path.expanduser("~"), "Pictures")
    videos = os.path.join(os.path.expanduser("~"), "Videos")

    roms_subpastas = {
        "3DS": [".3ds", ".cia"],
        "NDS": [".nds"],
        "PS1": [".bin", ".cue", ".pbp"],
        "PS2": [".iso", ".img"],
        "PSP": [".iso", ".cso"],
        "SNES": [".smc", ".sfc", ".srm"]
    }

    categorias = {
        instaladores: [".exe", ".msi"],
        compactados: [".zip", ".rar", ".7z", ".tar", ".gz"],
        documentos: [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        musicas: [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        fotos: [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        videos: [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"]
    }

    for pasta in [instaladores, compactados, documentos, musicas, fotos, videos]:
        os.makedirs(pasta, exist_ok=True)
    for subpasta in roms_subpastas:
        os.makedirs(os.path.join(roms, subpasta), exist_ok=True)

    for arquivo in os.listdir(downloads):
        caminho_arquivo = os.path.join(downloads, arquivo)
        if os.path.isfile(caminho_arquivo):
            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            for subpasta, extensoes in roms_subpastas.items():
                if extensao in extensoes:
                    shutil.move(caminho_arquivo, os.path.join(roms, subpasta, arquivo))
                    break
            else:
                for pasta, extensoes in categorias.items():
                    if extensao in extensoes:
                        shutil.move(caminho_arquivo, os.path.join(pasta, arquivo))
                        break

while True:
    organizar()
    time.sleep(600)
