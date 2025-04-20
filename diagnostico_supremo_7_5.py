# SUPREMO 7.5 — Diagnóstico Completo e Compatível
# Atualizado para funcionar com qualquer versão de pylint, radon e Python 3.13+

import os
import json
import psutil
import subprocess
from datetime import datetime

def validar_settings_json():
    print("🔍 Validando estrutura dos arquivos settings.json...")
    eventos_dir = "eventos"
    for nome in os.listdir(eventos_dir):
        caminho_config = os.path.join(eventos_dir, nome, "config", "settings.json")
        if os.path.isfile(caminho_config):
            try:
                with open(caminho_config) as f:
                    json.load(f)
                print(f"✅ settings.json válido: {caminho_config}")
            except Exception:
                print(f"❌ Erro ao carregar JSON: {caminho_config}")

def uso_memoria():
    print("\n📊 Verificando uso de memória...")
    processo = psutil.Process(os.getpid())
    memoria = processo.memory_info().rss / 1024 / 1024
    print(f"✅ Memória usada: {memoria:.2f} MB")

def complexidade_radon():
    print("\n🧠 Verificando complexidade ciclomática com radon...")
    try:
        arquivos = []
        for raiz, _, files in os.walk("src"):
            for file in files:
                if file.endswith(".py"):
                    arquivos.append(os.path.join(raiz, file))
        for arquivo in arquivos:
            print(f"📁 {arquivo}")
            try:
                resultado = subprocess.check_output(["radon", "cc", "-a", arquivo], stderr=subprocess.DEVNULL)
                print(resultado.decode())
            except Exception:
                print(f"⚠️ Não foi possível analisar: {arquivo}")
    except FileNotFoundError:
        print("❌ Radon não está instalado. Use: pip install radon")

def rodar_pylint():
    print("\n🔎 Análise com pylint...")
    try:
        arquivos = []
        for raiz, _, files in os.walk("src"):
            for file in files:
                if file.endswith(".py"):
                    arquivos.append(os.path.join(raiz, file))
        for arquivo in arquivos:
            print(f"📁 {arquivo}")
            subprocess.run(["pylint", arquivo])
    except Exception as e:
        print(f"⚠️ Erro ao rodar pylint: {e}")

def salvar_log():
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = f"diagnosticos/logs/relatorio_diagnostico_{agora}.txt"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "w") as f:
        f.write("Relatório gerado pelo SUPREMO 7.5\n")
        f.write(f"Data e hora: {agora}\n")
    print(f"📁 Relatório salvo: {log_path}")

if __name__ == "__main__":
    print(f"# SUPREMO 7.5 — DIAGNÓSTICO COMPLETO — {datetime.now()}")
    validar_settings_json()
    uso_memoria()
    complexidade_radon()
    rodar_pylint()
    salvar_log()
