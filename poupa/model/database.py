from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configurações do SQLAlchemy
Base = declarative_base()
engine = None
SessionLocal = None

def database_config(database_path: str):
    """Configura o caminho do banco de dados e inicializa o SQLAlchemy."""
    global engine, SessionLocal
    engine = create_engine(f"sqlite:///{database_path}")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Inicializa o banco de dados, criando as tabelas, se necessário."""
    if engine is None:
        raise RuntimeError("O banco de dados não foi configurado. Chame 'database_config' primeiro.")
    Base.metadata.create_all(engine)

# Exporta os objetos e funções para serem acessados por outros módulos
__all__ = ["Base", "engine", "SessionLocal", "init_db", "database_config"]