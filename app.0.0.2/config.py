# -*- coding: utf-8 -*-

LOG_LEVEL = "DEBUG"  # "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # Formato da mensagem
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"  # Formato da data
LOG_FILE_PATH = "c:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\app\\app.log"  # Caminho do arquivo de log
LOG_CONSOLE = True  # Se True, imprime os logs no console (terminal)
LOG_MODE = "w"  # Modo de abertura do arquivo de log ("a" para anexar, "w" para sobrescrever)
LOG_ENCODING = "utf-8"  # Codificação do arquivo de log

WINDOW_SIZE = {"width": 1024, "height": 768}  # Tamanho da janela (largura x altura)
WINDOW_POSITION = {"x": 100, "y": 100}  # Posição da janela (x, y)
WINDOW_THEME = "System"    # "System", "Dark", "Light"
WINDOW_RESIZABLE = {"width": True, "height": True}  # Se True, permite redimensionar a janela

FONT = "Helvetica"
FONT_NORMAL_SIZE = 12
FONT_TITLE_SIZE = 16

FONT_COLOR = "#000000"  # Preto
BACKGROUND_COLOR = "#FFFFFF"  # Branco


DATABASE_URL = "sqlite:///c:\\Users\\andre\\OneDrive\\Área de Trabalho\\CtrlFin\\ctrl-fin\\app\\database.db"
