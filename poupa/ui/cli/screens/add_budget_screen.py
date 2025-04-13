# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli.navigation import main
from poupa.model.budget import Budget
import poupa.model.database as db


def add_new_budget() -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("NOVO ORÇAMENTO")
    budget_name: str = CLI.prompt("\nNome", type=str)
    CLI.echo("\n\n        1. Salvar")
    CLI.echo("\n        9. Cancelar")
    choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "9"], default="1")
    
    if choice == 1:
        new_budget: Budget = Budget(name=budget_name)
        session = db.SessionLocal()
        try:
            session.add(new_budget)
            session.commit()
            CLI.echo(f'\nOrçamento "{new_budget.name}" criado com sucesso!')
            CLI.pause("\nPressione Enter para continuar...")
        except Exception as e:
            session.rollback()
            CLI.echo(f"\nErro ao salvar o orçamento: {e}")
            CLI.pause("\nPressione Enter para continuar...")
        finally:
            session.close()
        main()
    elif choice == 9:
        main()
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        add_new_budget()