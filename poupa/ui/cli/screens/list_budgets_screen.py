# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

from poupa.controller.budget_controller import BudgetController  # Importa o controlador

def list_budgets() -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("ORÇAMENTOS")

    # Obtém a lista de orçamentos do BudgetController
    budgets = BudgetController().get_all_budgets()

    if not budgets:
        CLI.echo("\nNenhum orçamento encontrado.\n")
        CLI.echo("\n        1. Adicionar orçamento\n")
        CLI.echo("        9. Voltar ao menu anterior\n")
        
        choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "9"], default="1")
        
        if choice == 1:
            navigation.add_new_budget()
        elif choice == 9:
            navigation.main()

    headers = [
        f"{'SELECAO':^7}", 
        f"{'ORÇAMENTO':^30}", 
        f"{'DATA DE INÍCIO':^18}", 
        f"{'ÚLTIMA ATUALIZAÇÃO':^18}"]
    rows = [
        [
            f"{budget.id:^7}",
            f"{budget.name:<28}",
            f"{budget.start_date.strftime('%d/%m/%Y') if budget.start_date else 'N/A':>18}",
            f"{budget.update_date.strftime('%d/%m/%Y') if budget.update_date else 'N/A':>18}",
        ]
        for budget in budgets
    ]
    CLI.print_table(headers, rows)
    
    CLI.echo(f"\n        8. Adicionar novo orçamento")
    CLI.echo(f"        9. Menu anterior")
    
    choices = [str(b.id) for b in budgets] + ["8", "9"] 
    choice: int = CLI.choice("\nEscolha um orçamento ou uma das opções do menu", choices=choices, default="1")

    if choice <= len(budgets):
        budget = next((b for b in budgets if b.id == choice), None)

        if budget:
            navigation.open_budget(budget)
        else:
            CLI.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            CLI.pause("Pressione Enter para continuar...")
            list_budgets()

    elif choice == 8:
        navigation.add_new_budget()

    elif choice == 9:
        navigation.main()

    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        navigation.list_budgets()