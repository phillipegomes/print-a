
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt6.QtCore import Qt


class RelatorioConfigWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.log_path = "logs/printa.log"

        layout = QVBoxLayout()
        layout.addWidget(QLabel("📋 Relatório de Ações e Erros do Sistema"))

        self.text_log = QTextEdit()
        self.text_log.setReadOnly(True)
        self.text_log.setMinimumHeight(400)
        layout.addWidget(self.text_log)

        btn_refresh = QPushButton("🔄 Atualizar Relatório")
        btn_refresh.clicked.connect(self.carregar_logs)
        layout.addWidget(btn_refresh)

        self.setLayout(layout)
        self.carregar_logs()

    def carregar_logs(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as f:
                conteudo = f.read()
                self.text_log.setPlainText(conteudo)
        else:
            self.text_log.setPlainText("Nenhum log encontrado em logs/printa.log")
