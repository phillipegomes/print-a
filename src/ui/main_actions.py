# src/ui/main_actions.py

import os
from PyQt6.QtWidgets import QMessageBox
from src.modules.print_counter import PrintCounter
from src.modules.whatsapp_sender import enviar_por_whatsapp
from src.modules.backup_manager import salvar_em_backup
from src.modules.config_manager import ConfigManager
from src.modules.printer_manager import imprimir_imagem
from src.ui.layout_preview import aplicar_layout_em_imagem

def carregar_imagens(pasta):
    """
    Carrega apenas imagens válidas da pasta especificada.
    Ignora arquivos ocultos e pastas inválidas.
    """

    # ✅ SUPREMO BLOCK: Verifica existência da pasta
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        return []

    arquivos_validos = []
    for arquivo in sorted(os.listdir(pasta)):
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png')) and not arquivo.startswith('.'):
            arquivos_validos.append(os.path.join(pasta, arquivo))

    return arquivos_validos

def imprimir_foto(caminho_imagem, config, parent=None):
    if not os.path.exists(caminho_imagem):
        QMessageBox.warning(parent, "Erro", "Imagem não encontrada.")
        return

    imagem_com_layout = aplicar_layout_em_imagem(caminho_imagem, config)
    imprimir_imagem(imagem_com_layout, config)
    PrintCounter.incrementar(caminho_imagem)

def excluir_foto(caminho_imagem, parent=None):
    if os.path.exists(caminho_imagem):
        salvar_em_backup(caminho_imagem, motivo="Exclusão manual")
        try:
            os.remove(caminho_imagem)
        except Exception as e:
            QMessageBox.critical(parent, "Erro", f"Erro ao excluir imagem: {e}")
    else:
        QMessageBox.warning(parent, "Erro", "Imagem não encontrada.")

def enviar_whatsapp(caminho_imagem, config, parent=None):
    if not os.path.exists(caminho_imagem):
        QMessageBox.warning(parent, "Erro", "Imagem não encontrada.")
        return

    try:
        enviar_por_whatsapp(caminho_imagem, config)
    except Exception as e:
        QMessageBox.critical(parent, "Erro", f"Erro ao enviar por WhatsApp: {e}")
