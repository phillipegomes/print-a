from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

class IAConfig(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.config = self.config_manager.config.setdefault("ia", {})

        layout = QVBoxLayout(self)

        label_estilo = QLabel("Estilo de IA:")
        label_estilo.setToolTip("Escolha o estilo visual que será aplicado às fotos automaticamente.")

        self.combo_estilo = QComboBox()
        self.combo_estilo.addItems(["Cartoon", "Anime", "Ghibli"])
        self.combo_estilo.setToolTip("Exemplo: Cartoon cria um efeito artístico, Ghibli simula animação japonesa.")

        layout.addWidget(label_estilo)
        layout.addWidget(self.combo_estilo)

        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("Salvar")
        self.btn_reverter = QPushButton("Reverter para padrão")

        self.btn_salvar.clicked.connect(self.salvar)
        self.btn_reverter.clicked.connect(self.reverter)

        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_reverter)
        layout.addLayout(botoes)

        self.carregar()

    def carregar(self):
        estilo = self.config.get("estilo", "Cartoon")
        index = self.combo_estilo.findText(estilo)
        self.combo_estilo.setCurrentIndex(index if index >= 0 else 0)

    def salvar(self):
        self.config["estilo"] = self.combo_estilo.currentText()
        self.config_manager.salvar_config()
        QMessageBox.information(self, "IA", "Configuração de IA salva com sucesso.")

    def reverter(self):
        self.config.clear()
        self.config.update({"estilo": "Cartoon"})
        self.carregar()
        QMessageBox.information(self, "IA", "Configuração de IA revertida para o padrão.")
