# ✅ src/modules/layout_saver.py

import os
import json
import logging
from datetime import datetime

# Logger Supremo
logger = logging.getLogger("editor")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/editor.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
if not logger.hasHandlers():
    logger.addHandler(handler)

class LayoutSaver:
    """
    Responsável por salvar e carregar layouts do editor em JSON.
    """
    def __init__(self, controller):
        self.controller = controller
        self.config_manager = controller.config_manager
        self.evento_path = os.path.dirname(self.config_manager.caminho_config)
        self.caminho_json = os.path.join(self.evento_path, "config", "layout_custom.json")

    def salvar(self, elementos):
        """
        Salva os elementos do canvas em um JSON no caminho do evento atual.
        """
        dados = []
        for el in elementos:
            dados.append({
                "id": el.get("id", ""),
                "tipo": el.get("tipo", ""),
                "x": el.get("x", 0),
                "y": el.get("y", 0),
                "w": el.get("w", 0),
                "h": el.get("h", 0),
                "z_index": el.get("z_index", 0)
            })

        try:
            os.makedirs(os.path.dirname(self.caminho_json), exist_ok=True)
            with open(self.caminho_json, "w", encoding="utf-8") as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            logger.info(f"Layout salvo com {len(dados)} elemento(s).")
        except Exception as e:
            logger.error(f"Erro ao salvar layout: {e}")

    def carregar(self):
        """
        Carrega elementos do layout JSON. Retorna lista de dicionários.
        """
        if not os.path.exists(self.caminho_json):
            logger.warning("Arquivo de layout não encontrado. Retornando vazio.")
            return []

        try:
            with open(self.caminho_json, "r", encoding="utf-8") as f:
                dados = json.load(f)
            logger.info(f"Layout carregado com {len(dados)} elemento(s).")
            return dados
        except Exception as e:
            logger.error(f"Erro ao carregar layout: {e}")
            return []
