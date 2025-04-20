import os
import shutil
import json
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox, QInputDialog

def carregar_eventos(parent=None):
    eventos = []
    eventos_path = "eventos"
    if not os.path.exists(eventos_path):
        os.makedirs(eventos_path)

    for nome in sorted(os.listdir(eventos_path), key=lambda n: os.path.getmtime(os.path.join(eventos_path, n)), reverse=True):
        caminho = os.path.join(eventos_path, nome)
        if not os.path.isdir(caminho):
            continue

        config_path = os.path.join(caminho, "config", "settings.json")
        data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho)).strftime("%d/%m/%Y %H:%M")

        eventos.append({
            "nome": nome,
            "caminho": caminho,
            "config": config_path,
            "data": data_modificacao
        })

    return eventos

def criar_evento(callback, nome_evento=None):
    """
    Cria um novo evento. Se nome_evento for passado, usa diretamente.
    Caso contrário, abre diálogo para o usuário.
    """
    if nome_evento:
        nome = nome_evento
        ok = True
    else:
        nome, ok = QInputDialog.getText(None, "Novo Evento", "Digite o nome do evento:")

    if ok and nome:
        caminho = os.path.join("eventos", nome)
        if not os.path.exists(caminho):
            os.makedirs(os.path.join(caminho, "Fotos"))
            os.makedirs(os.path.join(caminho, "config"))
            settings_path = os.path.join(caminho, "config", "settings.json")
            with open(settings_path, "w") as f:
                json.dump({}, f)
            print(f"[CRIADO] Evento: {nome}")
        else:
            if not nome_evento:  # Só alerta se foi manual
                QMessageBox.warning(None, "Aviso", f"Já existe um evento com o nome '{nome}'.")
        callback()

def abrir_evento(nome_evento, controller):
    caminho_config = os.path.join("eventos", nome_evento, "config", "settings.json")
    print(f"[CONFIG] Configurações carregadas: {caminho_config}")
    controller.abrir_main_window(caminho_config)

def duplicar_evento(nome_evento, callback):
    base_path = os.path.join("eventos", nome_evento)
    novo_nome = f"{nome_evento}_copia"
    novo_path = os.path.join("eventos", novo_nome)
    count = 1
    while os.path.exists(novo_path):
        novo_path = os.path.join("eventos", f"{novo_nome}_{count}")
        count += 1
    try:
        shutil.copytree(base_path, novo_path)
        print(f"[DUPLICADO] {base_path} ➜ {novo_path}")
        callback()
    except Exception as e:
        print(f"[ERRO] ao duplicar: {e}")
        QMessageBox.warning(None, "Erro", f"Erro ao duplicar o evento:\n{e}")

def excluir_evento(nome_evento):
    caminho = os.path.join("eventos", nome_evento)
    try:
        if os.path.isdir(caminho):
            shutil.rmtree(caminho)
        else:
            os.remove(caminho)
        print(f"[EXCLUÍDO] {caminho}")
    except Exception as e:
        print(f"[ERRO] ao excluir evento '{nome_evento}': {e}")

def renomear_evento(nome_evento, callback):
    novo_nome, ok = QInputDialog.getText(None, "Renomear Evento", "Digite o novo nome:", text=nome_evento)
    if ok and novo_nome and novo_nome != nome_evento:
        origem = os.path.join("eventos", nome_evento)
        destino = os.path.join("eventos", novo_nome)
        if os.path.exists(destino):
            QMessageBox.warning(None, "Erro", "Já existe um evento com esse nome.")
        else:
            try:
                os.rename(origem, destino)
                print(f"[RENOMEADO] {origem} ➜ {destino}")
                callback()
            except Exception as e:
                print(f"[ERRO] ao renomear: {e}")
                QMessageBox.warning(None, "Erro", f"Erro ao renomear:\n{e}")
