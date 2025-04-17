from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class EventWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("PrintA - Meus Eventos")
        self.setMinimumSize(800, 600)

        layout = QVBoxLayout()
        label = QLabel("Bem-vindo ao PrintA!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn = QPushButton("Simular Abertura")
        btn.clicked.connect(self.simular_acao)

        layout.addWidget(label)
        layout.addWidget(btn)
        self.setLayout(layout)

    def simular_acao(self):
        print("Simulando ação de evento")
