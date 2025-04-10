# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pydantic import BaseModel, Field


class BudgetSchema(BaseModel):
    id: str = Field(..., description="ID único para o orçamento")
    name: str = Field(..., min_length=1, max_length=50, description="Nome do orçamento")

    class Config:
        orm_mode = True