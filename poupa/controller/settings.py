# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path


# Inicialize as variáveis globais com valores padrão
# Path(os.getenv("APPDATA")) / "Poupa"
CONFIG_FILE: str = Path(__file__).resolve().parent.parent / "config.json"  # Caminho para o arquivo de configuração
DATABASE_FILE: str = Path(__file__).resolve().parent.parent / "poupa.db"  # Caminho para o arquivo do banco de dados
