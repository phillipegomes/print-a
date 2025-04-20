import os, shutil, json
from datetime import datetime
from src.ui.event_actions import criar_evento

PASTA = "eventos"
NOME = "TesteAuto_" + datetime.now().strftime("%H%M%S")

def teardown_module(module):
    caminho = os.path.join(PASTA, NOME)
    if os.path.exists(caminho): shutil.rmtree(caminho)

def test_criar_evento():
    callback = lambda: None
    criar_evento(callback, nome_evento=NOME)
    caminho = os.path.join(PASTA, NOME)
    assert os.path.exists(caminho)
    settings = os.path.join(caminho, "config", "settings.json")
    assert os.path.isfile(settings)
    with open(settings, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["nome"] == NOME
