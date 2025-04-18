# src/modules/printer_manager.py
# BLOCO 4 - Módulo de impressão: estrutura inicial para impressora real ou simulação

import os
import datetime

# 🧠 Explicação:
# Este módulo centraliza toda a lógica de impressão.
# Inicialmente ele simula a impressão (print no console), mas está pronto para receber
# comandos reais (ex: via subprocess para chamar drivers ou comandos de spool).
# Também registra um log em logs/execucao.log para rastreamento seguro.

def imprimir(caminho_arquivo, copias=1):
    """
    Simula ou envia imagem para impressão real.
    caminho_arquivo: caminho completo da imagem
    copias: número de cópias a imprimir
    """
    if not os.path.exists(caminho_arquivo):
        print(f"[ERRO] Arquivo não encontrado: {caminho_arquivo}")
        return False

    # Simula impressão
    print(f"[PRINTER] Imprimindo {copias}x: {caminho_arquivo}")

    # Grava log real em execucao.log
    try:
        os.makedirs("logs", exist_ok=True)
        with open("logs/execucao.log", "a") as log:
            log.write(f"[{datetime.datetime.now()}] IMPRESSAO: {copias}x {caminho_arquivo}\n")
    except Exception as e:
        print(f"[ERRO] ao gravar log de impressão: {e}")

    return True
