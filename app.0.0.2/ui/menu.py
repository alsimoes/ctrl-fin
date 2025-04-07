from tkinter import Menu  # Importar Menu do tkinter
import logging

import app.controller.menu as controller

def criar_menu(app):
    """
    Cria o menu principal da aplicação.

    Args:
        app: Janela principal da aplicação.
    """
    menu_bar = Menu(app)  # Use Menu do tkinter

    logger = logging.getLogger()
    
    
    # Menu Arquivo
    menu_arquivo = Menu(menu_bar, tearoff=0)
    menu_arquivo.add_command(label="Criar novo orçamento", command=lambda: controller.novo_orcamento()) 
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=lambda: controller.sair(app))
    menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

    # Menu Ajuda
    menu_ajuda = Menu(menu_bar, tearoff=0)
    menu_ajuda.add_command(label="Sobre", command=lambda: controller.sobre())
    menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

    # Adicionar o menu à janela principal
    app.config(menu=menu_bar)