# src/ui/layout_config.py
# BLOCO 11.3 – Botão de Preview na aba Layout

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox, QCheckBox
)
from src.ui.layout_preview import LayoutPreview
import os

class LayoutConfig(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.config = self.config_manager.config.setdefault("layout", {})

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Escolha o modelo de layout:"))
        self.combo_modelo = QComboBox()
        self.combo_modelo.addItems(["Padrão 1 (vertical)", "Padrão 2 (horizontal)", "Padrão 3 (duas fotos)"])
        layout.addWidget(self.combo_modelo)

        layout.addWidget(QLabel("Posição da imagem no layout:"))
        self.combo_posicao = QComboBox()
        self.combo_posicao.addItems(["Centro", "Superior", "Inferior"])
        layout.addWidget(self.combo_posicao)

        self.check_borda = QCheckBox("Adicionar borda decorativa")
        layout.addWidget(self.check_borda)

        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.clicked.connect(self.salvar)

        self.btn_reverter = QPushButton("Reverter")
        self.btn_reverter.clicked.connect(self.reverter)

        self.btn_preview = QPushButton("Visualizar Layout")
        self.btn_preview.clicked.connect(self.abrir_preview)

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_reverter)
        botoes.addWidget(self.btn_preview)
        layout.addLayout(botoes)

        self.carregar()

    def carregar(self):
        self.combo_modelo.setCurrentIndex(self.config.get("modelo", 0))
        self.combo_posicao.setCurrentIndex(self.config.get("posicao", 0))
        self.check_borda.setChecked(self.config.get("borda", False))

    def salvar(self):
        self.config["modelo"] = self.combo_modelo.currentIndex()
        self.config["posicao"] = self.combo_posicao.currentIndex()
        self.config["borda"] = self.check_borda.isChecked()
        self.config_manager.salvar_config()

    def reverter(self):
        self.config.clear()
        self.carregar()

    def abrir_preview(self):
        caminho_foto = "assets/teste.jpg"
        modelo = self.combo_modelo.currentIndex()
        layout_file = f"assets/layouts/layout{modelo + 1}.png"
        posicao = self.combo_posicao.currentText()
        borda = self.check_borda.isChecked()

        if not os.path.exists(caminho_foto) or not os.path.exists(layout_file):
            print("[Preview] Arquivo de teste ou layout não encontrado.")
            return

        self.preview_window = LayoutPreview(caminho_foto, layout_file, posicao, borda)
        self.preview_window.show()
