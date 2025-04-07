import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from poupa.settings import DATABASE_PATH

Base = declarative_base()

# Configura o engine do SQLAlchemy
engine = create_engine(f"sqlite:///{DATABASE_PATH}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Importa os modelos para garantir que sejam registrados no metadata
from poupa.model.budget import Budget  # Certifique-se de que o caminho está correto

def init_db():
    """Verifica se o banco de dados existe e o cria, se necessário."""
    if not os.path.exists(DATABASE_PATH):
        print(f"Banco de dados não encontrado...")
        print(f"Criando banco de dados...")
        Base.metadata.create_all(engine)
        print(f"Banco de dados criado... {os.path.basename(DATABASE_PATH)}")
    else:
        print(f"Banco de dados encontrado... {os.path.basename(DATABASE_PATH)}")