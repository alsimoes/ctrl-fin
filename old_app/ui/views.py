from tkinter import Frame, Label, Button, messagebox, filedialog
from ..config import bg_color

def criar_tela_principall(app, logging):
    logging.info("Tela incial")
    
    # Main frame
    tela_principall = Frame(app)
    tela_principall.pack(fill="both", expand=True)
    tela_principall.configure(bg=bg_color)

    # (Left Section
    frame_left = Frame(tela_principall, bg=bg_color)
    frame_left.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        
    # Center Section
    frame_center = Frame(tela_principall,bg=bg_color)
    frame_center.place(relx=0.3, rely=0, relwidth=0.4, relheight=1)
    
    # Right Section
    frame_right = Frame(tela_principall,bg=bg_color)
    frame_right.place(relx=0.70, rely=0, relwidth=0.3, relheight=1)
    
    # Add widgets to the frames
    Label(frame_center, text="Center Section", bg="lightgray").pack(pady=10)
    
    # Center sections
    frame_center_top = Frame(frame_center,bg=bg_color)
    frame_center_top.place(relx=0, rely=0, relwidth=1, relheight=0.25)
    
    # Ultimo orçamento sections
    frame_center_buttons = Frame(frame_center,bg="yellow")
    frame_center_buttons.place(relx=0, rely=0.25, relwidth=1, relheight=0.20)
    
    # Ultimo orçamento sections
    frame_center_botton = Frame(frame_center,bg=bg_color)
    frame_center_botton.place(relx=0, rely=0.45, relwidth=1, relheight=1)
    
    # Botões
    botao_ultimo_orcamento = Button(frame_center_buttons,bg="green")
    botao_ultimo_orcamento.configure(
        height=3, 
        text="Último Orçamento", 
        command=lambda: abrir(logging), 
        font=("Arial", 14), 
        fg="white")
    botao_ultimo_orcamento.pack(fill="x", side="top", padx=0, pady=0)

    botao_abrir_orcamento = Button(frame_center_buttons,bg="lightgray")
    botao_abrir_orcamento.configure(
        height=1, 
        text="Abrir orçamento", 
        command=lambda: abrir(logging), 
        font=("Arial", 12), 
        fg="black")
    botao_abrir_orcamento.pack(side="left", fill="x", expand=True, padx=0, pady=0)
    
    botao_novo_orcamento = Button(frame_center_buttons,bg="lightgray")
    botao_novo_orcamento.configure(
        height=1, 
        text="Abrir orçamento", 
        command=lambda: criar_tela_orcamento(app, logging), 
        font=("Arial", 12), 
        fg="black")
    botao_novo_orcamento.pack(side="left", fill="x", expand=True, padx=0, pady=0)
    
def criar_tela_orcamento(app, logging):
    logging.info("Tela orçamento")
    
    # Main frame
    tela_orcamento = Frame(app)
    tela_orcamento.pack(fill="both", expand=True)
    tela_orcamento.configure(bg=bg_color)

    # Frame 1 (Top Section)
    frame_top = Frame(tela_orcamento, bg="lightblue", height=100)
    frame_top.pack(fill="x", side="top", padx=10, pady=10)

    # Frame 2 (Left Section)
    frame_left = Frame(tela_orcamento, bg="lightgray", width=200)
    frame_left.pack(fill="y", side="left", padx=10, pady=10)

    # Frame 3 (Main Content Area)
    frame_main = Frame(tela_orcamento, bg="white")
    frame_main.pack(fill="both", expand=True, side="left", padx=10, pady=10)

    # Add widgets to the frames
    Label(frame_top, text="Top Section", bg="lightblue").pack(pady=10)
    Label(frame_left, text="Left Section", bg="lightgray").pack(pady=10)
    Label(frame_main, text="Main Content Area", bg="white").pack(pady=10)
    

def visualizar_contas(logging):
    logging.info("Visualizar contas selecionado")

def visualizar_orcamento(logging):
    logging.info("Visualizar orçamento selecionado")

def visualizar_relatorios(logging):
    logging.info("Visualizar relatórios selecionado")

def configuracao_pagamentos(logging):
    logging.info("Configuração de pagamentos selecionado")

def github_page(logging):
    logging.info("GitHub Page selecionado")

def sobre(logging):
    logging.info("Sobre selecionado")
    
     
def criar_orcamento(logging):
    logging.info("Criar orçamento")
    
    
def abrir(logging):
    logging.info("Abrir")
    
    
def importar_transacoes(logging):
    logging.info("Importar transações")
    
    
def sair(app, logging):
    logging.info("Saindo...")
    app.quit()