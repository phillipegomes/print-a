
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class GeralConfigWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()
        layout.addWidget(QLabel("⚙️ Configurações Gerais do Sistema"))

        btn_atualizacoes = QPushButton("🔄 Verificar Atualizações (em breve)")
        btn_backup = QPushButton("🛡️ Backup automático (em breve)")
        btn_limpar = QPushButton("🧹 Limpar cache e eventos vazios (em breve)")

        layout.addWidget(btn_atualizacoes)
        layout.addWidget(btn_backup)
        layout.addWidget(btn_limpar)

        self.setLayout(layout)
