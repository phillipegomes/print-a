import json
import os

class ConfigManager:
    def __init__(self, settings_path):
        self.settings_path = settings_path
        self.config = self.carregar_configuracoes()

    def get(self, chave, padrao=None):
        return self.config.get(chave, padrao)

    def carregar_configuracoes(self):
        if os.path.exists(self.settings_path):
            try:
                with open(self.settings_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"[CONFIG] Erro ao carregar configurações: {e}")
                return {}
        else:
            print("[CONFIG] Arquivo de configurações não encontrado, usando padrão.")
            return {}

    def salvar_configuracoes(self):
        try:
            with open(self.settings_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
            print(f"[CONFIG] Configuração salva: {self.settings_path}")
        except Exception as e:
            print(f"[CONFIG] Erro ao salvar configurações: {e}")

    def atualizar(self, chave, valor):
        self.config[chave] = valor
        self.salvar_configuracoes()
