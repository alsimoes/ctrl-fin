import json
import os

config_path = "config.json"

bg_color = "#2E98C8"

def carregar_configuracoes():
    if os.path.exists(config_path):
        with open(config_path, "r") as file:
            return json.load(file)
    else:
        # Configurações padrão
        return {
            "window_size": {"width": 600, "height": 480},
            "theme": "System",
            "last_opened_file": None
        }

def salvar_configuracoes(config):
    with open(config_path, "w") as file:
        json.dump(config, file, indent=4)