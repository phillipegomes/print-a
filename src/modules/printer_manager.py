# src/modules/printer_manager.py
# BLOCO 13 – Impressão real da imagem final processada

import os
import platform
import subprocess

def imprimir(caminho_imagem, copias=1, nome_impressora=None):
    """
    Envia uma imagem para a impressora padrão ou especificada.
    Funciona no Windows, macOS e Linux com CUPS.
    """
    sistema = platform.system()

    if not os.path.exists(caminho_imagem):
        print(f"[IMPRESSÃO] Arquivo não encontrado: {caminho_imagem}")
        return False

    try:
        if sistema == "Windows":
            for _ in range(copias):
                os.startfile(caminho_imagem, "print")

        elif sistema == "Darwin" or sistema == "Linux":
            comando = ["lp"]
            if nome_impressora:
                comando += ["-d", nome_impressora]
            if copias > 1:
                comando += ["-n", str(copias)]
            comando.append(caminho_imagem)

            subprocess.run(comando, check=True)

        print(f"[IMPRESSÃO] Enviado para a impressora: {caminho_imagem} ({copias}x)")
        return True

    except Exception as e:
        print(f"[ERRO IMPRESSÃO] {e}")
        return False
