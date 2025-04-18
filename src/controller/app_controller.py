# src/controller/app_controller.py
# AppController com FileWatcher ativo para evento de teste

import os
import json
from PyQt6.QtWidgets import QWidget, QStackedLayout
from src.ui.main_window import MainWindow
from src.modules.file_watcher import FileWatcher

class AppController(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Print A - Evento Teste")
        self.setGeometry(100, 100, 1200, 800)

        self.layout = QStackedLayout(self)

        # Caminho do evento de teste (você pode trocar depois)
        self.evento_nome = "TesteEvent"
        self.evento_path = os.path.join("eventos", self.evento_nome)
        self.config_path = os.path.join(self.evento_path, "config", "settings.json")

        # Carrega as configurações do evento
        self.config = self.carregar_config()

        # Tela principal com galeria (ainda pode estar básica)
        self.main_window = MainWindow(self.evento_path, self.config)
        self.layout.addWidget(self.main_window)

        # Inicia o monitoramento de novas fotos
        self.iniciar_monitoramento()

    def carregar_config(self):
        if not os.path.exists(self.config_path):
            print(f"[CONFIG] Arquivo não encontrado: {self.config_path}")
            return {}
        try:
            with open(self.config_path, "r") as f:
                print(f"[CONFIG] Configurações carregadas: {self.config_path}")
                return json.load(f)
        except Exception as e:
            print(f"[CONFIG] Erro ao carregar config: {e}")
            return {}

    def iniciar_monitoramento(self):
        pasta_fotos = os.path.join(self.evento_path, "Fotos")
        self.monitor = FileWatcher(
            pasta_fotos=pasta_fotos,
            config=self.config,
            callback=self.main_window.imagem_processada_callback if hasattr(self.main_window, "imagem_processada_callback") else None
        )
        self.monitor.iniciar()
        print(f"[MONITOR] Observando {pasta_fotos}...")
