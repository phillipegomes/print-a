# src/ui/layout_saver.py
import json
import os
from datetime import datetime
import logging

logger = logging.getLogger("editor")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/editor.log")
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

DEFAULT_LAYOUT = {
    "elementos": []
}

class LayoutSaver:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.layout_path = os.path.join(
            os.path.dirname(config_manager.settings_path),
            "config", "layout_custom.json"
        )

    def salvar_layout(self, elementos: list):
        try:
            data = {
                "elementos": [
                    {"id": eid, "x": item.rect().x(), "y": item.rect().y()} for eid, item in elementos
                ]
            }
            with open(self.layout_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logger.info(f"Layout salvo com {len(elementos)} elemento(s)")
        except Exception as e:
            logger.error(f"Erro ao salvar layout: {e}")

    def carregar_layout(self):
        if not os.path.exists(self.layout_path):
            logger.warning("layout_custom.json não encontrado, carregando padrão")
            return DEFAULT_LAYOUT
        try:
            with open(self.layout_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            logger.info(f"Layout carregado com {len(data.get('elementos', []))} elemento(s)")
            return data
        except Exception as e:
            logger.error(f"Erro ao carregar layout: {e}")
            return DEFAULT_LAYOUT
