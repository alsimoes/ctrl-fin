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
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("MENU INICIAL")
    CLI.echo("\n        1. Abrir último orçamento")
    CLI.echo("        2. Listar orçamentos")
    CLI.echo("\n        9. Sair")
    choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "2", "9"], default="1")

    if choice == 1:
        CLI.echo("\nSELECIONADO: Item abrir último orçamento selecionado\n")
        CLI.pause("Pressione Enter para continuar...")
        main()
    elif choice == 2:
        navigation.list_budgets()
    elif choice == 9:
        CLI.clear()
        CLI.print_title("POUPA SIMÃO CLI")
        CLI.echo("\n    Tchau! Tchau!")
        CLI.echo("\n    ...e até breve!\n\n")
        quit()
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        main()