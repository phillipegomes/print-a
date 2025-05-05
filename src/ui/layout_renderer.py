import os
from PIL import Image, ImageDraw

class LayoutRenderer:
    def __init__(self, layout_config: dict, imagem_path: str):
        self.layout_config = layout_config
        self.imagem_path = imagem_path

    def aplicar_layout(self, output_path: str) -> str:
        """
        Aplica o layout sobre a imagem base e salva no caminho final.
        """
        if not os.path.exists(self.imagem_path):
            raise FileNotFoundError(f"Imagem não encontrada: {self.imagem_path}")

        base = Image.open(self.imagem_path).convert("RGBA")

        # Se houver moldura no layout
        moldura_path = self.layout_config.get("moldura")
        if moldura_path and os.path.exists(moldura_path):
            moldura = Image.open(moldura_path).convert("RGBA")
            moldura = moldura.resize(base.size)
            base = Image.alpha_composite(base, moldura)

        # Simula elementos (exemplo: placeholders, textos)
        draw = ImageDraw.Draw(base)
        elementos = self.layout_config.get("elementos", [])
        for elem in elementos:
            if elem["tipo"] == "placeholder":
                x = elem["x"]
                y = elem["y"]
                w = elem["width"]
                h = elem["height"]
                draw.rectangle((x, y, x + w, y + h), outline="red", width=2)
                draw.text((x + 5, y + 5), f"{elem['id']}", fill="red")

        # Salva imagem com layout aplicado
        output_path = os.path.abspath(output_path)
        base.convert("RGB").save(output_path, "JPEG")
        return output_path
