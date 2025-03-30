import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("System")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

# Criar a janela principal
app = ctk.CTk()
app.title("Minha Aplicação com CustomTkinter")
app.geometry("500x300")

# Adicionar widgets
label = ctk.CTkLabel(app, text="Bem-vindo ao CustomTkinter!", font=("Arial", 20))
label.pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="Digite algo...")
entry.pack(pady=10)

button = ctk.CTkButton(app, text="Clique aqui", command=lambda: print("Botão clicado!"))
button.pack(pady=10)

# Rodar a aplicação
app.mainloop()