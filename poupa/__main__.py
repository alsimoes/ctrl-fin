# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.controller.settings import CONFIG_FILE, DATABASE_FILE
from poupa.ui.cli import menu


def init() -> None:
    print(f"Initializing Poupa...")
    print(f"{CONFIG_FILE = }")
    print(f"{DATABASE_FILE = }")
    print("Poupa initialized successfully.")
    menu.welcome()

if __name__ == "__main__":
    init()
    
    