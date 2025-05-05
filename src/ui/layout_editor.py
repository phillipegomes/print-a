
from PyQt6.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QGraphicsView, QGraphicsScene, QFrame, QListWidget, QListWidgetItem,
    QCheckBox, QComboBox, QSpinBox, QGridLayout, QGroupBox, QSizePolicy
)
from PyQt6.QtCore import Qt


# ✅ SUPREMO BLOCK: Layout Editor Completo – Estilo DSLRBooth (sem Texto/QR)
class LayoutEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Layout - Print A")
        self.setMinimumSize(1200, 700)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        # 🧭 Menu Superior
        topo_menu = QHBoxLayout()
        for nome in ["🆕 Novo", "💾 Salvar", "📤 Exportar", "🖨️ Teste Print", "🗑️ Apagar", "↩ Undo", "↪ Redo"]:
            topo_menu.addWidget(QPushButton(nome))
        main_layout.addLayout(topo_menu)

        # 📐 Layout horizontal: [Adicionar] [Canvas] [Painéis à direita]
        layout_horizontal = QHBoxLayout()
        main_layout.addLayout(layout_horizontal)

        # 🧩 Painel Lateral Esquerdo
        painel_add = QVBoxLayout()
        painel_add.addWidget(QLabel("➕ Adicionar Elemento"))
        for texto in ["🖼️ Imagem", "📸 Foto Booth", "🅰️ Texto", "⬛ Forma"]:
            painel_add.addWidget(QPushButton(texto))

        layout_info = QGroupBox("📐 Config Layout")
        info_layout = QVBoxLayout()
        info_layout.addWidget(QLabel("Tamanho: 1800 x 1200"))
        info_layout.addWidget(QLabel("DPI: 300"))
        layout_info.setLayout(info_layout)
        painel_add.addWidget(layout_info)
        layout_horizontal.addLayout(painel_add)

        # 🖼️ Canvas Central
        canvas_frame = QFrame()
        canvas_frame.setFrameShape(QFrame.Shape.Box)
        canvas_frame.setMinimumSize(600, 400)
        canvas_layout = QVBoxLayout(canvas_frame)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        canvas_layout.addWidget(self.view)
        layout_horizontal.addWidget(canvas_frame, 3)

        # 📋 Painel à Direita (Propriedades, Alinhamento, Camadas)
        painel_direita = QVBoxLayout()

        # ⚙️ Propriedades
        props = QGroupBox("⚙️ Propriedades")
        props_layout = QGridLayout()
        props_layout.addWidget(QLabel("X:"), 0, 0)
        props_layout.addWidget(QSpinBox(), 0, 1)
        props_layout.addWidget(QLabel("Y:"), 0, 2)
        props_layout.addWidget(QSpinBox(), 0, 3)
        props_layout.addWidget(QLabel("Largura:"), 1, 0)
        props_layout.addWidget(QSpinBox(), 1, 1)
        props_layout.addWidget(QLabel("Altura:"), 1, 2)
        props_layout.addWidget(QSpinBox(), 1, 3)
        props_layout.addWidget(QLabel("Rotação:"), 2, 0)
        props_layout.addWidget(QSpinBox(), 2, 1)
        props_layout.addWidget(QCheckBox("🔲 Manter Proporção"), 3, 0, 1, 2)
        props.setLayout(props_layout)
        painel_direita.addWidget(props)

        # 🔃 Alinhamento
        alinhamento = QGroupBox("🔃 Alinhamento")
        alin_layout = QGridLayout()
        alin_layout.addWidget(QPushButton("⬅ Esquerda"), 0, 0)
        alin_layout.addWidget(QPushButton("➡ Direita"), 0, 1)
        alin_layout.addWidget(QPushButton("⬆ Topo"), 1, 0)
        alin_layout.addWidget(QPushButton("⬇ Inferior"), 1, 1)
        alin_layout.addWidget(QPushButton("↔ Centralizar H"), 2, 0)
        alin_layout.addWidget(QPushButton("↕ Centralizar V"), 2, 1)
        alin_layout.addWidget(QPushButton("🧲 Snap/Grid"), 3, 0, 1, 2)
        alinhamento.setLayout(alin_layout)
        painel_direita.addWidget(alinhamento)

        # 📋 Camadas
        camadas = QGroupBox("📋 Camadas")
        camadas_layout = QVBoxLayout()
        for item in ["🔲 Foto Booth", "🔲 Imagem", "🔲 Texto", "🔲 Forma"]:
            camadas_layout.addWidget(QLabel(item))
        camadas.setLayout(camadas_layout)
        painel_direita.addWidget(camadas)

        layout_horizontal.addLayout(painel_direita)
        self.setLayout(main_layout)
