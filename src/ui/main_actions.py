import os
from PIL import Image
from PyQt6.QtWidgets import QMessageBox

# Módulos reais do projeto
from src.modules.image_processor import aplicar_ia_em_imagem
from src.modules.ia_real import processar_ia_via_api
from src.ui.layout_preview import aplicar_layout_em_imagem

EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png")


def carregar_imagens(pasta_fotos):
    """
    Carrega e ordena as imagens da pasta por data de modificação.
    """
    if not os.path.exists(pasta_fotos):
        print(f"[ERRO] Pasta de fotos não existe: {pasta_fotos}")
        return []

    arquivos = os.listdir(pasta_fotos)
    imagens = [
        os.path.join(pasta_fotos, f)
        for f in arquivos
        if f.lower().endswith(EXTENSOES_VALIDAS)
    ]

    imagens_ordenadas = sorted(imagens, key=os.path.getmtime)
    print(f"[GALERIA] Pasta: {pasta_fotos}")
    print(f"[GALERIA] Encontradas {len(imagens_ordenadas)} imagem(ns):")
    for img in imagens_ordenadas:
        print(f" - {img}")

    return imagens_ordenadas


def imprimir_foto(pasta_fotos, config, copias=1, caminho_direto=None):
    """
    Imprime uma imagem específica (se fornecida) ou a primeira da pasta.
    """
    if caminho_direto and os.path.isfile(caminho_direto):
        imagem = caminho_direto
    else:
        imagens = carregar_imagens(pasta_fotos)
        if not imagens:
            print("[IMPRIMIR] Nenhuma imagem para imprimir.")
            return
        imagem = imagens[0]

    print(f"[IMPRIMIR] {copias}x - {imagem}")
    # Integração com printer_manager real virá depois


def excluir_foto(caminho):
    """
    Exclui uma imagem do sistema.
    """
    try:
        if os.path.isfile(caminho):
            os.remove(caminho)
            print(f"[EXCLUÍDO] {caminho}")
            return True
        else:
            print(f"[ERRO] Arquivo não encontrado: {caminho}")
            return False
    except Exception as e:
        print(f"[ERRO] ao excluir {caminho}: {e}")
        QMessageBox.warning(None, "Erro", f"Erro ao excluir a imagem:\n{e}")
        return False


def enviar_whatsapp(numero, caminho_imagem):
    """
    Envia a imagem para um número via WhatsApp (placeholder).
    """
    print(f"[WHATSAPP] Enviando {caminho_imagem} para {numero}")
    # Envio real será implementado depois


def processar_imagem_completa(caminho_entrada, config):
    """
    Aplica IA (se ativada), aplica layout (se ativado) e salva no destino final.
    """
    try:
        nome_arquivo = os.path.basename(caminho_entrada)
        saida_temp = caminho_entrada

        # 🔹 IA
        if config.get("ia", {}).get("ativa"):
            estilo = config["ia"].get("estilo", "Cartoon")
            api_key = config["ia"].get("api_key", "")
            modo = config["ia"].get("modo", 0)
            saida_temp = caminho_entrada.replace(".jpg", f"_ia.jpg")

            if modo == 0:
                aplicar_ia_em_imagem(caminho_entrada, saida_temp, estilo)
            else:
                processar_ia_via_api(caminho_entrada, saida_temp, estilo, api_key)

        # 🔹 Layout
        if config.get("layout"):
            modelo = config["layout"].get("modelo", 0)
            posicao = config["layout"].get("posicao", 0)
            borda = config["layout"].get("borda", False)
            layout_file = f"assets/layouts/layout{modelo+1}.png"

            if os.path.exists(layout_file):
                imagem_com_layout = aplicar_layout_em_imagem(
                    saida_temp, layout_file,
                    ["Centro", "Superior", "Inferior"][posicao],
                    borda
                )
                if imagem_com_layout:
                    saida_temp = caminho_entrada.replace(".jpg", f"_final.jpg")
                    imagem_com_layout.save(saida_temp)

        # 🔹 Salvar em /Impressas
        pasta_final = os.path.join(os.path.dirname(os.path.dirname(caminho_entrada)), "Impressas")
        os.makedirs(pasta_final, exist_ok=True)
        destino_final = os.path.join(pasta_final, nome_arquivo)

        Image.open(saida_temp).save(destino_final)
        print(f"[FINALIZADO] Imagem salva: {destino_final}")
        return destino_final

    except Exception as e:
        print(f"[ERRO] no pipeline: {e}")
        return None
