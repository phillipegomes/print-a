# src/ui/main_window.py
# BLOCO 4B - Galeria com contador de impressão e limite por imagem

import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QGridLayout,
    QHBoxLayout, QMessageBox, QSpinBox
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from src.ui.main_actions import carregar_imagens, imprimir_foto, excluir_foto
from src.modules.print_counter import PrintCounter

class MainWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle(f"PrintA - Evento: {self.controller.evento_atual}")
        self.setMinimumSize(1000, 700)

        self.pasta_fotos = os.path.join("eventos", self.controller.evento_atual, "Fotos")
        self.print_counter = PrintCounter(self.controller.evento_atual)
        self.limite_copias = 3  # Limite fixo por imagem (poderá ser carregado de config futuramente)

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
            nome = os.path.basename(caminho)
            contagem = self.print_counter.get_contagem(caminho)

            img_label = QLabel()
            img_label.setPixmap(thumb)
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

            contador_label = QLabel(f"Impresso: {contagem}/{self.limite_copias}")
            contador_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            contador_label.setStyleSheet("font-size: 12px; color: #666;")

            spin = QSpinBox()
            spin.setMinimum(1)
            spin.setMaximum(self.limite_copias)
            spin.setValue(1)
            spin.setFixedWidth(60)

            btn_imprimir = QPushButton("Imprimir")
            btn_imprimir.clicked.connect(lambda _, c=caminho, s=spin, l=contador_label: self.acao_imprimir(c, s.value(), l))

            btn_excluir = QPushButton("Excluir")
            btn_excluir.clicked.connect(lambda _, c=caminho: self.acao_excluir(c))

            botoes = QHBoxLayout()
            botoes.addWidget(btn_imprimir)
            botoes.addWidget(spin)
            botoes.addWidget(btn_excluir)

            caixa = QVBoxLayout()
            caixa.addWidget(img_label)
            caixa.addWidget(contador_label)
            caixa.addLayout(botoes)

            container = QWidget()
            container.setLayout(caixa)
            container.setStyleSheet("padding: 8px; border: 1px solid #ddd; border-radius: 8px; background: #fff;")

            self.grid.addWidget(container, idx // 3, idx % 3)

    def acao_imprimir(self, caminho, copias, contador_label):
        if not self.print_counter.pode_imprimir(caminho, self.limite_copias):
            QMessageBox.warning(self, "Limite atingido", f"Essa imagem já foi impressa {self.limite_copias}x.")
            return
        imprimir_foto(caminho, copias)
        self.print_counter.registrar_impressao(caminho)
        novo_valor = self.print_counter.get_contagem(caminho)
        contador_label.setText(f"Impresso: {novo_valor}/{self.limite_copias}")

    def acao_excluir(self, caminho):
        confirm = QMessageBox.question(self, "Excluir", f"Deseja excluir a imagem?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if confirm == QMessageBox.StandardButton.Yes:
            if excluir_foto(caminho):
                self.carregar_galeria()
