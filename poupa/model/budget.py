from sqlalchemy import Column, String, DateTime
from datetime import datetime, timezone
from poupa.model.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(String, primary_key=True, index=True)  # ID único para cada orçamento
    budget_name = Column(String, nullable=False)  # Nome do orçamento
    purpose = Column(String, nullable=True)  # Propósito do orçamento
    start_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))  # Data de início do orçamento
    end_date = Column(DateTime, nullable=True)  # Data de término do orçamento
    update_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Data da última atualização do orçamento
    currency = Column(String, nullable=True)  # Moeda do orçamento
    
    '''
    initial_value = Column(String, nullable=True)  # Valor inicial do orçamento
    value = Column(String, nullable=True)  # Valor final do orçamento
    '''