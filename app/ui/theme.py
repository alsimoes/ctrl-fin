import customtkinter as ctk

# Funções para alterar o tema e salvar no config.json
def tema_claro(config, salvar_configuracoes):
    ctk.set_appearance_mode("Light")
    config["theme"] = "Light"
    salvar_configuracoes(config)
    print("Tema alterado para Claro e salvo no config.json")

def tema_escuro(config, salvar_configuracoes):
    ctk.set_appearance_mode("Dark")
    config["theme"] = "Dark"
    salvar_configuracoes(config)
    print("Tema alterado para Escuro e salvo no config.json")

def tema_sistema(config, salvar_configuracoes):
    ctk.set_appearance_mode("System")
    config["theme"] = "System"
    salvar_configuracoes(config)
    print("Tema alterado para Sistema e salvo no config.json")