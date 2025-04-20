# diagnostico/diagnostico_renderizacao_imagem.py
import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

PASTA = "eventos/Chatgpt/Fotos"  # Ajuste para o evento que está testando

def testar_imagens():
    print(f"🔍 Verificando imagens em: {PASTA}")
    if not os.path.exists(PASTA):
        print("❌ Pasta não existe.")
        return

    imagens = [f for f in os.listdir(PASTA) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not imagens:
        print("❌ Nenhuma imagem encontrada.")
        return

    app = QApplication(sys.argv)
    janela = QWidget()
    layout = QVBoxLayout()
    janela.setLayout(layout)

    for img_nome in imagens:
        caminho = os.path.join(PASTA, img_nome)
        pixmap = QPixmap(caminho)
        if pixmap.isNull():
            print(f"❌ Falha ao carregar: {caminho}")
        else:
            print(f"✅ Sucesso: {caminho}")
            label = QLabel(f"Imagem: {img_nome}")
            label.setPixmap(pixmap.scaled(100, 100))
            layout.addWidget(label)

    janela.setWindowTitle("Diagnóstico de Imagens")
    janela.show()
    app.exec()

if __name__ == "__main__":
    testar_imagens()
