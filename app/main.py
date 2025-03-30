import logging
import customtkinter as ctk
from app.config import *
from app.ui.menu import *
from app.ui.theme import *
from app.ui.events import *
from app.ui.views import *

 
# Configurar o logging
logging.basicConfig(
    level=logging.INFO,  # Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Formato da mensagem
    datefmt="%Y-%m-%d %H:%M:%S"  # Formato da data
)

# Carregar configurações
logging.info("Carregando configurações do arquivo config.json...")

# Carregar configurações
config = carregar_configuracoes()
logging.info(f"Configurações carregadas: {config}")

# Criar a janela principal
app = ctk.CTk()
app.title("Controle Financeiro")
# print(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')
app.geometry(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')
logging.info(f"Janela dimensionada: {config["window_size"]["width"]}x{config["window_size"]["height"]}")

def corrigir_tamanho_inicial():
    app.geometry(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')
    logging.info(f"corrigir_tamanho_inicial -> Janela dimensionada: {config["window_size"]["width"]}x{config["window_size"]["height"]}")
    # print("Tamanho corrigido para 1280x840")

# Configurar eventos
app.bind("<Configure>", lambda event: ao_redimensionar(event, app, logging, config, salvar_configuracoes))
app.protocol("WM_DELETE_WINDOW", lambda: ao_fechar(app, logging))

# Marcar a janela como inicializada após um pequeno atraso
app.after(100, marcar_janela_inicializada(logging))
# app.after(200, corrigir_tamanho_inicial)

# Aplicar o tema salvo no config.json ao iniciar
ctk.set_appearance_mode(config["theme"])  # Modos: "System", "Dark", "Light"

# Criar o menu
criar_menu(app, 
           theme_callbacks={
               "tema_claro": lambda: tema_claro(config, logging, salvar_configuracoes),
               "tema_escuro": lambda: tema_escuro(config, logging, salvar_configuracoes),
               "tema_sistema": lambda: tema_sistema(config, logging, salvar_configuracoes)
           },
           view_callbacks={"visualizar_contas":  lambda: visualizar_contas(logging), "visualizar_orcamento":  lambda: visualizar_orcamento(logging), 
                           "visualizar_relatorios":  lambda: visualizar_relatorios(logging), "configuracao_pagamentos":  lambda: configuracao_pagamentos(logging),
                           "github_page":  lambda: github_page(logging), "sobre": lambda:  sobre(logging)},
           file_callbacks={"criar_orcamento": lambda: criar_orcamento(logging), "abrir": lambda: abrir(logging),
                           "importar_transacoes": lambda: importar_transacoes(logging), "sair": lambda: sair(app, logging)})

# Cria tela principal
criar_tela_principall(app, logging)

# Rodar a aplicação
app.mainloop()