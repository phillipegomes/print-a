# src/controller/app_controller.py
# BLOCO 2 - Controlador principal: gerencia a troca entre telas

from PyQt6.QtWidgets import QApplication
from src.ui.event_window import EventWindow
from src.ui.main_window import MainWindow

class AppController:
    def __init__(self):
        self.app = None  # Definido em main.py
        self.evento_atual = None
        self.janela_atual = None

    def start(self):
        self.abrir_event_window()

    def abrir_event_window(self):
        if self.janela_atual:
            self.janela_atual.close()
        self.janela_atual = EventWindow(controller=self)
        self.janela_atual.show()

    def abrir_main_window(self):
        if not self.evento_atual:
            return
        if self.janela_atual:
            self.janela_atual.close()
        self.janela_atual = MainWindow(controller=self)
        self.janela_atual.show()
