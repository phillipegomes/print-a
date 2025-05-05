# ✅ src/ui/layout_preview.py
import os
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from src.modules.layout_renderer import LayoutRenderer

class LayoutPreviewWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.config = controller.config_manager.config

        self.setLayout(self._criar_layout())
        self._renderizar_preview()

    def _criar_layout(self):
        layout = QVBoxLayout()

        self.label_preview = QLabel("Prévia do layout")
        self.label_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_preview.setStyleSheet("border: 2px dashed gray; padding: 10px")

        self.btn_atualizar = QPushButton("🔄 Atualizar Prévia")
        self.btn_atualizar.clicked.connect(self._renderizar_preview)

        layout.addWidget(self.label_preview)
        layout.addWidget(self.btn_atualizar)
        return layout

    def _renderizar_preview(self):
        elementos = self.controller.canvas.get_elementos()
        renderer = LayoutRenderer(self.config)
        caminho_imagem = renderer.renderizar(elementos, nome_base="preview_temp")

        if os.path.exists(caminho_imagem):
            pixmap = QPixmap(caminho_imagem)
            self.label_preview.setPixmap(pixmap.scaled(
                600, 400,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            ))

# ✅ Exporta função para uso no processamento real da imagem capturada

def aplicar_layout_em_imagem(caminho_imagem, config):
    renderer = LayoutRenderer(config)
    elementos = config.get("layout", [])
    return renderer.renderizar(elementos, caminho_base=caminho_imagem)
