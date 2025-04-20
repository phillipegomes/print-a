# src/modules/file_watcher.py
# Módulo de monitoramento de nova imagem

import os
import time
import threading

class FileWatcher:
    """
    Monitora uma pasta e chama um callback quando uma nova imagem é adicionada.

    Parâmetros:
        - pasta_fotos (str): Caminho da pasta monitorada
        - config (dict): Configurações do evento (pode conter modo_teste etc.)
        - callback (func): Função a ser chamada quando nova imagem for detectada
    """
    def __init__(self, pasta_fotos, config, callback=None):
        self.pasta_fotos = pasta_fotos
        self.config = config
        self.callback = callback
        self.monitorando = False
        self._arquivos_conhecidos = set(os.listdir(pasta_fotos)) if os.path.exists(pasta_fotos) else set()

    def iniciar(self):
        if not os.path.exists(self.pasta_fotos):
            print(f"[ERRO] Pasta de fotos não existe: {self.pasta_fotos}")
            return
        print(f"[MONITOR] Iniciando monitoramento da pasta: {self.pasta_fotos}")
        self.monitorando = True
        thread = threading.Thread(target=self._loop_monitoramento, daemon=True)
        thread.start()

    def parar(self):
        self.monitorando = False

    def _loop_monitoramento(self):
        print(f"[MONITOR] Observando {self.pasta_fotos}...")
        while self.monitorando:
            try:
                arquivos_atuais = set(os.listdir(self.pasta_fotos))
                novos = arquivos_atuais - self._arquivos_conhecidos
                for nome_arquivo in novos:
                    caminho = os.path.join(self.pasta_fotos, nome_arquivo)
                    if os.path.isfile(caminho) and nome_arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
                        print(f"[MONITOR] Nova imagem detectada: {nome_arquivo}")
                        if self.callback:
                            self.callback(caminho)
                self._arquivos_conhecidos = arquivos_atuais
                time.sleep(2)
            except Exception as e:
                print(f"[MONITOR] Erro no monitoramento: {e}")
