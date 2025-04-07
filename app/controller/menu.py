import logging
from tkinter import messagebox

logger = logging.getLogger()


def novo_orcamento():
    """
    Comando para criar um novo arquivo.
    """
    logger.info("Novo orçamento criado.")
    messagebox.showinfo("Novo Orçamento", "Novo orçamento criado!")


def sair(app):
    """
    Comando para sair da aplicação.

    Args:
        app: Instância da janela principal da aplicação.
    """
    logger.info("Saindo da aplicação.")
    app.quit()


def sobre():
    """
    Comando para exibir informações sobre a aplicação.
    """
    logger.info("Exibindo informações sobre a aplicação.")
    messagebox.showinfo("Sobre", "Controle Financeiro\nVersão 1.0\nDesenvolvido por André Simões")