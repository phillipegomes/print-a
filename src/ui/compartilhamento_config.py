# src/ui/compartilhamento_config.py
# BLOCO 6.1 - Aba de Compartilhamento com checkboxes para envio de imagem

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QCheckBox, QLineEdit, QLabel,
    QPushButton, QHBoxLayout, QMessageBox
)

# 🧠 Explicação:
# Esta interface permite ativar ou desativar opções de compartilhamento:
# - WhatsApp
# - SmugMug (reserva para futuro)
# - Pasta de backup
# O estado é salvo no settings.json do evento

class CompartilhamentoConfig(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.config = self.config_manager.config.setdefault("compartilhamento", {})

        layout = QVBoxLayout(self)

        # WhatsApp
        self.checkbox_whatsapp = QCheckBox("Ativar envio por WhatsApp")
        self.input_numero = QLineEdit()
        self.input_numero.setPlaceholderText("Número (ex: +5511999999999)")

        layout.addWidget(self.checkbox_whatsapp)
        layout.addWidget(self.input_numero)

        # Backup extra
        self.checkbox_backup = QCheckBox("Salvar em pasta de backup adicional")
        self.input_backup = QLineEdit()
        self.input_backup.setPlaceholderText("Caminho completo da pasta")

        layout.addWidget(self.checkbox_backup)
        layout.addWidget(self.input_backup)

        # Botões
        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("Salvar")
        self.btn_padrao = QPushButton("Reverter para padrão")

        self.btn_salvar.clicked.connect(self.salvar)
        self.btn_padrao.clicked.connect(self.reverter)

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_padrao)
        layout.addLayout(botoes)

        self.carregar()

    def carregar(self):
        self.checkbox_whatsapp.setChecked(self.config.get("whatsapp_ativo", False))
        self.input_numero.setText(self.config.get("whatsapp_numero", ""))
        self.checkbox_backup.setChecked(self.config.get("backup_ativo", False))
        self.input_backup.setText(self.config.get("backup_pasta", ""))

    def salvar(self):
        self.config["whatsapp_ativo"] = self.checkbox_whatsapp.isChecked()
        self.config["whatsapp_numero"] = self.input_numero.text()
        self.config["backup_ativo"] = self.checkbox_backup.isChecked()
        self.config["backup_pasta"] = self.input_backup.text()
        self.config_manager.salvar_config()
        QMessageBox.information(self, "Salvo", "Configurações de compartilhamento salvas.")

    def reverter(self):
        self.config.clear()
        self.carregar()
        QMessageBox.information(self, "Revertido", "Valores revertidos para padrão.")
