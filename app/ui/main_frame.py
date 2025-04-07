from ttkbootstrap import ttk
import logging

logger = logging.getLogger()

def criar_frame_principal(app):
    """
    Cria o frame principal da aplicação.

    Args:
        app: Janela principal da aplicação.
    """    
    frame = ttk.Frame(app)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    
    return frame

# def adicionar_widgets_frame_principal(frame):
#     """
#     Adiciona widgets ao frame principal.
# 
#     Args:
#         frame: Frame principal da aplicação.
#     """
#     label = ttk.Label(frame, text="Bem-vindo ao Controle Financeiro!", font=("Helvetica", 16))
#     label.pack(pady=20)
#     
#      # Adicionar o frame com duas colunas
#      # criar_novo_orcamento(frame)
    
    
def criar_novo_orcamento(parent_frame):
    """
    Adiciona um frame com quatro colunas: left_spacer, title_frame, form_frame e right_spacer.

    Args:
        parent_frame: Frame pai onde as colunas serão adicionadas.
    """
    # Criar o frame para organizar as colunas
    
    frame_colunas = ttk.Frame(parent_frame)
    frame_colunas.pack(fill="both", expand=True, padx=10, pady=10)

    # Coluna left_spacer
    left_spacer = ttk.Frame(frame_colunas, width=25)  # Espaço vazio à esquerda
    left_spacer.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

    # Coluna title_frame
    title_frame = ttk.Frame(frame_colunas)
    title_frame.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    label_title = ttk.Label(title_frame, text="Configuração", font=("Helvetica", 22, "bold"), anchor="e")
    label_title.pack(pady=10)
    label_title = ttk.Label(title_frame, text="do Orçamento", font=("Helvetica", 22, "bold"), anchor="e")
    label_title.pack(pady=10)
    

    # Coluna form_frame
    form_frame = ttk.Frame(frame_colunas)
    form_frame.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
    label_form = ttk.Label(form_frame, text="Nome do orçamento:", font=("Helvetica", 12), anchor="w")
    label_form.pack(pady=10)
    entry_form = ttk.Entry(form_frame, font=("Helvetica", 12))
    entry_form.pack(pady=5)
    label_form = ttk.Label(form_frame, text="Moeda", font=("Helvetica", 12), anchor="w")
    label_form.pack(pady=10)
    listbox_moeda = ttk.Combobox(form_frame, font=("Helvetica", 12), values=["Real - BRL", "Dólar - USD"])
    listbox_moeda.pack(pady=5)
    # Botão "Cancelar"
    btn_cancelar = ttk.Button(form_frame, text="Cancelar", style="TButton", command=lambda: logger.debug("Operação cancelada"))
    btn_cancelar.pack(side="left", padx=5, pady=20)

    # Botão "Criar orçamento"
    btn_criar = ttk.Button(form_frame, text="Criar orçamento", style="TButton", command=lambda: logger.debug("Orçamento criado"))
    btn_criar.pack(side="right", padx=5, pady=20)

    # Estilos personalizados para os botões
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12))
    style.configure("TButton", padding=5)
    style.map("TButton", background=[("active", "gray"), ("!active", "gray")])

    # Coluna right_spacer
    right_spacer = ttk.Frame(frame_colunas, width=25)  # Espaço vazio à direita
    right_spacer.grid(row=0, column=3, padx=5, pady=5, sticky="ns")

    # Configurar o redimensionamento das colunas com proporções específicas
    frame_colunas.columnconfigure(0, weight=1)  # left_spacer (25%)
    frame_colunas.columnconfigure(1, weight=2)  # title_frame (20%)
    frame_colunas.columnconfigure(2, weight=3)  # form_frame (30%)
    frame_colunas.columnconfigure(3, weight=1)  # right_spacer (25%)