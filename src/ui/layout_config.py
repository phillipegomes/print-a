# src/ui/layout_config.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QGroupBox
)
from PyQt6.QtCore import Qt

from src.modules.canvas_widget import CanvasWidget
from src.modules.layout_saver import LayoutSaver
from src.modules.layout_templates import aplicar_template


class LayoutConfigWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.saver = LayoutSaver(controller)
        self.setLayout(self._criar_layout_principal())

    def _criar_layout_principal(self):
        layout = QHBoxLayout()

        # 🎨 Barra lateral esquerda
        self.sidebar = QVBoxLayout()
        self._adicionar_botoes_elementos()
        self._adicionar_config_layout()
        layout.addLayout(self.sidebar, 1)

        # 🖼️ Canvas central
        self.canvas = CanvasWidget(self.controller)
        layout.addWidget(self.canvas, 4)

        return layout

    def _adicionar_botoes_elementos(self):
        botoes = [
            ("Adicionar Foto", lambda: self.canvas.adicionar_elemento("foto")),
            ("Adicionar Texto", lambda: self.canvas.adicionar_elemento("texto")),
            ("Adicionar QR", lambda: self.canvas.adicionar_elemento("qr")),
            ("Adicionar Moldura", lambda: self.canvas.adicionar_elemento("moldura")),
            ("Adicionar Logo", lambda: self.canvas.adicionar_elemento("logo")),
            ("Adicionar Forma", lambda: self.canvas.adicionar_elemento("forma")),
            ("Aplicar Template", self._aplicar_template)
        ]
        for nome, func in botoes:
            botao = QPushButton(nome)
            botao.clicked.connect(func)
            self.sidebar.addWidget(botao)

    def _adicionar_config_layout(self):
        grupo = QGroupBox("Configuração do Layout")
        config_layout = QVBoxLayout()

        self.combo_dpi = QComboBox()
        self.combo_dpi.addItems(["300 DPI", "600 DPI"])
        config_layout.addWidget(QLabel("Resolução:"))
        config_layout.addWidget(self.combo_dpi)

        self.combo_tamanho = QComboBox()
        self.combo_tamanho.addItems(["4x6", "5x7", "6x8"])
        config_layout.addWidget(QLabel("Tamanho:"))
        config_layout.addWidget(self.combo_tamanho)

        self.combo_orientacao = QComboBox()
        self.combo_orientacao.addItems(["Horizontal", "Vertical"])
        config_layout.addWidget(QLabel("Orientação:"))
        config_layout.addWidget(self.combo_orientacao)

        grupo.setLayout(config_layout)
        self.sidebar.addWidget(grupo)

    def _aplicar_template(self):
        aplicar_template(self.canvas, self.controller.config_manager)
