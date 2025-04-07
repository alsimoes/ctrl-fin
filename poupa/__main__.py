# -*- coding: utf-8 -*-
from poupa.model.database import init_db

def init() -> None:
    print("Iniciando Poupa Simão!")
    init_db()

if __name__ == "__main__":
    init()