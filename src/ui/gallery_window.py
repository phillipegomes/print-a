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

class GalleryWindow(QWidget):
    def __init__(self, evento_path, config_manager):
        super().__init__()
        self.setWindowTitle(f"🖼️ Galeria de Fotos – {os.path.basename(evento_path)}")
        self.setMinimumSize(1000, 700)
        self.setStyleSheet(MAIN_STYLE)

        self.evento_path = evento_path
        self.pasta_fotos = os.path.join(evento_path, "fotos_prontas")
        self.config = config_manager.config
        self.print_counter = PrintCounter(os.path.basename(evento_path))
        self.limite_copias = 3
        self.caminho_selecionado = None

        layout = QVBoxLayout(self)

        titulo = QLabel(f"🖼️ Galeria de Fotos – {os.path.basename(evento_path)}")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; margin: 10px; color: white;")
        layout.addWidget(titulo)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.grid = QGridLayout(self.scroll_widget)
        self.grid.setSpacing(12)
        self.scroll.setWidget(self.scroll_widget)
        layout.addWidget(self.scroll)

        self.timer = QTimer()
        self.timer.timeout.connect(self.carregar_imagens)
        self.timer.start(5000)

        self.carregar_imagens()

    def carregar_imagens(self):
        imagens = sorted(carregar_imagens(self.pasta_fotos), key=os.path.getmtime, reverse=True)

        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().deleteLater()

        for idx, caminho in enumerate(imagens):
            thumb = QPixmap(caminho).scaled(180, 180, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

            img_label = QLabel()
            img_label.setPixmap(thumb)
            img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            img_label.setObjectName(caminho)
            img_label.mousePressEvent = lambda e, c=caminho: self.selecionar_imagem(c)

            # Aplica borda se for a imagem selecionada
            if caminho == self.caminho_selecionado:
                img_label.setStyleSheet("border: 2px solid #00e676;")
            else:
                img_label.setStyleSheet("border: 2px solid transparent;")

            msg_imprimindo = QLabel("🖨️ Imprimindo...")
            msg_imprimindo.setAlignment(Qt.AlignmentFlag.AlignCenter)
            msg_imprimindo.setStyleSheet("font-size: 14px; color: white; background-color: #222; padding: 5px 10px; border-radius: 6px; border: 1px solid #555;")
            msg_imprimindo.setVisible(False)

            spin = QSpinBox()
            spin.setMinimum(1)
            spin.setMaximum(self.limite_copias)
            spin.setValue(1)
            spin.setFixedWidth(60)

            btn_imprimir = QPushButton("🖨️")
            btn_excluir = QPushButton("🗑️")
            btn_whatsapp = QPushButton("📲")

            for btn in (btn_imprimir, btn_excluir, btn_whatsapp):
                btn.setStyleSheet(BOTAO_STYLE)
                btn.setCursor(Qt.CursorShape.PointingHandCursor)

            btn_imprimir.clicked.connect(lambda _, c=caminho, s=spin, m=msg_imprimindo: self.imprimir(c, s.value(), m))
            btn_excluir.clicked.connect(lambda _, c=caminho: self.excluir(c))
            btn_whatsapp.clicked.connect(lambda _, c=caminho: self.enviar_whatsapp(c))

            botoes = QHBoxLayout()
            botoes.addWidget(btn_imprimir)
            botoes.addWidget(spin)
            if self.config.get("compartilhamento", {}).get("whatsapp_ativo"):
                botoes.addWidget(btn_whatsapp)
            botoes.addWidget(btn_excluir)

            caixa = QVBoxLayout()
            caixa.addWidget(img_label)
            caixa.addWidget(msg_imprimindo)
            caixa.addLayout(botoes)

            container = QWidget()
            container.setLayout(caixa)
            container.setStyleSheet("padding: 8px; border: 1px solid #444; border-radius: 8px; background: #222;")

            self.grid.addWidget(container, idx // 3, idx % 3)

    def selecionar_imagem(self, caminho):
        self.caminho_selecionado = caminho
        self.carregar_imagens()

    def imprimir(self, caminho, copias, msg_label):
        if not self.print_counter.pode_imprimir(caminho, self.limite_copias):
            QMessageBox.warning(self, "Limite atingido", f"Essa imagem já foi impressa {self.limite_copias}x.")
            return

        msg_label.setVisible(True)
        QTimer.singleShot(1500, lambda: self.finalizar_impressao(caminho, copias, msg_label))

    def finalizar_impressao(self, caminho, copias, msg_label):
        try:
            if msg_label and msg_label.isVisible():
                msg_label.setVisible(False)
        except RuntimeError:
            print("[AVISO] QLabel já deletado ao finalizar impressão.")

        imprimir_foto(self.pasta_fotos, self.config, copias)
        self.print_counter.registrar_impressao(caminho)
        salvar_em_backup({}, caminho)
        self.carregar_imagens()

    def excluir(self, caminho):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Excluir")
        msg_box.setText("Deseja realmente excluir esta imagem?")
        btn_sim = msg_box.addButton("Sim", QMessageBox.ButtonRole.YesRole)
        btn_nao = msg_box.addButton("Não", QMessageBox.ButtonRole.NoRole)
        msg_box.exec()

        if msg_box.clickedButton() == btn_sim:
            if excluir_foto(caminho):
                self.carregar_imagens()

    def enviar_whatsapp(self, caminho):
        numero = "5511999999999"
        enviado = enviar_por_whatsapp(numero, caminho)
        if enviado:
            QMessageBox.information(self, "Enviado", f"Imagem enviada para {numero}.")
