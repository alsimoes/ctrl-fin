# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree
# .
from datetime import datetime
from pydantic import BaseModel, Field, field_validator

# TODO: Refatorar para usar o pydantic v2.0+
# TODO: Refatorar para quebrar em arquivos separados

class BudgetValidator(BaseModel):
    id: int | None = Field(default=None, description="ID do orçamento (opcional para criação)")
    name: str = Field(..., min_length=1, max_length=50, description="Nome do orçamento")
    start_date: datetime = Field(..., description="Data de início do orçamento")
    update_date: datetime | None = Field(default=None, description="Data de atualização do orçamento")

    @field_validator("start_date", mode="before")
    def validate_start_date(cls, value):
        """Valida que a data de início não está no futuro."""
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        if value > datetime.now():
            raise ValueError("A data de início não pode estar no futuro.")
        return value

    @field_validator("name")
    def validate_name(cls, value):
        """Valida que o nome não é vazio ou muito longo."""
        if not value.strip():
            raise ValueError("O nome do orçamento não pode estar vazio.")
        return value
    
    def for_creation(self) -> dict:
        """
        Retorna os dados necessários para a criação de um novo registro,
        excluindo os campos 'id' e 'update_date'.
        """
        return self.model_dump(exclude={"id", "update_date"})
    
class AccountValidator(BaseModel):
    id: int | None = Field(default=None, description="ID da conta (opcional para criação)")
    name: str = Field(..., min_length=1, max_length=50, description="Nome da conta")
    budget_id: int = Field(default=None, description="ID do orçamento associado (opcional)")
    account_type_id: int = Field(..., description="ID do tipo de conta")
    impact_budget: bool = Field(default=False, description="Impacta o orçamento?")
    balance: float | None = Field(default=None, description="Saldo da conta (opcional)")
    balance_date: datetime | None = Field(default=None, description="Data do saldo (opcional)")

    @field_validator("balance", mode="before")
    def validate_balance(cls, value):
        """Valida que o saldo é um número positivo."""
        if value is not None and value < 0:
            raise ValueError("O saldo não pode ser negativo.")
        return value
    
    def for_creation(self) -> dict:
        """
        Retorna os dados necessários para a criação de um novo registro,
        excluindo os campos 'id' e 'update_date'.
        """
        return self.model_dump(exclude={"id"})
    
class AccountTypeValidator(BaseModel):
    id: int | None = Field(default=None, description="ID do tipo de conta (opcional para criação)")
    name: str = Field(..., min_length=1, max_length=50, description="Nome do tipo de conta")

    @field_validator("name")
    def validate_name(cls, value):
        """Valida que o nome não é vazio ou muito longo."""
        if not value.strip():
            raise ValueError("O nome do tipo de conta não pode estar vazio.")
        return value
    
    def for_creation(self) -> dict:
        """
        Retorna os dados necessários para a criação de um novo registro,
        excluindo os campos 'id' e 'update_date'.
        """
        return self.model_dump(exclude={"id"})