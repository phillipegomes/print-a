# src/controller/app_controller.py
# BLOCO FIX – Garantir que config_manager exista antes de chamar MainWindow

import os
from src.ui.event_window import EventWindow
from src.ui.main_window import MainWindow
from src.modules.config_loader import carregar_config_evento
from src.modules.file_watcher import FileWatcher

class AppController:
    def __init__(self):
        self.evento_path = "eventos/TesteEvent"
        self.config_path = os.path.join(self.evento_path, "config", "settings.json")
        
        # ✅ Criação do config_manager ANTES de qualquer uso
        from src.modules.config_manager import ConfigManager
        self.config_manager = ConfigManager(self.config_path)

        self.config = self.config_manager.config
        
        # ✅ Inicialização correta do monitoramento com callback
        self.monitor = FileWatcher(
            pasta_fotos=os.path.join(self.evento_path, "Fotos"),
            config=self.config,
            callback=self.pipeline_processamento  # ← já definido na própria classe
        )
        self.monitor.iniciar()

        # ✅ Cria a janela principal com o controller contendo config_manager
        self.main_window = MainWindow(controller=self)

    def pipeline_processamento(self, caminho_imagem):
        print(f"[PIPELINE] (simulado) Processando {caminho_imagem}")
