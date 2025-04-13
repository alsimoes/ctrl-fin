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

# TODO : Refatorar para usar o AccountController
# TODO : Refatorar para usar o AccountValidator
from poupa.model.budget import Budget
from poupa.model.account import Account, AccountType
import poupa.model.database as db


def add_new_account(budget=Budget) -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("NOVA CONTA")

    account_name: str = CLI.prompt("\nNome", type=str)

    account_types = db.SessionLocal().query(AccountType).all()
    CLI.echo("\nTipos de conta disponíveis:")
    for account_type in account_types:
        CLI.echo(f"    {account_type.id}. {account_type.name}")
    choice: int = CLI.prompt("\nEscolha o tipo da conta", type=int)
    account_type = next((a for a in account_types if a.id == choice), None)
    if account_type:
        CLI.echo(f"\nTipo da conta: {account_type.name}")
    else:
        CLI.echo("\nTipo de conta não encontrado. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        add_new_account(budget)

    account_balance: float = CLI.prompt("\nSaldo atual", type=float, default=0.0)
    account_balance_date: datetime = CLI.prompt(
        "\nData do saldo (dd/mm/aaaa) ou <enter> para data atual",
        type=str,
        default=datetime.now().strftime("%d/%m/%Y"),
    )

    account_impact_budget: bool = CLI.confirm("\nA conta impacta o orçamento?", default=False)

    new_account: Account = Account(
        name=account_name,
        budget_id=budget.id,
        account_type=account_type,
        impact_budget=account_impact_budget,
        balance=account_balance,
        balance_date=datetime.strptime(account_balance_date, "%d/%m/%Y") if account_balance_date else None,
    )

    CLI.echo("\n1. Salvar")
    CLI.echo("9. Cancelar")
    
    # TODO : Refatorar para usar CLI.choice
    choice: int = CLI.prompt("\nEscolha uma opção", type=int)

    if choice == 1:
        session = db.SessionLocal()
        try:
            account_type = session.query(AccountType).filter_by(id=account_type.id).first()
            new_account.account_type = account_type
            session.add(new_account)
            session.commit()
            CLI.echo(f'\nConta "{new_account.name}" criada com sucesso!')
            CLI.pause("\nPressione Enter para continuar...")
        except Exception as e:
            session.rollback()
            CLI.echo(f"\nErro ao salvar conta: {e}")
            CLI.pause("\nPressione Enter para continuar...")
        finally:
            session.close()
        navigation.open_budget(budget)
    elif choice == 9:
        navigation.open_budget(budget)
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        navigation.open_budget(budget)