# src/ui/main_window.py
# BLOCO 3 - Tela principal com galeria visual, botões por imagem e layout refinado

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QGridLayout,
    QHBoxLayout, QMessageBox, QSpinBox
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from src.ui.main_actions import carregar_imagens, imprimir_foto, excluir_foto

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(f"PrintA - Evento: {self.controller.evento_atual}")
        self.setMinimumSize(1000, 700)

        self.pasta_fotos = os.path.join("eventos", self.controller.evento_atual, "Fotos")

        self.layout_principal = QVBoxLayout(self)
        self.label_evento = QLabel(f"Evento atual: {self.controller.evento_atual}")
        self.label_evento.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_evento.setStyleSheet("font-size: 18px; margin: 10px;")

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.grid = QGridLayout(self.scroll_widget)
        self.scroll.setWidget(self.scroll_widget)

        self.btn_voltar = QPushButton("Voltar para eventos")
        self.btn_voltar.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_voltar.clicked.connect(self.controller.abrir_event_window)

        self.layout_principal.addWidget(self.label_evento)
        self.layout_principal.addWidget(self.scroll)
        self.layout_principal.addWidget(self.btn_voltar, alignment=Qt.AlignmentFlag.AlignCenter)

        self.carregar_galeria()
        self.setStyleSheet("background-color: #f9f9f9;")

    def carregar_galeria(self):
        imagens = carregar_imagens(self.pasta_fotos)
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        for idx, caminho in enumerate(imagens):
            thumb = QPixmap(caminho).scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            img_label = QLabel()
            img_label.setPixmap(thumb)
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            btn_imprimir = QPushButton("Imprimir")
            btn_imprimir.clicked.connect(lambda _, c=caminho: imprimir_foto(c))

            btn_excluir = QPushButton("Excluir")
            btn_excluir.clicked.connect(lambda _, c=caminho: self.acao_excluir(c))

            spin = QSpinBox()
            spin.setMinimum(1)
            spin.setMaximum(10)
            spin.setValue(1)
            spin.setFixedWidth(60)
            btn_imprimir.clicked.connect(lambda _, c=caminho, s=spin: imprimir_foto(c, s.value()))

            botoes = QHBoxLayout()
            botoes.addWidget(btn_imprimir)
            botoes.addWidget(spin)
            botoes.addWidget(btn_excluir)

            caixa = QVBoxLayout()
            caixa.addWidget(img_label)
            caixa.addLayout(botoes)

            container = QWidget()
            container.setLayout(caixa)
            container.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 8px; background: #fff;")

            self.grid.addWidget(container, idx // 3, idx % 3)  # 3 colunas por linha

    def acao_excluir(self, caminho):
        confirm = QMessageBox.question(self, "Excluir", f"Deseja excluir a imagem?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            if excluir_foto(caminho):
                self.carregar_galeria()
