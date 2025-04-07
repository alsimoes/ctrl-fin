from sqlalchemy import Column, Integer, String, Float
from model.base import Base

class Orcamento(Base):
    __tablename__ = "orcamentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    moeda = Column(String, nullable=False)

    def __repr__(self):
        return f"<Orcamento(nome={self.nome}, moeda={self.moeda}>"