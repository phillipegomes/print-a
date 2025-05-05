# ✅ src/main.py – Entrada principal do Print A Supremo

import os
import sys
from PyQt6.QtWidgets import QApplication
from src.controller.app_controller import AppController

def garantir_pastas_essenciais():
    caminhos = [
        "assets/templates",
        "assets/molduras"
    ]
    for caminho in caminhos:
        os.makedirs(caminho, exist_ok=True)
        print(f"[INIT] Pasta garantida: {caminho}")

if __name__ == "__main__":
    garantir_pastas_essenciais()

    app = QApplication(sys.argv)
    controller = AppController()

    # ✅ SUPREMO FIX: método obrigatório para iniciar o fluxo
    if hasattr(controller, "iniciar"):
        controller.iniciar()
    else:
        print("❌ ERRO: AppController está sem o método iniciar().")
        sys.exit(1)

    sys.exit(app.exec())
