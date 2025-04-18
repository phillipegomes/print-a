# src/modules/backup_manager.py
# BLOCO 8.1 - Módulo de backup automático (salva imagens em pasta extra se ativado nas configs)

import os
import shutil

# 🧠 Explicação:
# Este módulo verifica se o backup está ativado no settings.json do evento.
# Se estiver, copia a imagem para a pasta especificada como "backup_pasta"

def salvar_em_backup(config_compartilhamento: dict, caminho_imagem: str):
    if not config_compartilhamento.get("backup_ativo"):
        return  # backup está desativado

    pasta_backup = config_compartilhamento.get("backup_pasta")
    if not pasta_backup or not os.path.isdir(pasta_backup):
        print(f"[BACKUP] Caminho de backup inválido: {pasta_backup}")
        return

    try:
        nome_arquivo = os.path.basename(caminho_imagem)
        destino = os.path.join(pasta_backup, nome_arquivo)
        shutil.copy2(caminho_imagem, destino)
        print(f"[BACKUP] Copiado para backup: {destino}")
    except Exception as e:
        print(f"[BACKUP] ERRO ao copiar {caminho_imagem}: {e}")
