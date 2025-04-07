from tkinter import Menu

def criar_menu(app, theme_callbacks, view_callbacks, file_callbacks):
    menu_bar = Menu(app)

    # Menu Arquivo
    menu_arquivo = Menu(menu_bar, tearoff=0)
    menu_arquivo.add_command(label="Crie um orçamento", command=file_callbacks["criar_orcamento"])
    menu_arquivo.add_command(label="Abrir", command=file_callbacks["abrir"])
    menu_arquivo.add_command(label="Importar transações", command=file_callbacks["importar_transacoes"])
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Exit", command=file_callbacks["sair"])
    menu_bar.add_cascade(label="Arquivo", menu=menu_arquivo)

    # Menu Visualizações
    menu_visualizacoes = Menu(menu_bar, tearoff=0)
    menu_visualizacoes.add_command(label="Contas", command=view_callbacks["visualizar_contas"])
    menu_visualizacoes.add_command(label="Orçamento", command=view_callbacks["visualizar_orcamento"])
    menu_visualizacoes.add_command(label="Relatórios", command=view_callbacks["visualizar_relatorios"])
    menu_visualizacoes.add_command(label="Configuração de pagamentos", command=view_callbacks["configuracao_pagamentos"])

    # Submenu Tema
    menu_tema = Menu(menu_visualizacoes, tearoff=0)
    menu_tema.add_command(label="Claro", command=theme_callbacks["tema_claro"])
    menu_tema.add_command(label="Escuro", command=theme_callbacks["tema_escuro"])
    menu_tema.add_command(label="Sistema", command=theme_callbacks["tema_sistema"])
    menu_visualizacoes.add_cascade(label="Tema", menu=menu_tema)
    menu_bar.add_cascade(label="Visualizações", menu=menu_visualizacoes)

    # Menu Ajuda
    menu_ajuda = Menu(menu_bar, tearoff=0)
    menu_ajuda.add_command(label="GitHub Page", command=view_callbacks["github_page"])
    menu_ajuda.add_command(label="Sobre", command=view_callbacks["sobre"])
    menu_bar.add_cascade(label="Ajuda", menu=menu_ajuda)

    app.config(menu=menu_bar)