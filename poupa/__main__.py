# -*- coding: utf-8 -*-
from poupa.controller.settings import CONFIG_FILE, DATABASE_FILE


def init() -> None:
    print(f"Initializing Poupa...")
    print(f"{CONFIG_FILE = }")
    print(f"{DATABASE_FILE = }")
    print("Poupa initialized successfully.")


if __name__ == "__main__":
    init()
    