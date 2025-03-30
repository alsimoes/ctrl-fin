import customtkinter as ctk
from app.config import carregar_configuracoes, salvar_configuracoes
from app.ui.menu import criar_menu
from app.ui.theme import tema_claro, tema_escuro, tema_sistema
from app.ui.events import ao_redimensionar, ao_fechar, marcar_janela_inicializada
from app.ui.events import ao_fechar, marcar_janela_inicializada
from app.ui.views import visualizar_contas, visualizar_orcamento, visualizar_relatorios, configuracao_pagamentos, github_page, sobre

# Carregar configurações
config = carregar_configuracoes()

# Criar a janela principal
app = ctk.CTk()
app.title("Controle Financeiro")
print(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')
app.geometry(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')

def corrigir_tamanho_inicial():
    app.geometry(f'{config["window_size"]["width"]}x{config["window_size"]["height"]}')
    print("Tamanho corrigido para 1280x840")

# Configurar eventos
app.bind("<Configure>", lambda event: ao_redimensionar(event, app, config, salvar_configuracoes))
app.protocol("WM_DELETE_WINDOW", lambda: ao_fechar(app))

# Marcar a janela como inicializada após um pequeno atraso
app.after(100, marcar_janela_inicializada)
# app.after(200, corrigir_tamanho_inicial)

# Aplicar o tema salvo no config.json ao iniciar
ctk.set_appearance_mode(config["theme"])  # Modos: "System", "Dark", "Light"

# Criar o menu
criar_menu(app, 
           theme_callbacks={
               "tema_claro": lambda: tema_claro(config, salvar_configuracoes),
               "tema_escuro": lambda: tema_escuro(config, salvar_configuracoes),
               "tema_sistema": lambda: tema_sistema(config, salvar_configuracoes)
           },
           view_callbacks={"visualizar_contas": visualizar_contas, "visualizar_orcamento": visualizar_orcamento, 
                           "visualizar_relatorios": visualizar_relatorios, "configuracao_pagamentos": configuracao_pagamentos,
                           "github_page": github_page, "sobre": sobre},
           file_callbacks={"criar_orcamento": lambda: print("Criar orçamento"), "abrir": lambda: print("Abrir"),
                           "importar_transacoes": lambda: print("Importar transações"), "sair": lambda: app.quit()})

# Rodar a aplicação
app.mainloop()