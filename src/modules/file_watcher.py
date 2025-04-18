# src/modules/file_watcher.py
# BLOCO 14 – Monitoramento da pasta /Fotos e execução automática do pipeline

import os
import time
import threading
from src.ui.main_actions import processar_imagem_completa

class FileWatcher:
    def __init__(self, pasta_fotos, config, callback=None):
        self.pasta_fotos = pasta_fotos
        self.config = config
        self.callback = callback  # função opcional para chamar após processar (ex: atualizar galeria)
        self._parar = False
        self._arquivos_processados = set()

    def iniciar(self):
        thread = threading.Thread(target=self._verificar_loop, daemon=True)
        thread.start()

    def parar(self):
        self._parar = True

    def _verificar_loop(self):
        print(f"[MONITOR] Iniciando monitoramento da pasta: {self.pasta_fotos}")
        while not self._parar:
            try:
                arquivos = [f for f in os.listdir(self.pasta_fotos)
                            if f.lower().endswith((".jpg", ".jpeg", ".png"))]

                for nome in arquivos:
                    caminho = os.path.join(self.pasta_fotos, nome)
                    if caminho not in self._arquivos_processados:
                        print(f"[MONITOR] Nova imagem detectada: {nome}")
                        final = processar_imagem_completa(caminho, self.config)
                        self._arquivos_processados.add(caminho)

                        if final and self.callback:
                            self.callback(final)  # exibir ou logar a imagem final

                time.sleep(2)

            except Exception as e:
                print(f"[MONITOR] Erro no monitoramento: {e}")
                time.sleep(5)
