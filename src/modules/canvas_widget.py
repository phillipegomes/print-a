
# ✅ src/modules/canvas_widget.py
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog
from PyQt6.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt6.QtCore import Qt
import logging

# 🔧 Logger
logging.basicConfig(filename='logs/editor.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('editor')

class CanvasWidget(QGraphicsView):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setRenderHints(QPainter.RenderHint.Antialiasing)
        self.setSceneRect(0, 0, 1800, 1200)  # 4x6 polegadas a 300 DPI
        self.elementos = []

    def adicionar_elemento(self, tipo):
        if tipo == "foto":
            caminho, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "", "Imagens (*.png *.jpg *.jpeg)")
            if caminho:
                pixmap = QPixmap(caminho).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                item = self.scene.addPixmap(pixmap)
                item.setPos(100, 100)
                item.setZValue(len(self.elementos))
                self.elementos.append({
                    "id": f"foto_{len(self.elementos)+1}",
                    "tipo": "foto",
                    "caminho": caminho,
                    "x": 100,
                    "y": 100,
                    "largura": 300,
                    "altura": 300
                })
                logger.info(f"Imagem real adicionada ao canvas: {caminho}")
        else:
            x, y, w, h = 100, 100, 300, 300
            retangulo = self.scene.addRect(x, y, w, h, QPen(QColor('blue'), 2), QColor(200, 200, 200, 100))
            retangulo.setZValue(len(self.elementos))
            self.elementos.append({
                "id": f"{tipo}_{len(self.elementos)+1}",
                "tipo": tipo,
                "x": x,
                "y": y,
                "largura": w,
                "altura": h
            })
            logger.info(f"Elemento {tipo} adicionado ao canvas.")

    def get_elementos(self):
        return self.elementos

    def carregar_elementos(self, elementos):
        self.scene.clear()
        self.elementos = []
        for el in elementos:
            if el["tipo"] == "foto" and el.get("caminho") and Path(el["caminho"]).exists():
                pixmap = QPixmap(el["caminho"]).scaled(el["largura"], el["altura"], Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                item = self.scene.addPixmap(pixmap)
            else:
                item = self.scene.addRect(el["x"], el["y"], el["largura"], el["altura"], QPen(QColor('blue'), 2), QColor(200, 200, 200, 100))
            item.setPos(el["x"], el["y"])
            item.setZValue(el.get("z_index", 0))
            self.elementos.append(el)
