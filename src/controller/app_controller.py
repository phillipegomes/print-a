# src/controller/app_controller.py
from src.ui.event_window import EventWindow
from src.ui.main_window import MainWindow
from src.modules.config_manager import ConfigManager

class AppController:
    def __init__(self):
        caminho_config = "eventos/TesteEvent/config/settings.json"
        self.config_manager = ConfigManager(caminho_config)
        self.event_window = EventWindow(controller=self)
        self.main_window = None

    def start(self):
        self.event_window.show()

    def abrir_main_window(self, config):
        self.main_window = MainWindow(evento_path="eventos/TesteEvent", controller=self)
        self.main_window.show()
        self.event_window.close()
