from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QMenu, QMessageBox
)
from PyQt6.QtCore import Qt
from src.ui.styles.event_styles import EVENT_STYLE, TABELA_STYLE
from src.ui.event_actions import (
    carregar_eventos, criar_evento, abrir_evento,
    duplicar_evento, excluir_evento, renomear_evento
)

import os

class EventWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Print A – Meus Eventos")
        self.setStyleSheet(EVENT_STYLE)
        self.setMinimumSize(1000, 650)
        self.ordem_crescente = {0: True, 1: True}  # nome, data

        layout = QVBoxLayout()
        self.setLayout(layout)

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Buscar evento por nome...")
        self.search_input.setFixedHeight(36)
        self.search_input.textChanged.connect(self.filtrar_eventos)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(2)
        self.tabela.setHorizontalHeaderLabels(["Nome do Evento", "Data do Evento"])
        self.tabela.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.tabela.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.tabela.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tabela.setSelectionMode(QTableWidget.SelectionMode.ExtendedSelection)
        self.tabela.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.tabela.customContextMenuRequested.connect(self.abrir_menu_contexto)
        self.tabela.cellDoubleClicked.connect(self.abrir_evento_clicado)
        self.tabela.horizontalHeader().sectionClicked.connect(self.ordenar_por_coluna)
        self.tabela.setStyleSheet(TABELA_STYLE)
        layout.addWidget(self.tabela)

        botoes_layout = QHBoxLayout()
        self.btn_abrir = QPushButton("📂 Abrir")
        self.btn_renomear = QPushButton("✏️ Renomear")
        self.btn_criar = QPushButton("➕ Criar")
        self.btn_duplicar = QPushButton("📑 Duplicar")
        self.btn_excluir = QPushButton("🗑️ Excluir")

        self.btn_abrir.clicked.connect(self.abrir_evento_selecionado)
        self.btn_renomear.clicked.connect(self.renomear_evento_selecionado)
        self.btn_criar.clicked.connect(lambda: criar_evento(self.carregar_eventos))
        self.btn_duplicar.clicked.connect(self.duplicar_evento_selecionado)
        self.btn_excluir.clicked.connect(self.excluir_evento_selecionado)

        for btn in [self.btn_abrir, self.btn_renomear, self.btn_criar, self.btn_duplicar, self.btn_excluir]:
            btn.setFixedHeight(40)
            botoes_layout.addWidget(btn)

        layout.addLayout(botoes_layout)
        self.carregar_eventos()

    def carregar_eventos(self):
        self.todos_eventos = carregar_eventos(self)
        self.exibir_eventos(self.todos_eventos)

    def exibir_eventos(self, eventos):
        self.tabela.setRowCount(len(eventos))
        for row, evento in enumerate(eventos):
            self.tabela.setItem(row, 0, QTableWidgetItem(evento["nome"]))
            self.tabela.setItem(row, 1, QTableWidgetItem(evento["data"]))

    def filtrar_eventos(self, texto):
        filtrados = [e for e in self.todos_eventos if texto.lower() in e["nome"].lower()]
        self.exibir_eventos(filtrados)

    def ordenar_por_coluna(self, coluna):
        chave = "nome" if coluna == 0 else "data"
        self.ordem_crescente[coluna] = not self.ordem_crescente[coluna]
        reverso = not self.ordem_crescente[coluna]
        eventos_ordenados = sorted(self.todos_eventos, key=lambda e: e[k] if (k := chave) else "", reverse=reverso)
        self.exibir_eventos(eventos_ordenados)

    def get_eventos_selecionados(self):
        linhas = self.tabela.selectionModel().selectedRows()
        return [self.tabela.item(row.row(), 0).text() for row in linhas]

    def abrir_evento_selecionado(self):
        nomes = self.get_eventos_selecionados()
        if nomes:
            abrir_evento(nomes[0], self.controller)

    def renomear_evento_selecionado(self):
        nomes = self.get_eventos_selecionados()
        if nomes:
            renomear_evento(nomes[0], self.carregar_eventos)

    def duplicar_evento_selecionado(self):
        nomes = self.get_eventos_selecionados()
        if nomes:
            duplicar_evento(nomes[0], self.carregar_eventos)

    def excluir_evento_selecionado(self):
        nomes = self.get_eventos_selecionados()
        if not nomes:
            return

        if len(nomes) == 1:
            mensagem = f"Tem certeza que deseja excluir o evento '{nomes[0]}'?"
        else:
            mensagem = f"Tem certeza que deseja excluir os {len(nomes)} eventos selecionados?"

        box = QMessageBox(self)
        box.setIcon(QMessageBox.Icon.Warning)
        box.setWindowTitle("Confirmação")
        box.setText(mensagem)
        btn_sim = box.addButton("Sim", QMessageBox.ButtonRole.YesRole)
        btn_nao = box.addButton("Não", QMessageBox.ButtonRole.NoRole)
        box.exec()

        if box.clickedButton() == btn_sim:
            for nome in nomes:
                caminho = os.path.join("eventos", nome)
                if os.path.exists(caminho):
                    excluir_evento(nome)
            self.carregar_eventos()

    def abrir_evento_clicado(self, row, _):
        nome = self.tabela.item(row, 0).text()
        abrir_evento(nome, self.controller)

    def abrir_menu_contexto(self, pos):
        index = self.tabela.indexAt(pos)
        if index.isValid():
            nome = self.tabela.item(index.row(), 0).text()
            menu = QMenu()
            menu.addAction("Abrir", lambda: abrir_evento(nome, self.controller))
            menu.addAction("Renomear", lambda: renomear_evento(nome, self.carregar_eventos))
            menu.addAction("Duplicar", lambda: duplicar_evento(nome, self.carregar_eventos))
            menu.addAction("Excluir", lambda: excluir_evento(nome, self.carregar_eventos))
            menu.exec(self.tabela.mapToGlobal(pos))

    def abrir_evento(self, nome_evento: str):
        if nome_evento:
            self.controller.abrir_main_window(f"eventos/{nome_evento}/config/settings.json")
