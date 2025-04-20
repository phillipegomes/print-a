# src/ui/layout_preview.py
# ✅ BLOCO 6.2 – Aplicar layout na imagem

from PIL import Image

def aplicar_layout_em_imagem(imagem_path, layout_path, posicao="Centro", borda=False):
    """
    Aplica o layout na imagem original, centralizando conforme a posição e opção de borda.
    Retorna uma nova imagem com o layout aplicado.
    """
    try:
        imagem = Image.open(imagem_path).convert("RGBA")
        layout = Image.open(layout_path).convert("RGBA")

        largura, altura = layout.size
        nova_imagem = layout.copy()

        imagem = imagem.resize((int(largura * 0.65), int(altura * 0.65)))

        # Calcula posição
        if posicao == "Centro":
            x = (largura - imagem.width) // 2
            y = (altura - imagem.height) // 2
        elif posicao == "Superior":
            x = (largura - imagem.width) // 2
            y = int(altura * 0.1)
        elif posicao == "Inferior":
            x = (largura - imagem.width) // 2
            y = altura - imagem.height - int(altura * 0.1)
        else:
            x, y = 0, 0

        nova_imagem.paste(imagem, (x, y), imagem if imagem.mode == 'RGBA' else None)

        # Adiciona borda opcional
        if borda:
            from PIL import ImageOps
            nova_imagem = ImageOps.expand(nova_imagem, border=30, fill="white")

        return nova_imagem

    except Exception as e:
        print(f"[ERRO] ao aplicar layout: {e}")
        return None
