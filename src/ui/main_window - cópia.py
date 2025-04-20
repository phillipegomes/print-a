import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QHBoxLayout,
    QGridLayout, QMessageBox, QSpinBox
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QTimer

from src.ui.main_actions import carregar_imagens, imprimir_foto, excluir_foto
from src.modules.print_counter import PrintCounter
from src.modules.whatsapp_sender import enviar_por_whatsapp
from src.modules.backup_manager import salvar_em_backup
from src.ui.main_styles import MAIN_STYLE, BOTAO_STYLE

class MainWindow(QWidget):
    def __init__(self, controller, settings_path):
        super().__init__()
        self.controller = controller
        self.settings_path = settings_path
        self.evento_path = os.path.dirname(os.path.dirname(settings_path))
        self.nome_evento = os.path.basename(self.evento_path)

        self.setWindowTitle(f"Print A – Evento: {self.nome_evento}")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(MAIN_STYLE)

        self.pasta_fotos = os.path.join(self.evento_path, "fotos_prontas")
        self.print_counter = PrintCounter(self.nome_evento)
        self.limite_copias = 3
        self.config = controller.config_manager.config

        layout = QVBoxLayout(self)

        # 🔼 Barra superior com Configurações, Status e Galeria
        topo = QHBoxLayout()

        icon_gear = "assets/icons/gear.png"
        icon_gallery = "assets/icons/gallery.png"

        self.btn_config = QPushButton()
        if os.path.exists(icon_gear):
            self.btn_config.setIcon(QIcon(icon_gear))
        else:
            self.btn_config.setText("⚙️")
        self.btn_config.setFixedSize(48, 48)
        self.btn_config.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                color: white;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #444;
                border-radius: 8px;
            }
        """)
        self.btn_config.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_config.clicked.connect(lambda: controller.abrir_configuracoes(self.settings_path))

        wifi_nome = self.config.get("conexao", {}).get("wifi_nome")
        if wifi_nome:
            status_mifi = f"MiFi: <span style='color:#00e676'>{wifi_nome}</span>"
        else:
            status_mifi = "MiFi: <span style='color:#ff5252'>Offline</span>"

        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setText(f"<span style='color:white'>Impressas: 0</span> | {status_mifi} | <span style='color:white'>Restante: 0</span>")
        self.status_label.setStyleSheet("font-size: 14px;")

        self.btn_galeria = QPushButton()
        if os.path.exists(icon_gallery):
            self.btn_galeria.setIcon(QIcon(icon_gallery))
        else:
            self.btn_galeria.setText("🖼️")
        self.btn_galeria.setFixedSize(48, 48)
        self.btn_galeria.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
                color: white;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: #444;
                border-radius: 8px;
            }
        """)
        self.btn_galeria.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_galeria.clicked.connect(controller.abrir_galeria)

        topo.addWidget(self.btn_config)
        topo.addWidget(self.status_label, 1)
        topo.addWidget(self.btn_galeria)
        layout.addLayout(topo)

        # 🔽 Imagem principal
        self.imagem_label = QLabel("Nenhuma imagem")
        self.imagem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagem_label.setStyleSheet("border: 2px solid #333; padding: 10px;")
        layout.addWidget(self.imagem_label, 1)

        self.msg = QLabel("🖨️ Imprimindo...")
        self.msg.setStyleSheet("font-size: 16px; color: white; background-color: #222; padding: 6px; border-radius: 6px; border: 1px solid #555;")
        self.msg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.msg.setVisible(False)
        layout.addWidget(self.msg)

        # 🔽 Ações
        acoes = QHBoxLayout()

        self.btn_imprimir = QPushButton("🖨️")
        self.btn_imprimir.setStyleSheet(BOTAO_STYLE)
        self.btn_imprimir.clicked.connect(self.acao_imprimir)

        self.spin_copias = QSpinBox()
        self.spin_copias.setMinimum(1)
        self.spin_copias.setMaximum(self.limite_copias)
        self.spin_copias.setValue(1)
        self.spin_copias.setFixedWidth(60)

        self.btn_whatsapp = QPushButton("📲")
        self.btn_whatsapp.setStyleSheet(BOTAO_STYLE)
        self.btn_whatsapp.clicked.connect(self.acao_whatsapp)

        acoes.addStretch()
        acoes.addWidget(self.btn_imprimir)
        acoes.addWidget(self.spin_copias)
        if self.config.get("compartilhamento", {}).get("whatsapp_ativo"):
            acoes.addWidget(self.btn_whatsapp)
        acoes.addStretch()
        layout.addLayout(acoes)

        # 🔽 Miniaturas
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.thumb_widget = QWidget()
        self.thumb_layout = QHBoxLayout(self.thumb_widget)
        self.scroll.setWidget(self.thumb_widget)
        layout.addWidget(self.scroll)

        self.btn_voltar = QPushButton("← Voltar para eventos")
        self.btn_voltar.setStyleSheet(BOTAO_STYLE)
        self.btn_voltar.clicked.connect(self.controller.voltar_para_eventos)
        layout.addWidget(self.btn_voltar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.carregar_galeria)
        self.timer.start(3000)

        self.imagem_atual = None
        self.carregar_galeria()

    def carregar_galeria(self):
        imagens = carregar_imagens(self.pasta_fotos)
        for i in reversed(range(self.thumb_layout.count())):
            self.thumb_layout.itemAt(i).widget().deleteLater()

        if imagens:
            nova_imagem = imagens[-1]
            if self.imagem_atual != nova_imagem:
                self.exibir_imagem(nova_imagem)

        for caminho in imagens[-3:]:
            thumb = QPixmap(caminho).scaled(140, 140, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            thumb_label = QLabel()
            thumb_label.setPixmap(thumb)
            thumb_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            thumb_label.setStyleSheet("border: 2px solid #222;")
            thumb_label.mousePressEvent = lambda e, c=caminho: self.exibir_imagem(c)
            self.thumb_layout.addWidget(thumb_label)

    def exibir_imagem(self, caminho):
        pixmap = QPixmap(caminho).scaled(700, 500, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.imagem_label.setPixmap(pixmap)
        self.imagem_atual = caminho

    def acao_imprimir(self):
        if self.imagem_atual:
            self.msg.setVisible(True)
            QTimer.singleShot(1500, self.finalizar_impressao)

    def finalizar_impressao(self):
        self.msg.setVisible(False)
        imprimir_foto(self.pasta_fotos, self.controller.config_manager.config, self.spin_copias.value())
        self.print_counter.registrar_impressao(self.imagem_atual)
        salvar_em_backup({}, self.imagem_atual)
        self.carregar_galeria()

    def acao_whatsapp(self):
        if self.imagem_atual:
            numero = "5511999999999"
            enviar_por_whatsapp(numero, self.imagem_atual)
