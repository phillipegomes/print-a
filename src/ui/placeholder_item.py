from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsSimpleTextItem
from PyQt6.QtGui import QPen, QColor, QBrush
from PyQt6.QtCore import Qt


class PlaceholderItem(QGraphicsRectItem):
    def __init__(self, label, x, y, w, h):
        super().__init__(x, y, w, h)
        self.label = label
        self.setFlags(
            QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable |
            QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable
        )

        self.setBrush(QBrush(QColor(200, 200, 200, 100)))  # Cor cinza claro com transparência
        self.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.DashLine))

        # Texto centralizado
        self.texto = QGraphicsSimpleTextItem(label, self)
        self.texto.setBrush(QColor(0, 0, 0))
        self.atualizar_posicao_texto()

    def atualizar_posicao_texto(self):
        rect = self.rect()
        largura_texto = self.texto.boundingRect().width()
        altura_texto = self.texto.boundingRect().height()
        self.texto.setPos(
            rect.x() + (rect.width() - largura_texto) / 2,
            rect.y() + (rect.height() - altura_texto) / 2
        )

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        self.atualizar_posicao_texto()

    def setRect(self, *args):
        super().setRect(*args)
        self.atualizar_posicao_texto()

    def to_dict(self):
        r = self.rect()
        return {
            "label": self.label,
            "x": int(r.x()),
            "y": int(r.y()),
            "width": int(r.width()),
            "height": int(r.height())
        }
