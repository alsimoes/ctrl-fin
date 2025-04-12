# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from poupa.model.database import Base

class Account(Base):
    __tablename__ = "accounts"

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=True)
    account_type_id = Column(Integer, ForeignKey("account_types.id"), nullable=False)
    impact_budget = Column(Integer, nullable=False, default=0)
    balance = Column(String, nullable=True, default=None)
    balance_date = Column(DateTime, nullable=True, default=None)
    update_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # Relationships
    account_type = relationship("AccountType")    
    budget = relationship("Budget", back_populates="accounts")

    def __init__(self, name, budget_id=None, balance=None, balance_date=None, impact_budget=False, account_type=None):
        self.name = name
        self.budget_id = budget_id
        self.account_type = account_type
        self.impact_budget = int(impact_budget)
        self.balance = balance or None
        self.balance_date = balance_date or None
                

    def __repr__(self):
        return f"<Account({self.id = }, {self.name = }, {self.account_type = }, {self.impact_budget = }, {self.balance = }, {self.balance_date = })>"


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "account_type": self.account_type.name if self.account_type else None,
            "impact_budget": self.impact_budget,
            "balance": self.balance,
            "balance_date": self.balance_date.strftime("%d/%m/%Y") if self.balance_date else None,
        }


    # @classmethod
    # def from_dict(cls, data):
    #     return cls(
    #         name=data.get("name"),
    #         start_date=datetime.fromisoformat(data.get("start_date")) if data.get("start_date") else None,
    #     )
        
class AccountType(Base):
    __tablename__ = "account_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    

    def __repr__(self):
        return f"<AccountType({self.id = }, {self.name = })>"