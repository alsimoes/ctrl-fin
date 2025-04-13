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
    CLI.print_title("POUPA SIMÃO CLI", lines_after=1)
    CLI.print_subtitle("NOVA CONTA", lines_after=1)

    account_name: str = CLI.prompt("\nNome", type=str)

    with db.SessionLocal() as session:
        account_types = db.SessionLocal().query(AccountType).all()
    
    CLI.echo("Tipos de conta disponíveis:", lines_before=1, lines_after=1)
        
    for account_type in account_types:
        CLI.echo(f"        {account_type.id}. {account_type.name}")
    
    choices = [(str(a.id)) for a in account_types]
    
    choice: int = CLI.choice("Escolha o tipo da conta", choices=choices, lines_before=1)
    
    account_type = next((a for a in account_types if a.id == choice), None)
    
    if account_type:
        CLI.echo(f"Tipo da conta: {account_type.name}", lines_before=1)
    else:
        CLI.echo("Tipo de conta não encontrado. Por favor, tente novamente.", lines_before=1, lines_after=1)
        CLI.pause("Pressione Enter para continuar...")
        add_new_account(budget)
    
    account_balance: float = CLI.prompt("Saldo atual", type=float, default=0.0, lines_before=1)
    account_balance_date: datetime = CLI.prompt(
        "Data do saldo (dd/mm/aaaa) ou <enter> para data atual",
        type=str,
        default=datetime.now().strftime("%d/%m/%Y"),
        lines_before=1
    )

    account_impact_budget: bool = CLI.confirm("A conta impacta o orçamento?", default=False, lines_before=1, lines_after=2)

    new_account: Account = Account(
        name=account_name,
        budget_id=budget.id,
        account_type=account_type,
        impact_budget=account_impact_budget,
        balance=account_balance,
        balance_date=datetime.strptime(account_balance_date, "%d/%m/%Y") if account_balance_date else None,
    )
       
    choices = {1: "Salvar", 9: "Cancelar"}
    
    for key, value in choices.items():
        CLI.echo(f"{key}. {value}")
    
    choice:str = CLI.prompt("Escolha uma opção", type=str, choices=choices.keys(), lines_before=1)
    if choice not in choices:
        CLI.echo("Opção inválida. Por favor, tente novamente.", lines_before=1, lines_after=1)
        CLI.pause("Pressione Enter para continuar...")
        add_new_account(budget)
    
    if choice == 1:
        session = db.SessionLocal()
        try:
            account_type = session.query(AccountType).filter_by(id=account_type.id).first()
            new_account.account_type = account_type
            session.add(new_account)
            session.commit()
            CLI.echo(f'Conta "{new_account.name}" criada com sucesso!', lines_before=1, lines_after=1)
            CLI.pause("Pressione Enter para continuar...")
        except Exception as e:
            session.rollback()
            CLI.echo(f"Erro ao salvar conta: {e}", lines_before=1, lines_after=1)
            CLI.pause("Pressione Enter para continuar...")
        finally:
            session.close()
        navigation.open_budget(budget)
    elif choice == 9:
        navigation.open_budget(budget)
    else:
        CLI.echo("Opção inválida. Por favor, tente novamente.", lines_before=1, lines_after=1)
        CLI.pause("Pressione Enter para continuar...")
        navigation.open_budget(budget)