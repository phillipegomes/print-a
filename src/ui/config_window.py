# src/ui/config_window.py
# BLOCO 6.2 - Integração da aba Compartilhamento na janela de configurações

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget
)
from src.ui.compartilhamento_config import CompartilhamentoConfig

# 🧠 Explicação:
# Este arquivo agrega todas as abas de configuração. Agora incluímos a nova aba de compartilhamento,
# que oferece controles para WhatsApp e backup, com botões de salvar e reverter.

class ConfigWindow(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.setWindowTitle("Configurações do Evento")
        self.setMinimumSize(600, 400)

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Aba: Compartilhamento
        self.compartilhamento = CompartilhamentoConfig(config_manager)
        self.tabs.addTab(self.compartilhamento, "Compartilhamento")

        # Futuras abas: Impressão, Layout, IA, Monitoramento...
        # self.tabs.addTab(OutraAba(...), "Impressão")

        layout.addWidget(self.tabs)
        self.setLayout(layout)
