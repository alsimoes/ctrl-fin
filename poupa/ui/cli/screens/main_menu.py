# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

def show_main_menu() -> None:
    """Exibe o menu principal."""
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI", lines_after=1)
    CLI.print_subtitle("MENU INICIAL", lines_after=1)
    CLI.echo("        1. Abrir último orçamento", lines_before=1)
    CLI.echo("        2. Listar orçamentos")
    CLI.echo("        9. Sair", lines_after=1)
    choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "2", "9"], default="1")

    if choice == 1:
        CLI.echo("SELECIONADO: Item abrir último orçamento selecionado.", lines_before=1, lines_after=1)
        CLI.pause("Pressione Enter para continuar...")
        show_main_menu()
    elif choice == 2:
        navigation.list_budgets()
    elif choice == 9:
        navigation.close_application()
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        show_main_menu()