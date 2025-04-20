from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox,
    QCheckBox, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt

class ImpressaoConfig(QWidget):
    def __init__(self, config_manager):
        super().__init__()
        self.config_manager = config_manager
        self.config = self.config_manager.config.setdefault("impressao", {})

        layout = QVBoxLayout(self)

        # Impressora
        label_impressora = QLabel("Impressora:")
        self.combo_impressora = QComboBox()
        self.combo_impressora.addItems(["CS2", "BRA21", "HITE", "Kodak", "InJoy"])
        layout.addWidget(label_impressora)
        layout.addWidget(self.combo_impressora)

        # Formato de papel
        label_papel = QLabel("Formato de papel:")
        self.combo_papel = QComboBox()
        self.combo_papel.addItems(["10x15", "15x20", "15x21", "13x18"])
        layout.addWidget(label_papel)
        layout.addWidget(self.combo_papel)

        # Número de cópias padrão
        label_copias = QLabel("Cópias padrão por imagem:")
        self.spin_copias = QSpinBox()
        self.spin_copias.setMinimum(1)
        self.spin_copias.setMaximum(10)
        layout.addWidget(label_copias)
        layout.addWidget(self.spin_copias)

        # AirPrint
        self.chk_airprint = QCheckBox("Ativar servidor AirPrint (CUPS + Avahi)")
        layout.addWidget(self.chk_airprint)

        # Impressão automática
        self.chk_auto = QCheckBox("Imprimir automaticamente após processar")
        layout.addWidget(self.chk_auto)

        # Limitar impressões por imagem
        label_limite = QLabel("Máximo de impressões por imagem:")
        self.spin_limite = QSpinBox()
        self.spin_limite.setMinimum(1)
        self.spin_limite.setMaximum(20)
        layout.addWidget(label_limite)
        layout.addWidget(self.spin_limite)

        # Botões
        botoes = QHBoxLayout()
        self.btn_salvar = QPushButton("💾 Salvar")
        self.btn_reverter = QPushButton("🔄 Reverter para padrão")
        self.btn_salvar.clicked.connect(self.salvar)
        self.btn_reverter.clicked.connect(self.reverter)
        botoes.addWidget(self.btn_salvar)
        botoes.addWidget(self.btn_reverter)
        layout.addLayout(botoes)

        self.carregar()

    def carregar(self):
        self.combo_impressora.setCurrentText(self.config.get("modelo", "CS2"))
        self.combo_papel.setCurrentText(self.config.get("papel", "10x15"))
        self.spin_copias.setValue(self.config.get("copias", 1))
        self.chk_airprint.setChecked(self.config.get("airprint", False))
        self.chk_auto.setChecked(self.config.get("auto", False))
        self.spin_limite.setValue(self.config.get("limite", 3))

    def salvar(self):
        self.config["modelo"] = self.combo_impressora.currentText()
        self.config["papel"] = self.combo_papel.currentText()
        self.config["copias"] = self.spin_copias.value()
        self.config["airprint"] = self.chk_airprint.isChecked()
        self.config["auto"] = self.chk_auto.isChecked()
        self.config["limite"] = self.spin_limite.value()
        self.config_manager.salvar_config()
        QMessageBox.information(self, "Impressão", "Configurações salvas com sucesso.")

    def reverter(self):
        self.config.clear()
        self.config.update({
            "modelo": "CS2",
            "papel": "10x15",
            "copias": 1,
            "airprint": False,
            "auto": False,
            "limite": 3
        })
        self.carregar()
        QMessageBox.information(self, "Impressão", "Revertido para configurações padrão.")
