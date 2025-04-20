# src/controller/app_controller.py

import os
from src.ui.event_window import EventWindow
from src.ui.main_window import MainWindow
from src.ui.config_window import ConfigWindow
from src.ui.gallery_window import GalleryWindow  # ✅ Import necessário
from src.modules.config_manager import ConfigManager

class AppController:
    def __init__(self):
        self.event_window = EventWindow(self)
        self.main_window = None
        self.config_window = None
        self.gallery_window = None
        self.config_manager = None
        self.nome_evento_atual = ""

    def abrir_event_window(self):
        """
        Abre a janela principal de eventos e fecha outras, se existirem.
        """
        self.event_window.show()
        if self.main_window:
            self.main_window.close()

    def abrir_main_window(self, caminho_config):
        """
        Abre a tela principal do evento com base no settings.json selecionado.
        """
        self.config_manager = ConfigManager(caminho_config)
        self.nome_evento_atual = caminho_config.split("/")[1]
        self.main_window = MainWindow(self, caminho_config)
        self.main_window.show()
        self.event_window.close()

    def abrir_configuracoes(self, settings_path):
        """
        Abre a janela de configurações com base no caminho fornecido.
        """
        if not self.config_manager:
            print("[ERRO] Nenhuma configuração carregada.")
            return
        self.config_window = ConfigWindow(self.config_manager)
        self.config_window.show()

    def voltar_para_eventos(self):
        """
        Fecha a janela atual e retorna à janela de seleção de eventos.
        """
        if self.main_window:
            self.main_window.close()
        if self.gallery_window:
            self.gallery_window.close()
        self.abrir_event_window()

    def abrir_galeria(self):
        """
        Abre a janela da galeria, passando as informações do evento atual.
        """
        if not self.config_manager or not self.main_window:
            print("[ERRO] Nenhuma configuração carregada.")
            return

        # ✅ SUPREMO FIX
        evento_path = os.path.dirname(os.path.dirname(self.main_window.settings_path))
        self.gallery_window = GalleryWindow(evento_path, self.config_manager)
        self.gallery_window.show()
