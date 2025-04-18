# src/ui/config_window.py
# BLOCO 9.3 - Integração da aba IA no painel de configurações

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout, QPushButton
)
from src.ui.compartilhamento_config import CompartilhamentoConfig
from src.ui.ia_config import IAConfig

class ConfigWindow(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.setWindowTitle("Configurações do Evento")
        self.setMinimumSize(600, 400)
        self.config_manager = config_manager

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Abas de configuração
        self.tab_compartilhamento = CompartilhamentoConfig(config_manager)
        self.tab_ia = IAConfig(config_manager)

        self.tabs.addTab(self.tab_compartilhamento, "Compartilhamento")
        self.tabs.addTab(self.tab_ia, "IA")

        layout.addWidget(self.tabs)

        # Tooltips e ações inferiores
        self.tooltip_label = QLabel("ℹ️ Passe o mouse sobre os campos para ver a descrição.")
        self.tooltip_label.setStyleSheet("color: #666; font-size: 12px; margin-top: 6px;")

        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("Salvar Todas")
        self.btn_salvar.clicked.connect(self.salvar_todas)

        self.btn_reverter = QPushButton("Reverter Tudo")
        self.btn_reverter.clicked.connect(self.reverter_todas)

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_reverter)

        layout.addWidget(self.tooltip_label)
        layout.addLayout(botoes)
        self.setLayout(layout)

    def salvar_todas(self):
        if hasattr(self.tab_compartilhamento, "salvar"):
            self.tab_compartilhamento.salvar()
        if hasattr(self.tab_ia, "salvar"):
            self.tab_ia.salvar()

    def reverter_todas(self):
        if hasattr(self.tab_compartilhamento, "reverter"):
            self.tab_compartilhamento.reverter()
        if hasattr(self.tab_ia, "reverter"):
            self.tab_ia.reverter()
