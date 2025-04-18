# src/ui/main_actions.py
# BLOCO 3 (atualizado) - Ações da galeria com impressão real via printer_manager

import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox
from src.modules.printer_manager import imprimir  # Importa função real

EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png")

# 🧠 carrega todas as imagens da pasta do evento, ordenadas por data
# Evita arquivos inválidos

def carregar_imagens(pasta_fotos):
    if not os.path.exists(pasta_fotos):
        return []
    return sorted([
        os.path.join(pasta_fotos, f)
        for f in os.listdir(pasta_fotos)
        if f.lower().endswith(EXTENSOES_VALIDAS)
    ], key=os.path.getmtime)

# 🧠 usa o printer_manager real para imprimir (com log e verificação de caminho)

def imprimir_foto(caminho, copias=1):
    return imprimir(caminho, copias)

# 🧠 exclui uma imagem e emite alerta visual se houver erro

def excluir_foto(caminho):
    try:
        os.remove(caminho)
        print(f"[EXCLUIR] {caminho}")
        return True
    except Exception as e:
        print(f"[ERRO] ao excluir {caminho}: {e}")
        QMessageBox.warning(None, "Erro", f"Erro ao excluir a imagem:\n{e}")
        return False
