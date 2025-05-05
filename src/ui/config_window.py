
from PyQt6.QtWidgets import (
    QWidget, QTabWidget, QVBoxLayout
)

from src.ui.layout_editor import LayoutEditor
from src.ui.impressao_config import ImpressaoConfigWidget
from src.ui.ia_config import IAConfigWidget
from src.ui.compartilhamento_config import CompartilhamentoConfigWidget


class ConfigWindow(QWidget):
    def __init__(self, controller, config_manager):
        super().__init__()
        self.controller = controller
        self.config_manager = config_manager

        self.setWindowTitle("⚙️ Configurações")
        self.setMinimumSize(900, 600)

        self.tabs = QTabWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.tabs)

        # 🎨 Layout (Editor Completo)
        self.layout_editor = LayoutEditor()
        self.tabs.addTab(self.layout_editor, "🎨 Layout")

        # 🖨️ Impressão
        self.impressao_config = ImpressaoConfigWidget(controller)
        self.tabs.addTab(self.impressao_config, "🖨️ Impressão")

        # 🤖 Inteligência Artificial
        self.ia_config = IAConfigWidget(controller)
        self.tabs.addTab(self.ia_config, "🤖 IA")

        # 📲 Compartilhamento
        self.compartilhamento_config = CompartilhamentoConfigWidget(controller)
        self.tabs.addTab(self.compartilhamento_config, "📲 Compartilhamento")

        # 📋 Relatório
        from src.ui.relatorio_config import RelatorioConfigWidget
        self.relatorio_config = RelatorioConfigWidget(controller)
        self.tabs.addTab(self.relatorio_config, "📋 Relatório")

        # ⚙️ Geral
        from src.ui.geral_config import GeralConfigWidget
        self.geral_config = GeralConfigWidget(controller)
        self.tabs.addTab(self.geral_config, "⚙️ Geral")

        self.compartilhamento_config = CompartilhamentoConfigWidget(controller)
