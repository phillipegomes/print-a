# src/modules/image_processor.py
# BLOCO 10A - Estrutura de processamento de IA (modo simulado com imagem de teste)

from PIL import Image, ImageEnhance
import os

def aplicar_ia_em_imagem(caminho_entrada, caminho_saida, estilo="Cartoon"):
    """
    Simula aplicação de IA com base no estilo. Futuramente pode ser substituído por modelo real ou API.
    """
    try:
        img = Image.open(caminho_entrada).convert("RGB")

        if estilo == "Cartoon":
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.8)
        elif estilo == "Ghibli":
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(1.2)
        elif estilo == "Anime":
            img = img.transpose(Image.Transpose.CONTOUR)
        else:
            print(f"[IA] Estilo '{estilo}' não reconhecido. Nenhum efeito aplicado.")

        img.save(caminho_saida)
        print(f"[IA] Imagem processada com estilo '{estilo}' e salva em: {caminho_saida}")
        return True
    except Exception as e:
        print(f"[IA] ERRO ao aplicar IA: {e}")
        return False
