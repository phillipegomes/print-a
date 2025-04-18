# src/modules/print_counter.py
# BLOCO 4B - Contador de impressões por imagem com limite configurável

import os
import json

# 🧠 Explicação:
# Este módulo registra quantas vezes cada imagem foi impressa durante o evento.
# Ele permite aplicar um limite máximo de impressões por imagem.
# O controle é feito por um JSON salvo na pasta do evento.


class PrintCounter:
    def __init__(self, evento_nome):
        self.evento_nome = evento_nome
        self.arquivo_contador = os.path.join("eventos", evento_nome, "config", "print_counter.json")
        os.makedirs(os.path.dirname(self.arquivo_contador), exist_ok=True)
        self.dados = self._carregar()

    def _carregar(self):
        if os.path.exists(self.arquivo_contador):
            try:
                with open(self.arquivo_contador, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _salvar(self):
        try:
            with open(self.arquivo_contador, "w") as f:
                json.dump(self.dados, f, indent=2)
        except Exception as e:
            print(f"[ERRO] Falha ao salvar contador: {e}")

    def pode_imprimir(self, caminho_imagem, limite=1):
        chave = os.path.basename(caminho_imagem)
        return self.dados.get(chave, 0) < limite

    def registrar_impressao(self, caminho_imagem):
        chave = os.path.basename(caminho_imagem)
        self.dados[chave] = self.dados.get(chave, 0) + 1
        self._salvar()

    def get_contagem(self, caminho_imagem):
        chave = os.path.basename(caminho_imagem)
        return self.dados.get(chave, 0)
