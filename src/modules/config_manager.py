# src/modules/config_manager.py
# SUPREMO – Gerenciador de Configurações por Evento

import os
import json

class ConfigManager:
    """
    Gerencia o carregamento e salvamento do settings.json de cada evento.
    Cria uma estrutura padrão se o arquivo não existir.
    """
    def __init__(self, caminho_config):
        self.caminho_config = caminho_config
        self.config = {}
        self._carregar()
        self._garantir_estrutura_padrao()  # ✅ SUPREMO FIX: garantir chaves mínimas

    def _carregar(self):
        """Carrega o JSON se existir, senão cria estrutura padrão"""
        if os.path.exists(self.caminho_config):
            try:
                with open(self.caminho_config, "r", encoding="utf-8") as f:
                    self.config = json.load(f)
                    print(f"[CONFIG] Configurações carregadas: {self.caminho_config}")
            except Exception as e:
                print(f"[CONFIG] Erro ao carregar config: {e}")
                self.config = {}
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

    def _garantir_estrutura_padrao(self):  # ✅ SUPREMO FIX
        padrao = {
            "modo_teste": True,
            "ia": {},
            "layout": {"arquivo": ""},
            "compartilhamento": {},
            "impressao": {"copias": 1},
            "smugmug": {}
        }
        for chave, valor in padrao.items():
            if chave not in self.config:
                self.config[chave] = valor


        """Salva o JSON atualizado"""
        try:
            os.makedirs(os.path.dirname(self.caminho_config), exist_ok=True)
            with open(self.caminho_config, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
                print(f"[CONFIG] Configuração salva: {self.caminho_config}")
        except Exception as e:
            print(f"[CONFIG] Erro ao salvar config: {e}")
