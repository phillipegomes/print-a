# src/ui/main_window.py
# BLOCO 2 - Janela principal do evento (layout inicial funcional e refinado)

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(f"PrintA - Evento: {self.controller.evento_atual}")
        self.setMinimumSize(800, 500)

        layout = QVBoxLayout(self)

        self.label_evento = QLabel(f"Evento atual: {self.controller.evento_atual}")
        self.label_evento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_evento.setStyleSheet("font-size: 18px; margin-top: 20px;")

        self.btn_voltar = QPushButton("Voltar para eventos")
        self.btn_voltar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_voltar.setFixedWidth(200)
        self.btn_voltar.setStyleSheet("margin-top: 40px; padding: 10px; font-size: 14px;")
        self.btn_voltar.clicked.connect(self.controller.abrir_event_window)

        layout.addWidget(self.label_evento)
        layout.addWidget(self.btn_voltar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet("background-color: #f9f9f9;")
