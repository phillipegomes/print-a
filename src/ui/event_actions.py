# src/ui/event_actions.py
# BLOCO 2 - Funções de gerenciamento de eventos (CRUD)

import os
import shutil
import json
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
EVENTOS_DIR = os.path.join(BASE_DIR, "eventos")
CONFIG_TEMPLATE = os.path.join(BASE_DIR, "config", "settings_default.json")

os.makedirs(EVENTOS_DIR, exist_ok=True)

def listar_eventos_ordenados():
    eventos = []
    for nome in os.listdir(EVENTOS_DIR):
        caminho = os.path.join(EVENTOS_DIR, nome)
        if os.path.isdir(caminho):
            data = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d-%m-%Y")
            eventos.append((nome, data))
    eventos.sort(key=lambda x: x[0].lower())  # ordena por nome
    return eventos

def criar_evento(nome):
    caminho = os.path.join(EVENTOS_DIR, nome)
    if os.path.exists(caminho):
        QMessageBox.warning(None, "Erro", f"O evento '{nome}' já existe.")
        return False
    os.makedirs(os.path.join(caminho, "Fotos"))
    os.makedirs(os.path.join(caminho, "Impressas"))
    os.makedirs(os.path.join(caminho, "config"))
    shutil.copy(CONFIG_TEMPLATE, os.path.join(caminho, "config", "settings.json"))
    return True

def abrir_evento(nome, controller):
    controller.evento_atual = nome
    controller.abrir_main_window()

def duplicar_evento(nome):
    origem = os.path.join(EVENTOS_DIR, nome)
    novo_nome = f"{nome} (Cópia)"
    destino = os.path.join(EVENTOS_DIR, novo_nome)
    contador = 2
    while os.path.exists(destino):
        novo_nome = f"{nome} (Cópia {contador})"
        destino = os.path.join(EVENTOS_DIR, novo_nome)
        contador += 1
    shutil.copytree(origem, destino)
    return True

def renomear_evento(nome_antigo, novo_nome):
    origem = os.path.join(EVENTOS_DIR, nome_antigo)
    destino = os.path.join(EVENTOS_DIR, novo_nome)
    if os.path.exists(destino):
        QMessageBox.warning(None, "Erro", f"O evento '{novo_nome}' já existe.")
        return False
    os.rename(origem, destino)
    return True

def excluir_evento(nome):
    caminho = os.path.join(EVENTOS_DIR, nome)
    if not os.path.exists(caminho):
        return False
    shutil.rmtree(caminho)
    return True
