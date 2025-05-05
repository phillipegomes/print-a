from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class IAConfigWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel("⚙️ Configurações de IA"))