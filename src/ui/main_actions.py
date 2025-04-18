# src/ui/main_actions.py
# BLOCO 12 – Pipeline completo: IA → Layout → Salvar imagem final

import os
from PIL import Image
from PyQt6.QtWidgets import QMessageBox
from src.modules.image_processor import aplicar_ia_em_imagem
from src.modules.ia_real import processar_ia_via_api
from src.ui.layout_preview import aplicar_layout_em_imagem

EXTENSOES_VALIDAS = (".jpg", ".jpeg", ".png")

def carregar_imagens(pasta_fotos):
    if not os.path.exists(pasta_fotos):
        return []
    return sorted([
        os.path.join(pasta_fotos, f)
        for f in os.listdir(pasta_fotos)
        if f.lower().endswith(EXTENSOES_VALIDAS)
    ], key=os.path.getmtime)

def imprimir_foto(caminho, copias=1):
    print(f"[IMPRIMIR] {copias}x - {caminho}")
    # Integração com printer_manager aqui futuramente

def excluir_foto(caminho):
    try:
        os.remove(caminho)
        print(f"[EXCLUIR] {caminho}")
        return True
    except Exception as e:
        print(f"[ERRO] ao excluir {caminho}: {e}")
        QMessageBox.warning(None, "Erro", f"Erro ao excluir a imagem:\n{e}")
        return False

def enviar_whatsapp(numero, caminho_imagem):
    print(f"[WHATSAPP] Enviando {caminho_imagem} para {numero}")
    # Aqui entraria a lógica real de envio

def processar_imagem_completa(caminho_entrada, config):
    """
    Pipeline real: aplica IA (se ativado), aplica layout (se ativado), salva final.
    """
    try:
        nome_arquivo = os.path.basename(caminho_entrada)
        saida_temp = caminho_entrada

        # === IA ===
        if config.get("ia", {}).get("ativa"):
            estilo = config["ia"].get("estilo", "Cartoon")
            api_key = config["ia"].get("api_key", "")
            modo = config["ia"].get("modo", 0)
            saida_temp = caminho_entrada.replace(".jpg", f"_ia.jpg")

            if modo == 0:
                aplicar_ia_em_imagem(caminho_entrada, saida_temp, estilo)
            else:
                processar_ia_via_api(caminho_entrada, saida_temp, estilo, api_key)

        # === Layout ===
        if config.get("layout"):
            modelo = config["layout"].get("modelo", 0)
            posicao = config["layout"].get("posicao", 0)
            borda = config["layout"].get("borda", False)
            layout_file = f"assets/layouts/layout{modelo+1}.png"

            if os.path.exists(layout_file):
                imagem_com_layout = aplicar_layout_em_imagem(saida_temp, layout_file, ["Centro", "Superior", "Inferior"][posicao], borda)
                if imagem_com_layout:
                    saida_temp = caminho_entrada.replace(".jpg", f"_final.jpg")
                    imagem_com_layout.save(saida_temp)

        # === Salvar final em /Impressas ===
        pasta_final = os.path.join(os.path.dirname(os.path.dirname(caminho_entrada)), "Impressas")
        os.makedirs(pasta_final, exist_ok=True)
        destino_final = os.path.join(pasta_final, nome_arquivo)

        Image.open(saida_temp).save(destino_final)
        print(f"[FINALIZADO] Imagem salva: {destino_final}")
        return destino_final

    except Exception as e:
        print(f"[ERRO] no pipeline: {e}")
        return None
