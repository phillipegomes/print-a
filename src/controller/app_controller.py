from src.ui.event_window import EventWindow
from src.ui.main_window import MainWindow
from src.ui.config_window import ConfigWindow
from src.modules.config_manager import ConfigManager
from src.modules.logger import criar_logger  # ✅ Logger importado corretamente

class AppController:
    def __init__(self):
        self.event_window = None
        self.main_window = None
        self.config_window = None
        self.config_manager = None
        self.config_path = None
        self.nome_evento_atual = None

        # ✅ SUPREMO BLOCK: Logger centralizado
        self.logger = criar_logger()
        self.logger.info("Logger inicializado com sucesso.")

    def iniciar(self):
        """Inicia o sistema abrindo a janela de eventos"""
        self.event_window = EventWindow(controller=self)
        self.event_window.show()
        self.logger.info("Janela de eventos aberta.")

    def abrir_main_window(self, caminho_config):
        self.config_path = caminho_config
        self.config_manager = ConfigManager(caminho_config)
        self.nome_evento_atual = self.config_manager.get("nome_evento", "")

        self.main_window = MainWindow(controller=self, settings_path=caminho_config)
        self.main_window.show()
        evento_nome = self.nome_evento_atual or "(evento sem nome)"
        self.logger.info(f"MainWindow aberta para o evento: {evento_nome} ({self.config_path})")

    def abrir_configuracoes(self, config_path=None):
        self.config_window = ConfigWindow(controller=self, config_manager=self.config_manager)
        self.config_window.show()
        self.logger.info("Janela de configurações aberta.")

    def voltar_para_eventos(self):
        """Fecha a janela principal e volta para a janela de eventos"""
        if self.main_window:
            self.main_window.close()
            self.main_window = None
            self.logger.info("MainWindow fechada.")

        if self.event_window:
            self.event_window.show()
            self.logger.info("Retorno para a janela de eventos.")

    def abrir_galeria(self):
        """Abre a galeria a partir da janela principal"""
        if self.main_window:
            self.main_window.carregar_galeria()
            self.logger.info("Galeria aberta via MainWindow.")
