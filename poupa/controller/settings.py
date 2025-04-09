from pathlib import Path


# Inicialize as variáveis globais com valores padrão
# Path(os.getenv("APPDATA")) / "Poupa"
CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.json"  # Caminho para o arquivo de configuração
DATABASE_FILE = Path(__file__).resolve().parent.parent / "poupa.db"  # Caminho para o arquivo do banco de dados
