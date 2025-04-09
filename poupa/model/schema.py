from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from poupa.model.database import init_db

class BudgetSchema(BaseModel):
    budget_name: str = Field(..., min_length=1, max_length=50, description="Nome do orçamento")
    purpose: Optional[str] = Field(None, max_length=140, description="Propósito do orçamento")
    currency: Optional[str] = Field(None, max_length=10, description="Moeda do orçamento")
    # id: str = Field(..., description="ID único para o orçamento")
    # start_date: datetime = Field(..., description="Data de início do orçamento")
    # end_date: Optional[datetime] = Field(None, description="Data de término do orçamento")
    # update_date: datetime = Field(..., description="Data da última atualização do orçamento")

    class Config:
        orm_mode = True