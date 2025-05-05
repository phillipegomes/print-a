from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt

class LayerPanel(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setLayout(self._criar_layout())

    def _criar_layout(self):
        layout = QVBoxLayout()

        # Lista de camadas
        self.lista_camadas = QListWidget()
        layout.addWidget(self.lista_camadas)

        # Botões de ordem
        botoes_ordem = QHBoxLayout()
        self.btn_subir = QPushButton("⬆️ Subir")
        self.btn_descer = QPushButton("⬇️ Descer")
        self.btn_subir.clicked.connect(self.subir_item)
        self.btn_descer.clicked.connect(self.descer_item)
        botoes_ordem.addWidget(self.btn_subir)
        botoes_ordem.addWidget(self.btn_descer)
        layout.addLayout(botoes_ordem)

        # Botão visibilidade
        self.btn_visibilidade = QPushButton("👁️ Alternar Visibilidade")
        self.btn_visibilidade.clicked.connect(self.alternar_visibilidade)
        layout.addWidget(self.btn_visibilidade)

        # Botão bloqueio
        self.btn_bloquear = QPushButton("🔒 Bloquear / Desbloquear")
        self.btn_bloquear.clicked.connect(self.bloquear_item)
        layout.addWidget(self.btn_bloquear)

        return layout

    def atualizar_lista(self, elementos):
        self.lista_camadas.clear()
        for elemento in elementos:
            item = QListWidgetItem(elemento.nome)
            item.setData(Qt.ItemDataRole.UserRole, elemento)
            self.lista_camadas.addItem(item)

    def item_selecionado(self):
        item = self.lista_camadas.currentItem()
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def subir_item(self):
        index = self.lista_camadas.currentRow()
        if index > 0:
            self.controller.canvas.trocar_ordem(index, index - 1)

    def descer_item(self):
        index = self.lista_camadas.currentRow()
        if index < self.lista_camadas.count() - 1:
            self.controller.canvas.trocar_ordem(index, index + 1)

    def alternar_visibilidade(self):
        elemento = self.item_selecionado()
        if elemento:
            elemento.visivel = not getattr(elemento, 'visivel', True)
            self.controller.canvas.update()

    def bloquear_item(self):
        elemento = self.item_selecionado()
        if elemento:
            elemento.bloqueado = not getattr(elemento, 'bloqueado', False)
            self.controller.canvas.update()
