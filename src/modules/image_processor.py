import os
from PIL import Image, ImageDraw, ImageFont

def aplicar_ia_em_imagem(imagem_path, estilo="default"):
    """
    Simula a aplicação de um efeito IA na imagem. 
    Aqui o efeito é ilustrativo. Pode ser trocado por modelo real.
    """
    try:
        imagem = Image.open(imagem_path).convert("RGB")
        draw = ImageDraw.Draw(imagem)
        draw.text((10, 10), f"IA: {estilo}", fill="red")
        return imagem
    except Exception as e:
        print(f"[ERRO] Falha ao aplicar IA: {e}")
        return None

def aplicar_layout(imagem_path, layout_path):
    """
    Aplica um layout PNG (com transparência) sobre a imagem original.
    """
    try:
        imagem = Image.open(imagem_path).convert("RGBA")
        layout = Image.open(layout_path).convert("RGBA")

        # Redimensiona o layout para caber sobre a imagem base
        layout = layout.resize(imagem.size, Image.Resampling.LANCZOS)

        imagem_final = Image.alpha_composite(imagem, layout)
        return imagem_final.convert("RGB")
    except Exception as e:
        print(f"[ERRO] ao aplicar layout: {e}")
        return None
