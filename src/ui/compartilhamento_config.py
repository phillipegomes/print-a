# src/ui/compartilhamento_config.py
# SUPREMO – Aba de Compartilhamento nas Configurações

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox

class CompartilhamentoConfigWidget(QWidget):
    """
    Aba de configurações relacionadas ao compartilhamento de fotos,
    incluindo modo offline e futuras integrações com redes sociais.
    """
    def __init__(self, controller):
        super().__init__()

        # ✅ SUPREMO FIX – Acesso correto às configurações
        self.controller = controller
        self.config_manager = controller.config_manager
        self.config = self.config_manager.config  # Garante que get() funciona

        layout = QVBoxLayout()
        self.setLayout(layout)

        # 📲 Checkbox para modo offline (ex: eventos sem internet)
        self.checkbox_offline = QCheckBox("Ativar modo offline")
        self.checkbox_offline.setChecked(self.config.get("compartilhamento_offline", False))
        layout.addWidget(QLabel("Modo de Compartilhamento"))
        layout.addWidget(self.checkbox_offline)

        # Você pode adicionar mais campos aqui conforme a evolução da aba
