# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import click
from poupa.controller.settings import DATABASE_FILE
from poupa.ui.cli import menu
import poupa.model.database as db

def init() -> None:
    click.clear()
    db.config(DATABASE_FILE)
    menu.main()

if __name__ == "__main__":
    init()
    
    