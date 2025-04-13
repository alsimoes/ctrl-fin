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


class BudgetValidator(BaseModel):
    id: int | None = Field(default=None, description="ID do orçamento (opcional para criação)")
    name: str = Field(..., min_length=1, max_length=50, description="Nome do orçamento")
    start_date: datetime = Field(..., description="Data de início do orçamento")
    update_date: datetime | None = Field(default=None, description="Data de atualização do orçamento")

    @field_validator("start_date", pre=True)
    def validate_start_date(cls, value):
        """Valida que a data de início não está no futuro."""
        if isinstance(value, str):
            value = datetime.fromisoformat(value)
        if value > datetime.now():
            raise ValueError("A data de início não pode estar no futuro.")
        return value

    @field_validator("update_date", pre=True, always=True)
    def set_update_date(cls, value, values):
        """Define a data de atualização como a data atual, se não fornecida."""
        return value or datetime.now()

    @field_validator("name")
    def validate_name(cls, value):
        """Valida que o nome não é vazio ou muito longo."""
        if not value.strip():
            raise ValueError("O nome do orçamento não pode estar vazio.")
        return value