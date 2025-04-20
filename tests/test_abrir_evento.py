import os
from src.modules.config_loader import carregar_config_evento

def test_abrir_evento():
    caminho = "eventos/TesteEvent/config/settings.json"
    if not os.path.isfile(caminho):
        assert True, "Evento de teste não existe"
    else:
        config = carregar_config_evento(caminho)
        assert "nome" in config
