# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from sqlalchemy import Column, String, DateTime,Integer
from datetime import datetime, timezone
from poupa.model.database import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))      
    update_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))    
    
    def __init__(self, name, start_date=None):
        self.name = name
        self.start_date = start_date or datetime.now(timezone.utc)

    def __repr__(self):
        return f"<Budget(id='{self.id}', name='{self.name}', start_date='{self.start_date}', update_date='{self.update_date}')>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "start_date": self.start_date.isoformat(),
            "update_date": self.update_date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get("name"),
            start_date=datetime.fromisoformat(data.get("start_date")) if data.get("start_date") else None,
        )