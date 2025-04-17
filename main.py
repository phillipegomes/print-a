import traceback
from PyQt6.QtWidgets import QApplication
import sys

try:
    from src.controller.app_controller import AppController

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        controller = AppController()
        controller.start()
        sys.exit(app.exec())

except Exception as e:
    import os
    os.makedirs("logs", exist_ok=True)
    with open("logs/erro_atual.log", "w") as f:
        f.write("ERRO EXECUÇÃO PrintA:\n\n")
        f.write(traceback.format_exc())
    raise
