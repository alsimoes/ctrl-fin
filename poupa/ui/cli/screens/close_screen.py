# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI

def close_application() -> None:
    """Exibe a tela de encerramento e finaliza o programa."""
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI", lines_after=1)
    CLI.echo("    Tchau! Tchau!", lines_before=1, lines_after=1)
    CLI.echo("    Obrigado por usar o Poupa Simão.", lines_before=1, lines_after=1)
    CLI.echo("    Esperamos que tenha gostado!", lines_before=1, lines_after=1)
    CLI.echo("    ...e até breve!", lines_before=1, lines_after=2)
    quit()