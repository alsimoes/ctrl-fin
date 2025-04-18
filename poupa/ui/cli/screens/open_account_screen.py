# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

from poupa.model.budget import Budget
from poupa.model.account import Account



def open_account(budget=Budget, account=Account) -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle(f"CONTA: {account.name}")

    # TODO : Implementar a exibição dos detalhes da conta
    
    CLI.echo("        9. Voltar ao orçamento\n")

    # TODO : Refatorar para usar CLI.choice
    choice: int = CLI.prompt("\nEscolha uma opção", type=int)

    if choice == 9:
        navigation.open_budget(budget)