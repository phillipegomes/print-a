# src/ui/layout_templates.py
import os
import json
import logging

logger = logging.getLogger("editor")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logs/editor.log")
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

TEMPLATES = {
    "casamento": {
        "elementos": [
            {"id": "photo_1", "x": 100, "y": 100},
            {"id": "text_1", "x": 200, "y": 400}
        ]
    },
    "formatura": {
        "elementos": [
            {"id": "photo_1", "x": 150, "y": 100},
            {"id": "text_1", "x": 250, "y": 350},
            {"id": "logo_1", "x": 400, "y": 50}
        ]
    }
}

class LayoutTemplates:
    def __init__(self, canvas, saver):
        self.canvas = canvas
        self.saver = saver

    def aplicar_template(self, nome_template: str):
        if nome_template not in TEMPLATES:
            logger.warning(f"Template '{nome_template}' não encontrado.")
            return
        try:
            template = TEMPLATES[nome_template]
            self.canvas.limpar()
            for elemento in template["elementos"]:
                self.canvas.adicionar_elemento_desde_template(elemento)
            self.saver.salvar_layout([
                (e["id"], self.canvas.get_elemento_por_id(e["id"]))
                for e in template["elementos"]
            ])
            logger.info(f"Template '{nome_template}' aplicado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao aplicar template '{nome_template}': {e}")
