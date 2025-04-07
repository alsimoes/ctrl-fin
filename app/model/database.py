from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL

# Criar o engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Criar a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para inicializar o banco de dados
def init_db():
    from model.base import Base
    from model.orcamento import Orcamento  # Importe todos os modelos aqui

    # Criar as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)