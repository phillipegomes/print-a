# ✅ SUPREMO FIX – CanvasConfigWidget
# src/ui/canvas_config.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QHBoxLayout
from PyQt6.QtCore import Qt

class CanvasConfigWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setMinimumSize(800, 600)

        layout = QVBoxLayout()

        # Título
        titulo = QLabel("🖼️ Configurações do Canvas")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # DPI
        dpi_layout = QHBoxLayout()
        dpi_label = QLabel("Resolução (DPI):")
        self.dpi_combo = QComboBox()
        self.dpi_combo.addItems(["300", "600"])
        dpi_layout.addWidget(dpi_label)
        dpi_layout.addWidget(self.dpi_combo)
        layout.addLayout(dpi_layout)

        # Tamanho do Papel
        tamanho_layout = QHBoxLayout()
        tamanho_label = QLabel("Tamanho do Papel:")
        self.tamanho_combo = QComboBox()
        self.tamanho_combo.addItems(["4x6", "5x7", "6x8"])
        tamanho_layout.addWidget(tamanho_label)
        tamanho_layout.addWidget(self.tamanho_combo)
        layout.addLayout(tamanho_layout)

        # Orientação
        orientacao_layout = QHBoxLayout()
        orientacao_label = QLabel("Orientação:")
        self.orientacao_combo = QComboBox()
        self.orientacao_combo.addItems(["Horizontal", "Vertical"])
        orientacao_layout.addWidget(orientacao_label)
        orientacao_layout.addWidget(self.orientacao_combo)
        layout.addLayout(orientacao_layout)

        # Placeholder visual
        aviso = QLabel("⚠️ Funções avançadas serão adicionadas em breve.")
        aviso.setStyleSheet("color: gray;")
        aviso.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(aviso)

        self.setLayout(layout)
