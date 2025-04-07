from ttkbootstrap import Style
import logging

from app.config import *
from app.ui.menu import criar_menu
from app.ui.main_frame import criar_frame_principal

# Função para criar e rodar a interface gráfica
def create_window(window_size):
    logger = logging.getLogger()

    # Criar a janela principal com ttkbootstrap
    style = Style(theme="darkly")  # Escolha um tema (ex: "darkly", "flatly", "cosmo", etc.)
    app = style.master
    app.title("Controle Financeiro")

    # Configurar o tamanho da janela
    app.geometry(f"{window_size['width']}x{window_size['height']}")
    logger.debug(f"Janela criada com tamanho {window_size['width']}x{window_size['height']}")

    # Configurar o redimensionamento da janela
    app.resizable(WINDOW_RESIZABLE["width"], WINDOW_RESIZABLE["height"])
    logger.debug(f"Janela redimensionável: {WINDOW_RESIZABLE}")
    

    # Criar o menu
    criar_menu(app)

    # Criar o frame principal
    criar_frame_principal(app)

    # Rodar a aplicação
    app.mainloop()