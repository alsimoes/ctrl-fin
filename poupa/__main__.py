# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.controller.settings import DATABASE_FILE
from poupa.ui.cli import main as cli
import poupa.model.database as db

def init() -> None:
    db.config(DATABASE_FILE)
    cli.main()

if __name__ == "__main__":
    init()
    
    