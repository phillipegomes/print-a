import os
import json
import shutil
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox, QInputDialog

# ✅ SUPREMO BLOCK: Criar Evento
def criar_evento(callback, nome_evento=None):
    """
    Cria um novo evento com estrutura obrigatória e gravação de settings.json com 'nome_evento'.
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
            data = {
                "nome_evento": nome,
                "criado_em": datetime.now().isoformat()
            }

            with open(settings_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            print(f"[CRIADO] Evento: {nome}")
        else:
            if not nome_evento:
                QMessageBox.warning(None, "Aviso", f"Já existe um evento com o nome '{nome}'.")

        if callback:
            callback()


# ✅ SUPREMO BLOCK: Abrir Evento
def abrir_evento(nome_evento, controller):
    """
    Abre um evento existente chamando o método supremo do controller.
    """
    path = f"eventos/{nome_evento}/config/settings.json"
    controller.abrir_main_window(path)
    print(f"[ABERTO] Evento: {nome_evento}")


# ✅ SUPREMO BLOCK: Duplicar Evento
def duplicar_evento(nome, callback):
    """
    Cria uma cópia do evento selecionado com sufixo _copia
    """
    origem = os.path.join("eventos", nome)
    destino = os.path.join("eventos", f"{nome}_copia")
    if os.path.exists(destino):
        QMessageBox.warning(None, "Erro", "Já existe uma cópia deste evento.")
        return
    try:
        shutil.copytree(origem, destino)
        print(f"[DUPLICADO] {nome} -> {nome}_copia")
        callback()
    except Exception as e:
        print(f"[ERRO] ao duplicar evento: {e}")


# ✅ SUPREMO BLOCK: Excluir Evento
def excluir_evento(nome):
    """
    Exclui evento e envia para backup automático em eventos_backup/
    """
    caminho = os.path.join("eventos", nome)
    if os.path.exists(caminho):
        destino_backup = os.path.join("eventos_backup", f"{nome}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
        shutil.move(caminho, destino_backup)
        print(f"[EXCLUÍDO] {caminho} -> {destino_backup}")


# ✅ SUPREMO BLOCK: Renomear Evento
def renomear_evento(nome_antigo, callback):
    """
    Renomeia evento mantendo estrutura e atualizando o nome_evento no settings.json
    """
    nome_novo, ok = QInputDialog.getText(None, "Renomear Evento", "Novo nome:")
    if ok and nome_novo:
        origem = os.path.join("eventos", nome_antigo)
        destino = os.path.join("eventos", nome_novo)
        if os.path.exists(destino):
            QMessageBox.warning(None, "Erro", "Já existe um evento com este nome.")
            return
        shutil.move(origem, destino)

        # Atualiza o nome_evento no settings.json
        settings_path = os.path.join(destino, "config", "settings.json")
        if os.path.exists(settings_path):
            try:
                with open(settings_path, "r+", encoding="utf-8") as f:
                    data = json.load(f)
                    data["nome_evento"] = nome_novo
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
            except Exception as e:
                print(f"[ERRO] ao atualizar nome no settings: {e}")

        print(f"[RENOMEADO] {nome_antigo} -> {nome_novo}")
        callback()
