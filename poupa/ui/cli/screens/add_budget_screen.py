# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from datetime import datetime

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

from poupa.controller.budget_controller import BudgetController


def add_new_budget() -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("NOVO ORÇAMENTO")
    budget_name: str = CLI.prompt("\nNome", type=str)
    start_date: str = CLI.prompt(
        "\nInício do orçamento (dd/mm/aaaa) ou <enter> para data atual",
        type=str,
        default=datetime.now().strftime("%d/%m/%Y"),
    )
    
    CLI.echo(f'\n{datetime.strptime(start_date, "%d/%m/%Y") = }\n')
    
    CLI.echo("\n\n        1. Salvar")
    CLI.echo("\n        9. Cancelar")
    choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "9"], default="1")
    
    if choice == 1:
        budget_controller = BudgetController()  # Instancia o controlador
        try:
            # Cria o orçamento usando o controlador, fornecendo um valor padrão para start_date
            new_budget = budget_controller.create_budget({
                "name": budget_name,
                "start_date": datetime.strptime(start_date, "%d/%m/%Y"),
            })
            
            CLI.echo(f'\nOrçamento "{new_budget.name}" criado com sucesso!')
            CLI.pause("\nPressione Enter para continuar...")
        except Exception as e:
            CLI.echo(f"\nErro ao salvar o orçamento: {e}")
            CLI.pause("\nPressione Enter para continuar...")
        navigation.main()
    elif choice == 9:
        navigation.main()
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        navigation.add_new_budget()