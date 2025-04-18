# src/modules/config_manager.py
# BLOCO FIX – Gerenciador central das configurações por evento

import os
import json

class ConfigManager:
    """
    Gerencia o carregamento e salvamento do JSON de configurações de um evento.
    """
    def __init__(self, caminho_config):
        self.caminho_config = caminho_config
        self.config = {}
        self._carregar()

    def _carregar(self):
        """Carrega o JSON se existir, senão cria estrutura padrão"""
        if os.path.exists(self.caminho_config):
            with open(self.caminho_config, "r") as f:
                self.config = json.load(f)
                print(f"[CONFIG] Configurações carregadas: {self.caminho_config}")
        else:
            print(f"[CONFIG] Arquivo não encontrado. Usando padrão.")
            self.config = {
                "modo_teste": True,
                "ia": {},
                "layout": {},
                "compartilhamento": {},
                "impressao": {},
                "smugmug": {}
            }
            self.salvar_config()

    def salvar_config(self):
        """Salva o JSON atualizado"""
        os.makedirs(os.path.dirname(self.caminho_config), exist_ok=True)
        with open(self.caminho_config, "w") as f:
            json.dump(self.config, f, indent=4)
            print(f"[CONFIG] Configuração salva: {self.caminho_config}")
