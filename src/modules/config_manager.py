import os
import json

class ConfigManager:
    def __init__(self, caminho_config):
        self.caminho_config = caminho_config
        self.configuracoes = {}
        self._carregar()
        self._garantir_estrutura_padrao()

    def _carregar(self):
        if os.path.exists(self.caminho_config):
            try:
                with open(self.caminho_config, "r", encoding="utf-8") as f:
                    self.configuracoes = json.load(f)
                    print(f"[CONFIG] Configurações carregadas: {self.caminho_config}")
            except Exception as e:
                print(f"[CONFIG] Erro ao carregar config: {e}")
                self.configuracoes = {}
        else:
            print(f"[CONFIG] Arquivo não encontrado. Usando padrão.")
            self.configuracoes = {
                "modo_teste": True,
                "ia": {},
                "layout": {},
                "compartilhamento": {},
                "impressao": {},
                "smugmug": {}
            }
            self.salvar_config()

    def _garantir_estrutura_padrao(self):
        padrao = {
            "modo_teste": True,
            "ia": {},
            "layout": {},
            "compartilhamento": {},
            "impressao": {},
            "smugmug": {}
        }
        for chave, valor in padrao.items():
            self.configuracoes.setdefault(chave, valor)

    def salvar_config(self):
        try:
            with open(self.caminho_config, "w", encoding="utf-8") as f:
                json.dump(self.configuracoes, f, indent=4, ensure_ascii=False)
                print(f"[CONFIG] Configuração salva: {self.caminho_config}")
        except Exception as e:
            print(f"[CONFIG] Erro ao salvar config: {e}")

    def get(self, chave, default=None):
        return self.configuracoes.get(chave, default)

    @property
    def config(self):
        return self.configuracoes

    @property
    def settings_path(self):
        return self.caminho_config