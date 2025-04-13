# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from contextlib import contextmanager
from poupa.model import database as db


@contextmanager
def get_session():
    """
    Gerenciador de contexto para criar e fechar sessões do banco de dados.
    """
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()