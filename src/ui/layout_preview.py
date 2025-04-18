# src/ui/layout_preview.py
# BLOCO 11.2 – Preview do Layout com aplicação de moldura estilo photobooth

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt
from PIL import Image, ImageQt, ImageOps
import os

def aplicar_layout_em_imagem(caminho_foto, caminho_layout, posicao="Centro", borda=False):
    """
    Aplica um layout PNG transparente sobre uma imagem base.
    """
    try:
        base = Image.open(caminho_foto).convert("RGBA")
        layout = Image.open(caminho_layout).convert("RGBA")

        if borda:
            base = ImageOps.expand(base, border=20, fill="white")
            layout = layout.resize(base.size)

        else:
            layout = layout.resize(base.size)

        combinada = Image.alpha_composite(base, layout)
        return combinada

    except Exception as e:
        print(f"[LAYOUT] Erro ao aplicar layout: {e}")
        return None

class LayoutPreview(QWidget):
    def __init__(self, caminho_foto, caminho_layout, posicao="Centro", borda=False):
        super().__init__()
        self.setWindowTitle("Preview do Layout")
        self.setMinimumSize(400, 400)

        layout = QVBoxLayout(self)
        self.label = QLabel("Pré-visualização")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        imagem_resultado = aplicar_layout_em_imagem(caminho_foto, caminho_layout, posicao, borda)
        if imagem_resultado:
            qt_img = ImageQt.ImageQt(imagem_resultado)
            pixmap = QPixmap.fromImage(QImage(qt_img))
            self.label.setPixmap(pixmap.scaled(380, 380, Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.label.setText("Erro ao carregar imagem com layout.")
