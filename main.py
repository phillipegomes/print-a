# main.py – Arquivo de entrada principal do sistema

import sys
from PyQt6.QtWidgets import QApplication
from src.controller.app_controller import AppController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.abrir_event_window()  # Abre a tela de eventos ao iniciar
    sys.exit(app.exec())
