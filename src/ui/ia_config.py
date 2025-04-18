# src/ui/ia_config.py
# BLOCO 10B - Conecta botão "Aplicar Teste" ao módulo de IA com imagem de teste

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox,
    QComboBox, QMessageBox
)
from PyQt6.QtGui import QPixmap
import os
from src.modules.image_processor import aplicar_ia_em_imagem

class IAConfig(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.config = self.config_manager.config.setdefault("ia", {})

        layout = QVBoxLayout(self)

        self.checkbox_ativa = QCheckBox("Ativar IA no processamento de imagem")
        layout.addWidget(self.checkbox_ativa)

        self.combo_estilo = QComboBox()
        self.estilos = ["Cartoon", "Ghibli", "Anime"]
        self.combo_estilo.addItems(self.estilos)
        layout.addWidget(QLabel("Estilo de IA:") )
        layout.addWidget(self.combo_estilo)

        self.preview = QLabel()
        self.preview.setFixedSize(150, 150)
        self.preview.setScaledContents(True)
        layout.addWidget(QLabel("Prévia do estilo selecionado:"))
        layout.addWidget(self.preview)

        self.combo_estilo.currentTextChanged.connect(self.atualizar_preview)
        self.atualizar_preview(self.combo_estilo.currentText())

        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.clicked.connect(self.salvar)

        self.btn_reverter = QPushButton("Reverter")
        self.btn_reverter.clicked.connect(self.reverter)

        self.btn_teste = QPushButton("Aplicar Teste")
        self.btn_teste.clicked.connect(self.aplicar_teste)

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_reverter)
        botoes.addWidget(self.btn_teste)
        layout.addLayout(botoes)

        self.carregar()

    def atualizar_preview(self, estilo):
        caminho = f"assets/ia/{estilo.lower()}.jpg"
        if os.path.exists(caminho):
            self.preview.setPixmap(QPixmap(caminho))
        else:
            self.preview.clear()

    def carregar(self):
        self.checkbox_ativa.setChecked(self.config.get("ativa", False))
        estilo = self.config.get("estilo", "Cartoon")
        if estilo in self.estilos:
            self.combo_estilo.setCurrentText(estilo)
        self.atualizar_preview(estilo)

    def salvar(self):
        self.config["ativa"] = self.checkbox_ativa.isChecked()
        self.config["estilo"] = self.combo_estilo.currentText()
        self.config_manager.salvar_config()
        QMessageBox.information(self, "Salvo", "Configuração de IA salva com sucesso.")

    def reverter(self):
        self.config.clear()
        self.carregar()
        QMessageBox.information(self, "Revertido", "Valores de IA revertidos para padrão.")

    def aplicar_teste(self):
        if not self.checkbox_ativa.isChecked():
            QMessageBox.warning(self, "IA desativada", "A IA está desativada. Ative-a para testar.")
            return

        estilo = self.combo_estilo.currentText()
        entrada = "assets/teste.jpg"
        saida = "assets/teste_processado.jpg"

        sucesso = aplicar_ia_em_imagem(entrada, saida, estilo)
        if sucesso:
            QMessageBox.information(self, "Teste aplicado", f"Estilo '{estilo}' aplicado na imagem de teste.")
        else:
            QMessageBox.critical(self, "Erro", "Falha ao aplicar IA na imagem de teste.")
