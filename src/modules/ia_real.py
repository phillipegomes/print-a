import requests
from PIL import Image, ImageEnhance
from io import BytesIO

# === EFEITOS DE IA LOCAL (Offline) ===

def aplicar_ia(imagem, estilo):
    """
    Aplica um efeito IA local diretamente em uma imagem PIL.

    Estilos suportados:
      - "cartoon"
      - "ghibli"
    """
    estilo = estilo.lower()
    if estilo == "cartoon":
        return _efeito_cartoon(imagem)
    elif estilo == "ghibli":
        return _efeito_ghibli(imagem)
    else:
        print(f"[IA] Estilo desconhecido: {estilo}. Retornando original.")
        return imagem

def _efeito_cartoon(imagem):
    """
    Aumenta a saturação da imagem para dar um visual cartoon.
    """
    enhancer = ImageEnhance.Color(imagem)
    return enhancer.enhance(2.0)

def _efeito_ghibli(imagem):
    """
    Clareia a imagem suavemente, inspirado nos visuais de filmes Ghibli.
    """
    enhancer = ImageEnhance.Brightness(imagem)
    return enhancer.enhance(1.2)

def aplicar_ia_em_imagem(caminho_entrada, caminho_saida, estilo):
    """
    Aplica IA local (offline) com base no estilo escolhido.

    Parâmetros:
      - caminho_entrada: caminho da imagem original
      - caminho_saida: onde salvar a imagem processada
      - estilo: "cartoon", "ghibli", etc.
    """
    try:
        imagem = Image.open(caminho_entrada).convert("RGB")
        imagem_processada = aplicar_ia(imagem, estilo)
        imagem_processada.save(caminho_saida)
        print(f"[IA OFFLINE] Imagem processada com estilo '{estilo}' e salva em {caminho_saida}")
    except Exception as e:
        print(f"[ERRO] ao aplicar IA offline: {e}")

# === IA ONLINE (API) ===

def processar_ia_via_api(caminho_entrada, caminho_saida, estilo, api_key):
    """
    Envia a imagem para uma API externa (DeepAI ou similar) e salva a imagem de saída.

    Parâmetros:
      - caminho_entrada: caminho da imagem original
      - caminho_saida: onde salvar a imagem transformada
      - estilo: nome do endpoint da API ("Anime", "Avatar", etc.)
      - api_key: chave da API fornecida pelo usuário
    """
    try:
        if not api_key:
            print("[IA/API] Chave de API ausente.")
            Image.open(caminho_entrada).save(caminho_saida)
            return

        url = "https://api.deepai.org/api/" + estilo.lower().replace(" ", "-")

        with open(caminho_entrada, "rb") as f:
            response = requests.post(
                url,
                files={'image': f},
                headers={'api-key': api_key}
            )

        if response.status_code == 200:
            output_url = response.json().get("output_url")
            if output_url:
                output = requests.get(output_url)
                Image.open(BytesIO(output.content)).save(caminho_saida)
                print(f"[IA/API] Imagem via API salva em {caminho_saida}")
                return
        print("[IA/API] Falha ao processar imagem via API.")
        Image.open(caminho_entrada).save(caminho_saida)

    except Exception as e:
        print(f"[IA/API] Erro: {e}")
        Image.open(caminho_entrada).save(caminho_saida)
