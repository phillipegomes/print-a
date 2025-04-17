import os

def carregar_imagens(pasta_fotos):
    if not os.path.exists(pasta_fotos):
        return []
    return sorted([
        os.path.join(pasta_fotos, f)
        for f in os.listdir(pasta_fotos)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ], key=os.path.getmtime)
