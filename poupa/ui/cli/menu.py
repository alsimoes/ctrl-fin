# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from datetime import datetime
from poupa.model.account import Account, AccountType
from poupa.model.budget import Budget
import poupa.model.database as db
from poupa.ui.cli.__rich__ import CLI


def main() -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("MENU INICIAL")
    CLI.echo("\n        1. Abrir último orçamento")
    CLI.echo("        2. Listar orçamentos")
    # CLI.echo("    3. Atualizar banco de dados")
    CLI.echo("\n        9. Sair")
    choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "2", "3", "9"], default="1")

    if choice == 1:
        CLI.echo("\nSELECIONADO: Item abrir último orçamento selecionado\n")
        CLI.pause("Pressione Enter para continuar...")
        main()
    elif choice == 2:
        list_budgets()
    elif choice == 3:
        db.update_db()
        CLI.echo("\nBanco de dados atualizado com sucesso!")
        CLI.pause("\nPressione Enter para continuar...")
        main()
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


def list_budgets() -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle("ORÇAMENTOS")

    list_budgets: list = db.SessionLocal().query(Budget).all()

    if not list_budgets:
        CLI.echo("\nNenhum orçamento encontrado.\n")
        CLI.echo("\n        1. Adicionar orçamento\n")
        CLI.echo("        9. Voltar ao menu anterior\n")
        choice: int = CLI.choice("\nEscolha uma opção", choices=["1", "9"], default="1")
        
        if choice == 1:
            add_new_budget()
        elif choice == 9:
            main()

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
        for budget in list_budgets
    ]
    CLI.print_table(headers, rows)
    
    CLI.echo(f"\n        8. Adicionar novo orçamento")
    CLI.echo(f"        9. Menu anterior")
    
    choices = [str(b.id) for b in list_budgets] + ["8", "9"] 
    choice: int = CLI.choice("\nEscolha um orçamento ou uma das opções do menu", choices=choices, default="1")

    if choice <= len(list_budgets):
        budget: Budget = next((b for b in list_budgets if b.id == choice), None)

        if budget:
            open_budget(budget)
        else:
            CLI.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            CLI.pause("Pressione Enter para continuar...")
            list_budgets()

    elif choice == 8:
        add_new_budget()

    elif choice == 9:
        main()

    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        list_budgets()


def open_budget(budget=Budget) -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle(f"ORÇAMENTO: {budget.name}")

    list_accounts: list = db.SessionLocal().query(Account).filter_by(budget_id=budget.id).all()
    if not list_accounts:
        CLI.echo("\nNenhuma conta encontrada.\n")
        CLI.echo("\n1. Adicionar nova conta")
        CLI.echo("9. Menu anterior\n")
        choice: int = CLI.prompt("Escolha uma opção", type=int)
        if choice == 1:
            add_new_account(budget)
        elif choice == 9:
            list_budgets()

    headers = [
        f"{'SELECAO':^7}", 
        f"{'CONTA':^18}", 
        f"{'TIPO':^18}", 
        f"{'SALDO':^13}", 
        f"{'ATUALIZADA EM':^13}"]
    rows = [
        [
            f"{account.id:^7}",
            f"{account.name:<18}",
            f"{db.SessionLocal().query(AccountType).filter_by(id=account.account_type_id).first().name if account.account_type_id else None:<18}",
            f"{account.balance if account.balance else '-':>13}",
            f"{account.update_date.strftime('%d/%m/%Y') if account.update_date else None:>13}",
        ]
        for account in list_accounts
    ]
    CLI.print_table(headers, rows)

    CLI.echo(f"\n\n        6. Adicionar nova conta")
    CLI.echo(f"        7. Editar conta")
    CLI.echo(f"        8. Excluir conta")
    CLI.echo(f"        9. Menu anterior")
    
    choices = [str(a.id) for a in list_accounts] + ["6", "7", "8", "9"] 
    choice: int = CLI.choice("\nEscolha um orçamento ou uma das opções do menu", choices=choices, default="1")

    if choice <= len(list_accounts):
        account: Account = next((b for b in list_accounts if b.id == choice), None)
        if account:
            open_account(budget, account)
        else:
            CLI.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            CLI.pause("Pressione Enter para continuar...")
            list_budgets()
    elif choice == 9:
        list_budgets()
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        open_budget()


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
        open_budget(budget)
    elif choice == 9:
        open_budget(budget)
    else:
        CLI.echo("\nOpção inválida. Por favor, tente novamente.")
        CLI.pause("Pressione Enter para continuar...")
        open_budget(budget)


def open_account(budget=Budget, account=Account) -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.print_subtitle(f"CONTA: {account.name}")

    CLI.echo("9. Voltar ao orçamento\n")

    choice: int = CLI.prompt("\nEscolha uma opção", type=int)

    if choice == 9:
        open_budget(budget)