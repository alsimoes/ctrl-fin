# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

def main() -> None:
    try:
        navigation.show_main_menu()
    except KeyboardInterrupt:
        navigation.close_application()
    except EOFError:
        CLI.pause("EOFError: Unexpected end of input. Exiting application.", lines_before=1, lines_after=1)
    except Exception as e:
        CLI.pause(f"Unexpected error:\n{e}\nExiting application.", lines_before=1, lines_after=1)