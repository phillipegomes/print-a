# src/ui/main_actions.py
# BLOCO 3 - Ações da galeria: carregar imagens, imprimir, excluir, enviar

import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox

EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png")

def carregar_imagens(pasta_fotos):
    if not os.path.exists(pasta_fotos):
        return []
    return sorted([
        os.path.join(pasta_fotos, f)
        for f in os.listdir(pasta_fotos)
        if f.lower().endswith(EXTENSOES_VALIDAS)
    ], key=os.path.getmtime)

def imprimir_foto(caminho, copias=1):
    print(f"[IMPRIMIR] {copias}x - {caminho}")
    # Integração com printer_manager aqui futuramente


def excluir_foto(caminho):
    try:
        os.remove(caminho)
        print(f"[EXCLUIR] {caminho}")
        return True
    except Exception as e:
        print(f"[ERRO] ao excluir {caminho}: {e}")
        QMessageBox.warning(None, "Erro", f"Erro ao excluir a imagem:\n{e}")
        return False
