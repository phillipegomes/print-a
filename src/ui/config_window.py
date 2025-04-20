from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget, QLabel, QHBoxLayout,
    QPushButton, QCheckBox, QMessageBox, QApplication
)
from PyQt6.QtCore import Qt
import os
import json
import webbrowser
import sys


class ConfigWindow(QWidget):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Print A – Configurações")
        self.setMinimumSize(800, 600)

        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()

        # Verifica se há config_manager no controller
        config_manager = getattr(controller, 'config_manager', None)

        # Abas reais
        self.tabs.addTab(self.init_aba_geral(), "⚙️ Geral")

        # Abas placeholder (em construção)
        self.tabs.addTab(self.criar_aba_placeholder("🖨️ Impressão"), "Impressão")
        self.tabs.addTab(self.criar_aba_placeholder("🎨 Layout"), "Layout")
        self.tabs.addTab(self.criar_aba_placeholder("🤖 IA"), "IA")
        self.tabs.addTab(self.criar_aba_placeholder("📲 Compartilhamento"), "Compartilhamento")
        self.tabs.addTab(self.criar_aba_placeholder("☁️ SmugMug"), "SmugMug")
        self.tabs.addTab(self.criar_aba_placeholder("📊 Relatórios"), "Relatórios")

        layout.addWidget(self.tabs)

    def criar_aba_placeholder(self, titulo):
        aba = QWidget()
        layout = QVBoxLayout(aba)
        label = QLabel(f"{titulo} – conteúdo em construção")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 18px; padding: 20px;")

        botoes = QHBoxLayout()
        btn_salvar = QPushButton("💾 Salvar")
        btn_reset = QPushButton("🔄 Reverter para padrão")
        for btn in [btn_salvar, btn_reset]:
            btn.setFixedHeight(36)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            botoes.addWidget(btn)

        layout.addWidget(label)
        layout.addLayout(botoes)
        layout.addStretch()
        return aba

    def init_aba_geral(self):
        aba = QWidget()
        layout = QVBoxLayout(aba)

        # Label e botão de update
        label = QLabel("🔄 Verificar atualizações disponíveis:")
        btn_update = QPushButton("Verificar atualizações no GitHub")
        btn_update.clicked.connect(lambda: webbrowser.open("https://github.com/phillipegomes/print-a"))

        # Checkboxes
        self.check_backup = QCheckBox("Fazer backup automático antes de excluir ou renomear eventos")
        self.check_backup.setChecked(True)

        self.check_limpeza = QCheckBox("Limpar automaticamente eventos vazios após 24h")
        self.check_limpeza.setChecked(True)

        # Botões
        btn_salvar = QPushButton("💾 Salvar")
        btn_reverter = QPushButton("🔄 Reverter para padrão")
        btn_salvar.clicked.connect(self.salvar_geral)
        btn_reverter.clicked.connect(self.reverter_padrao)

        botoes = QHBoxLayout()
        botoes.addWidget(btn_salvar)
        botoes.addWidget(btn_reverter)

        # Monta o layout da aba
        layout.addWidget(label)
        layout.addWidget(btn_update)
        layout.addSpacing(20)
        layout.addWidget(self.check_backup)
        layout.addWidget(self.check_limpeza)
        layout.addSpacing(30)
        layout.addLayout(botoes)
        layout.addStretch()

        return aba

    def salvar_geral(self):
        config = {
            "backup_automatico": self.check_backup.isChecked(),
            "limpeza_automatica": self.check_limpeza.isChecked()
        }
        os.makedirs("config", exist_ok=True)
        with open("config/geral.json", "w") as f:
            json.dump(config, f, indent=4)
        QMessageBox.information(self, "Configurações", "Configurações salvas com sucesso!")

    def reverter_padrao(self):
        self.check_backup.setChecked(True)
        self.check_limpeza.setChecked(True)
        QMessageBox.information(self, "Configurações", "Valores padrão restaurados.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConfigWindow()
    window.show()
    sys.exit(app.exec())
