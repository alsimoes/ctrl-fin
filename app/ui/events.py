# Variável de controle para evitar salvar dimensões durante a inicialização
janela_inicializada = False

def ao_redimensionar(event, app, config, salvar_configuracoes):
    global janela_inicializada
    
    # Obter dimensões reais definidas no código
    dimensoes_reais = app.geometry()  # Retorna algo como "1280x840+100+100"
    largura_real, resto = dimensoes_reais.split('x')
    altura_real = resto.split('+')[0]  # Pega apenas a altura antes do "+"

    largura_real = int(largura_real)
    altura_real = int(altura_real)
    
    if janela_inicializada:  # Só salva as dimensões após a inicialização
        if (config["window_size"]["width"] != largura_real or config["window_size"]["height"] != altura_real):
            config["window_size"]["width"] = largura_real
            config["window_size"]["height"] = altura_real
            salvar_configuracoes(config)
            print(f"Janela redimensionada: {largura_real}x{altura_real}")

def ao_fechar(app):
    # Obter dimensões ajustadas pelo Windows
    largura_ajustada = app.winfo_width()
    altura_ajustada = app.winfo_height()

    # Obter dimensões reais definidas no código
    dimensoes_reais = app.geometry()  # Retorna algo como "1280x840+100+100"
    largura_real, resto = dimensoes_reais.split('x')
    altura_real = resto.split('+')[0]  # Pega apenas a altura antes do "+"

    largura_real = int(largura_real)
    altura_real = int(altura_real)

    print(f"Dimensões ajustadas pelo Windows: {largura_ajustada}x{altura_ajustada}")
    print(f"Dimensões reais definidas no código: {largura_real}x{altura_real}")

    # Fechar a aplicação
    app.destroy()

def marcar_janela_inicializada():
    global janela_inicializada
    janela_inicializada = True
    print("Janela inicializada.")
    
    