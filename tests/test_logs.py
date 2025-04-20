import os

def test_logs_vazio():
    caminho = "logs/erro_atual.log"
    if not os.path.isfile(caminho):
        assert True
    else:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
        assert "Traceback" not in conteudo, "❌ Log contém erro não tratado"
