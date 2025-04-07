# -*- coding: utf-8 -*- 
import os
import logging
from app.config import *
import app.ui.window as ui

# Criar o logger principal
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)  # Nível de log (ex: DEBUG, INFO)

# Formato do log
formatter = logging.Formatter(LOG_FORMAT, datefmt=LOG_DATEFMT)

# Garantir que o diretório de logs exista
log_dir = os.path.dirname(LOG_FILE_PATH)
os.makedirs(log_dir, exist_ok=True)

# Handler para o arquivo de log
file_handler = logging.FileHandler(LOG_FILE_PATH, mode=LOG_MODE, encoding=LOG_ENCODING)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Handler para o console (terminal)
if LOG_CONSOLE:
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

# Inicializar a interface gráfica
if __name__ == "__main__":
    logger.info("Iniciando a aplicação...")
    ui.create_window(WINDOW_SIZE)