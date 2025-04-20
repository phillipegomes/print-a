import os
import subprocess
import datetime
import json
import ast

# 🗂️ Caminhos importantes
PASTA_PROJETO = os.getcwd()
PASTA_LOGS = os.path.join(PASTA_PROJETO, "diagnostico", "diagnosticos", "logs")
ARQUIVO_RELATORIO = os.path.join(PASTA_LOGS, f"relatorio_diagnostico_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

# ✅ Utilitários
def registrar(msg):
    print(msg)
    with open(ARQUIVO_RELATORIO, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

# 🚀 Diagnóstico completo
def diagnostico_completo():
    registrar("🚀 Iniciando Diagnóstico Supremo 9.4...\n")

    # 📁 Verificação de estrutura
    for pasta in ["src", "tests", "diagnostico"]:
        path = os.path.join(PASTA_PROJETO, pasta)
        if os.path.isdir(path):
            registrar(f"✅ Pasta presente: {pasta}")
        else:
            registrar(f"❌ Pasta ausente: {pasta}")

    # 📄 Verificação de settings.json
    settings_path = os.path.join(PASTA_PROJETO, "eventos", "TesteEvent", "config", "settings.json")
    if os.path.exists(settings_path):
        try:
            with open(settings_path, encoding="utf-8") as f:
                data = json.load(f)
            if "nome" in data and "compartilhamento" in data:
                registrar("✅ settings.json OK")
            else:
                registrar("❌ settings.json incompleto (faltando 'nome' ou 'compartilhamento')")
        except Exception as e:
            registrar(f"❌ Erro ao ler settings.json: {str(e)}")
    else:
        registrar("❌ settings.json não encontrado")

    # 🔍 Verificação de imports (pylint)
    registrar("\n🔍 Verificando imports com pylint...")
    try:
        resultado = subprocess.run(["pylint", "src"], capture_output=True, text=True)
        erros = [linha for linha in resultado.stdout.splitlines() if "E0401" in linha or "E0611" in linha]
        if erros:
            for erro in erros:
                registrar(f"❌ Import inválido: {erro}")
        else:
            registrar("✅ Imports válidos")
    except Exception as e:
        registrar(f"⚠️ Erro ao executar pylint: {str(e)}")

    # 📦 Verificação de assets
    registrar("\n🔎 Verificando arquivos de assets...")
    assets = [
        "assets/teste.jpg",
        "assets/layouts/layout1.png",
        "assets/ia/cartoon.jpg"
    ]
    for asset in assets:
        if os.path.exists(asset):
            registrar(f"✅ Asset presente: {asset}")
        else:
            registrar(f"❌ Asset ausente: {asset}")

    # 🧠 Verificação de métodos via AST
    registrar("\n🔎 Verificando métodos principais...")
    caminhos = [
        ("src/ui/event_window.py", ["abrir_evento", "renomear_evento", "voltar_eventos"]),
        ("src/ui/main_window.py", ["carregar_foto", "atualizar_galeria"]),
        ("src/controllers/app_controller.py", ["start"])
    ]
    for arquivo, metodos in caminhos:
        if os.path.exists(arquivo):
            try:
                with open(arquivo, "r", encoding="utf-8") as f:
                    tree = ast.parse(f.read())
                    funcoes = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
                    for metodo in metodos:
                        if metodo in funcoes:
                            registrar(f"✅ Método presente: {metodo} em {arquivo}")
                        else:
                            registrar(f"❌ Método ausente: {metodo} em {arquivo}")
            except Exception as e:
                registrar(f"❌ Erro ao processar {arquivo}: {e}")
        else:
            registrar(f"❌ Arquivo não encontrado: {arquivo}")

    # ✅ Testes PyTest
    registrar("\n🧪 Executando testes PyTest...")
    try:
        subprocess.run(["pytest", "--maxfail=3", "--disable-warnings", "-v", "tests"], check=True)
        registrar("✅ PyTest executado com sucesso")
    except subprocess.CalledProcessError as e:
        registrar(f"❌ Erro no PyTest: código {e.returncode} — verifique os testes com falha")

    registrar("\n✅ Diagnóstico finalizado!")
    registrar(f"📁 Relatório salvo: {ARQUIVO_RELATORIO}")

# ▶️ Execução
if __name__ == "__main__":
    os.makedirs(PASTA_LOGS, exist_ok=True)
    diagnostico_completo()
