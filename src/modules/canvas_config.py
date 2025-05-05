import logging
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt6.QtCore import QRectF

def configurar_canvas(view: QGraphicsView, scene: QGraphicsScene, largura: int, altura: int):
    """
    Configura o canvas com proporção real e margens visuais.

    :param view: QGraphicsView onde a cena será exibida
    :param scene: QGraphicsScene onde os elementos serão adicionados
    :param largura: Largura do layout (ex: 1500)
    :param altura: Altura do layout (ex: 1000)
    """
    scene.clear()
    scene.setSceneRect(QRectF(0, 0, largura, altura))
    view.setScene(scene)
    view.setRenderHint(view.RenderHint.Antialiasing)

    logging.info(f"[🖼️ CANVAS] Configurado com {largura}x{altura}px")

    # Margens visuais (traço cinza claro)
    try:
        from PyQt6.QtGui import QPen, QColor
        from PyQt6.QtCore import Qt
        pen = QPen(QColor(180, 180, 180), 2, Qt.PenStyle.DashLine)

        # Margens em forma de borda tracejada
        margem = scene.addRect(0, 0, largura, altura, pen)
        margem.setZValue(1000)
    except Exception as e:
        logging.warning(f"[⚠️ MARGEM] Erro ao desenhar margem: {str(e)}")
