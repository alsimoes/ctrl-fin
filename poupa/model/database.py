# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Configurações do SQLAlchemy
Base = declarative_base()
engine: Engine = None
SessionLocal: Session = None

def config(database_path: str):
    """Configura o caminho do banco de dados e inicializa o SQLAlchemy."""
    global engine, SessionLocal
    if not os.path.exists(database_path):
        engine = create_engine(f"sqlite:///{database_path}", echo=True)
        
        init_db()
    else:
        engine = create_engine(f"sqlite:///{database_path}")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    
def init_db():
    global engine, SessionLocal
    """Inicializa o banco de dados, criando as tabelas, se necessário."""
    if engine is None:
        raise RuntimeError("O banco de dados não foi configurado. Chame 'config' primeiro.")
    Base.metadata.create_all(engine)

def update_db():
    global engine
    """Atualiza a estrutura do banco de dados, aplicando alterações no esquema."""
    if engine is None:
        raise RuntimeError("O banco de dados não foi configurado. Chame 'config' primeiro.")
    with engine.connect() as connection:
        for table in Base.metadata.sorted_tables:
            if not engine.dialect.has_table(connection, table.name):
                table.create(engine)

# Exporta os objetos e funções para serem acessados por outros módulos
__all__ = ["Base", "engine", "SessionLocal", "init_db", "config", "update_db"]