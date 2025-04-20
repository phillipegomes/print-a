# src/modules/config_loader.py

import json
import os

def carregar_config_evento(caminho_arquivo):
    if not os.path.isfile(caminho_arquivo):
        print(f"[AVISO] Configuração não encontrada em {caminho_arquivo}")
        return {}
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERRO] Falha ao carregar config: {e}")
        return {}
