# -*- coding: utf-8 -*-
import json
from pathlib import Path
from typing import Any

# Inicialize as variáveis globais com valores padrão
CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.json"  # Caminho para o arquivo de configuração
DATABASE_FILE = Path(__file__).resolve().parent.parent / "poupa.db"  # Caminho para o arquivo do banco de dados

def load_config() -> dict[str, Any]:
    global CONFIG_FILE, DATABASE_FILE  # Declare que está usando as variáveis globais
    if not CONFIG_FILE.exists():
        print(f"{CONFIG_FILE = } not found!")
        json_file = {
            "config_file": str(CONFIG_FILE), 
            "database_file": str(DATABASE_FILE)
        }
        print(f"{json_file = }")
        save_config(json_file, CONFIG_FILE)
    else:
        print(f"{CONFIG_FILE = } found!")
        with open(CONFIG_FILE, "r") as file:
            json_file = json.load(file)
            print(f"{json_file = }")
            # CONFIG_FILE = Path(json_file["config_file"])
            # DATABASE_FILE = Path(json_file["database_file"])
    # if not DATABASE_FILE.exists():
    #     database_config(str(DATABASE_FILE))
    #     return {"notes_dir": str(DATABASE_FILE)}

def save_config(config: dict[str, Any], config_file: Path) -> None:
    with open(config_file, "w") as file:
        json.dump(config, file, indent=4)