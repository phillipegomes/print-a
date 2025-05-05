# ✅ src/modules/layout_renderer.py
# Renderizador de Layout - Print A 3.6

import os
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from src.modules.config_manager import ConfigManager

# ❌ get_logger removido completamente

class LayoutRenderer:
    def __init__(self, config):
        self.config = config or {}
        self.tamanho = self.config.get("layout", {}).get("tamanho", "4x6")
        self.orientacao = self.config.get("layout", {}).get("orientacao", "Horizontal")
        self.dpi = int(self.config.get("layout", {}).get("dpi", 300))
        self.largura_px, self.altura_px = self._calcular_dimensoes()

    def _calcular_dimensoes(self):
        tamanhos_cm = {
            "4x6": (10, 15),
            "5x7": (13, 18),
            "6x8": (15, 20),
        }
        cm_larg, cm_alt = tamanhos_cm.get(self.tamanho, (10, 15))
        if self.orientacao == "Vertical":
            cm_larg, cm_alt = cm_alt, cm_larg
        px_larg = int(cm_larg * self.dpi / 2.54)
        px_alt = int(cm_alt * self.dpi / 2.54)
        return px_larg, px_alt

    def renderizar(self, elementos, nome_base="preview_temp"):
        imagem = Image.new("RGB", (self.largura_px, self.altura_px), (255, 255, 255))
        draw = ImageDraw.Draw(imagem)

        for el in elementos:
            tipo = el.get("tipo")
            x = int(el.get("x", 0) * self.largura_px)
            y = int(el.get("y", 0) * self.altura_px)
            w = int(el.get("largura", 0.3) * self.largura_px)
            h = int(el.get("altura", 0.3) * self.altura_px)

            if tipo == "foto" and el.get("caminho") and os.path.exists(el["caminho"]):
                try:
                    img = Image.open(el["caminho"]).resize((w, h))
                    imagem.paste(img, (x, y))
                except Exception as e:
                    pass  # logger removido

            elif tipo == "texto":
                texto = el.get("texto", "Texto")
                cor = el.get("cor", "#000000")
                tamanho = int(el.get("tamanho", 0.05) * self.largura_px)
                font_path = "/System/Library/Fonts/Supplemental/Arial.ttf" if os.name == "posix" else "arial.ttf"
                try:
                    font = ImageFont.truetype(font_path, tamanho)
                except:
                    font = ImageFont.load_default()
                draw.text((x, y), texto, fill=cor, font=font)

            elif tipo == "forma":
                cor = el.get("cor", "#000000")
                draw.rectangle([x, y, x + w, y + h], outline=cor, width=2)

        pasta_saida = os.path.join("eventos", self.config.get("nome_evento", "teste"), "fotos_prontas")
        os.makedirs(pasta_saida, exist_ok=True)

        nome_arquivo = f"{nome_base}_{datetime.now().strftime('%H%M%S')}.png"
        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        imagem.save(caminho_saida)
        return caminho_saida

def aplicar_layout_em_imagem(caminho_imagem, config):
    renderer = LayoutRenderer(config)
    elementos = config.get("layout", [])
    return renderer.renderizar(elementos, nome_base=os.path.splitext(os.path.basename(caminho_imagem))[0])
