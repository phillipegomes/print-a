# src/modules/whatsapp_sender.py
# BLOCO 5 - Módulo para envio de imagens por WhatsApp (versão inicial com simulação)

import os

# 🧠 Explicação:
# Este módulo é um ponto central para envio de imagens por WhatsApp.
# Nesta fase inicial, ele apenas simula o envio com um print.
# Futuramente, aqui entrará integração real com API como Ultramsg, Chat-API, etc.
# Ele será chamado diretamente da galeria, ao lado do botão de impressão.

def enviar_por_whatsapp(numero, caminho_imagem):
    """
    Simula envio de imagem para um número de WhatsApp.
    - numero: string com telefone no formato internacional
    - caminho_imagem: caminho completo da imagem a ser enviada
    """
    if not os.path.exists(caminho_imagem):
        print(f"[WHATSAPP] ERRO: Arquivo não encontrado: {caminho_imagem}")
        return False

    print(f"[WHATSAPP] Enviando imagem para {numero}: {caminho_imagem}")
    # Aqui entraria a lógica real de envio via API

    return True
