# src/ui/impressao_config.py

"""
🧠 ImpressaoConfigWidget – Print A 3.5
Bloco responsável por exibir e aplicar as configurações de impressão do sistema.
Integrado ao ConfigManager e à aba de configurações principal.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox


class ImpressaoConfigWidget(QWidget):
    def __init__(self, controller):
        """
        Inicializa o widget de configurações de impressão.

        :param controller: Controller principal do sistema, com acesso ao ConfigManager
        """
        super().__init__()
        self.controller = controller
        self.config = controller.config_manager
        self.init_ui()

    def init_ui(self):
        """
        Monta a interface visual da aba de impressão.
        """
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Título
        layout.addWidget(QLabel("Configurações de Impressão"))

        # Checkbox de múltiplas cópias
        self.checkbox_copias = QCheckBox("Permitir múltiplas cópias por imagem")
        self.checkbox_copias.setChecked(self.config.get("permitir_multiplas_copias", True))
        layout.addWidget(self.checkbox_copias)

    def aplicar_configuracoes(self):
        """
        Salva as configurações marcadas na interface.
        """
        self.config.config["permitir_multiplas_copias"] = self.checkbox_copias.isChecked()
        self.config.salvar_configuracoes()
