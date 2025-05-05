# ✅ src/modules/layout_templates.py

import logging

logger = logging.getLogger("editor")

def aplicar_template(canvas, config_manager):
    """
    Aplica um template de layout predefinido ao canvas.
    """
    template = obter_template_toten_3fotos()
    canvas.carregar_elementos(template)
    logger.info("Template 'Totem 3 Fotos' aplicado ao canvas.")

def obter_template_toten_3fotos():
    """
    Retorna um layout de totem com 3 fotos verticais, estilo clássico 10x15.
    """
    return [
        {
            "id": "photo_1",
            "tipo": "foto",
            "x": 150,
            "y": 100,
            "w": 450,
            "h": 300,
            "z_index": 1
        },
        {
            "id": "photo_2",
            "tipo": "foto",
            "x": 150,
            "y": 420,
            "w": 450,
            "h": 300,
            "z_index": 2
        },
        {
            "id": "photo_3",
            "tipo": "foto",
            "x": 150,
            "y": 740,
            "w": 450,
            "h": 300,
            "z_index": 3
        },
        {
            "id": "texto_evento",
            "tipo": "texto",
            "x": 650,
            "y": 1000,
            "w": 1000,
            "h": 100,
            "z_index": 4
        }
    ]
