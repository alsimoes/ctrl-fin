# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from sqlalchemy import Column, String, DateTime
from datetime import datetime, timezone
from poupa.model.database import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(String, primary_key=True, index=True) 
    name = Column(String, nullable=False)
    start_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))      
    update_date = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))    
    
