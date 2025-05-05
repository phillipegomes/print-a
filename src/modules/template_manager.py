# ✅ SUPREMO TEMPLATE MANAGER – Compatível com layout_editor.py
import os
import json


def save_layout(layout_data, path):
    """
    Salva os dados do layout em formato JSON no caminho especificado.
    layout_data: dicionário com estrutura do layout
    path: caminho absoluto para salvar (ex: layout_evento1.json)
    """
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(layout_data, f, indent=4, ensure_ascii=False)
        print(f"[✔] Layout salvo com sucesso em: {path}")
        return True
    except Exception as e:
        print(f"[ERRO] Não foi possível salvar o layout: {e}")
        return False


def load_layout(path):
    """
    Carrega o layout salvo anteriormente.
    Retorna um dicionário ou None se erro.
    """
    try:
        if not os.path.exists(path):
            print(f"[⚠] Layout não encontrado em: {path}")
            return None
        with open(path, 'r', encoding='utf-8') as f:
            layout = json.load(f)
        print(f"[✔] Layout carregado com sucesso de: {path}")
        return layout
    except Exception as e:
        print(f"[ERRO] Falha ao carregar layout: {e}")
        return None
