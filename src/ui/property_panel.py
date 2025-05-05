from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QSpinBox,
    QComboBox, QFormLayout
)
from PyQt6.QtCore import Qt


class PropertyPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(250)
        self.setWindowTitle("Propriedades do Item")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.title = QLabel("🛠️ Propriedades")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.form_layout = QFormLayout()

        self.x_input = QSpinBox()
        self.x_input.setRange(0, 9999)
        self.form_layout.addRow("X:", self.x_input)

        self.y_input = QSpinBox()
        self.y_input.setRange(0, 9999)
        self.form_layout.addRow("Y:", self.y_input)

        self.width_input = QSpinBox()
        self.width_input.setRange(1, 9999)
        self.form_layout.addRow("Largura:", self.width_input)

        self.height_input = QSpinBox()
        self.height_input.setRange(1, 9999)
        self.form_layout.addRow("Altura:", self.height_input)

        self.rotation_input = QSpinBox()
        self.rotation_input.setRange(0, 360)
        self.form_layout.addRow("Rotação:", self.rotation_input)

        self.alignment_input = QComboBox()
        self.alignment_input.addItems(["Esquerda", "Centro", "Direita"])
        self.form_layout.addRow("Alinhamento:", self.alignment_input)

        self.id_input = QLineEdit()
        self.form_layout.addRow("ID do Item:", self.id_input)

        self.layout.addLayout(self.form_layout)

    def atualizar_com_dados(self, dados: dict):
        self.x_input.setValue(dados.get("x", 0))
        self.y_input.setValue(dados.get("y", 0))
        self.width_input.setValue(dados.get("width", 100))
        self.height_input.setValue(dados.get("height", 100))
        self.rotation_input.setValue(dados.get("rotation", 0))
        alinhamento = dados.get("alignment", "Centro")
        index = self.alignment_input.findText(alinhamento)
        if index >= 0:
            self.alignment_input.setCurrentIndex(index)
        self.id_input.setText(dados.get("id", ""))

    def obter_dados(self) -> dict:
        return {
            "x": self.x_input.value(),
            "y": self.y_input.value(),
            "width": self.width_input.value(),
            "height": self.height_input.value(),
            "rotation": self.rotation_input.value(),
            "alignment": self.alignment_input.currentText(),
            "id": self.id_input.text()
        }
