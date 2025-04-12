# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from datetime import datetime
from pathlib import Path
import click
from poupa.model.account import Account, AccountType
from poupa.model.budget import Budget
import poupa.model.database as db

def main() -> None:
    click.clear()
    click.echo("\nBEM VINDO AO POUPA SIMÃO CLI!\n")
    click.echo("## MENU INICIAL ##\n")
    click.echo("1. Abrir último orçamento")
    click.echo("2. Listar orçamentos")
    click.echo("3. Atualizar banco de dados")
    click.echo("\n9. Sair")
    choice: int = click.prompt("\nEscolha uma opção", type=int)

    
    if choice == 1:
        click.echo("\nSELECIONADO: Item abrir último orçamento selecionado\n")
        click.pause("Pressione Enter para continuar...")
        main()
        # TODO Adicionar lógica para abrir o último orçamento
    elif choice == 2:
        list_budgets()
    elif choice == 3:
        db.update_db()
        click.echo("\nBanco de dados atualizado com sucesso!")
        click.pause("\nPressione Enter para continuar...")
        main()
    elif choice == 9:
        click.echo("\nExiting...")
        click.echo("\nAté logo!\n")
        quit()
    else:
        click.echo("\nInvalid option. Please try again.")
        click.pause("Pressione Enter para continuar...")
        main()
        
        
def add_new_budget() -> None:
    click.clear()
    click.echo("\n## NOVO ORÇAMENTO ##\n")
    budget_name: str = click.prompt("\nNome", type=str)
    click.echo("\n\n1. Salvar")
    click.echo("\n9. Cancelar")
    choice: int = click.prompt("\nEscolha uma opção", type=int)
    
    if choice == 1:
        new_budget: Budget = Budget(name=budget_name)
        session = db.SessionLocal()
        try:
            session.add(new_budget)
            session.commit()
            click.echo(f'\nOrçamento "{new_budget.name}" criado com sucesso!')
            click.pause("\nPressione Enter para continuar...")
        except Exception as e:
            session.rollback()
            click.echo(f"\nErro ao salvar o orçamento: {e}")
            click.pause("\nPressione Enter para continuar...")
        finally:
            session.close()
        main()
    elif choice == 9:
        main()
    else:
        click.echo("\nOpção inválida. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        new_budget()
        
        
def list_budgets() -> None:
    click.clear()
    click.echo("\n## ORÇAMENTOS ##\n")
    
    list_budgets: list = db.SessionLocal().query(Budget).all()
    
    if not list_budgets:
        click.echo("\nNenhum orçamento encontrado.\n")
        click.echo("\n1. Adicionar orçamento\n")
        click.echo("9. Voltar ao menu anterior\n")
        choice: int = click.prompt("\nEscolha uma opção", type=int)
        if choice == 1:
            add_new_budget()
        elif choice == 9:
            main()
    
    click.echo(f"{len(list_budgets)} orçamento(s) encontrado(s).")
    
    straight_lines = "+---------+------------------------------+--------------------+--------------------+"
    
    click.echo(straight_lines)
    click.echo(f"| SELECAO | ORÇAMENTO                    | DATA DE INÍCIO     | ÚLTIMA ATUALIZAÇÃO |")
    click.echo(straight_lines)
    
    for budget in list_budgets:
        start_date: datetime = budget.start_date.strftime("%d/%m/%Y") if budget.start_date else "N/A"
        update_date: datetime  = budget.update_date.strftime("%d/%m/%Y") if budget.update_date else "N/A"
        click.echo(f"| {budget.id:^7} | {budget.name:<28} | {start_date:>18} | {update_date:>18} |")
    
    click.echo(straight_lines)
    
    click.echo(f"\n8. Adicionar novo orçamento")
    click.echo(f"9. Menu anterior")
    
    choice: int = click.prompt("\nEscolha um orçamento ou voltar ao menu anterior", type=int)
    
    if choice <= len(list_budgets):
        budget: Budget = next((b for b in list_budgets if b.id == choice), None)
        
        if budget:
            open_budget(budget)
        else:
            click.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            click.pause("Pressione Enter para continuar...")
            list_budgets()
    
    elif choice == 8:
        add_new_budget()
            
    elif choice == 9:
        main()
        
    else:
        click.echo("\nOpção inválida. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        list_budgets()

        
def open_budget(budget=Budget) -> None:
    click.clear()
    click.echo(f"\n## ORÇAMENTO: {budget.name} ##\n")
    
    list_accounts: list = db.SessionLocal().query(Account).filter_by(budget_id=budget.id).all()
    if not list_accounts:
        click.echo("\nNenhuma conta encontrada.\n")
        click.echo("\n1. Adicionar nova conta")
        click.echo("9. Menu anterior\n")
        choice: int = click.prompt("Escolha uma opção", type=int)
        if choice == 1:
            add_new_account(budget)
        elif choice == 9:
            list_budgets()
            
    click.echo(f"{len(list_accounts)} conta(s) encontrada(s).")
     
    straight_lines = "+---------+--------------------+--------------------+---------------+---------------+"
    
    click.echo(straight_lines)
    click.echo(f"| SELECAO | CONTA              | TIPO               | SALDO         | ATUALIZADA EM |")
    click.echo(straight_lines)
    
    for account  in list_accounts:
        id = account.id
        name = account.name
        account_type = db.SessionLocal().query(AccountType).filter_by(id=account.account_type_id).first().name if account.account_type_id else None
        balance = account.balance if account.balance else '-'
        update_date = account.update_date.strftime("%d/%m/%Y") if account.update_date else None
        click.echo(f"| {id:^7} | {name:<18} | {account_type:<18} | {balance:>13} | {update_date:>13} |")
    
    click.echo(straight_lines)
    
    click.echo(f"\n\n9. Menu anterior")
    choice: int = click.prompt("\nEscolha um orçamento ou a opção voltar", type=int)
    
    if choice <= len(list_accounts):
        account: Account = next((b for b in list_accounts if b.id == choice), None)
        if account:
            open_account(budget, account)
        else:
            click.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            click.pause("Pressione Enter para continuar...")
            list_budgets()
    elif choice == 9:
        list_budgets()
    else:
        click.echo("\nOpção inválida. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        open_budget()
    pass


def add_new_account(budget=Budget) -> None:
    click.clear()
    click.echo("\n## NOVA CONTA ##\n")

    account_name: str = click.prompt("\nNome", type=str)
    
    account_types = db.SessionLocal().query(AccountType).all()
    click.echo("\nTipos de conta disponíveis:")
    for account_type in account_types:
        click.echo(f"    {account_type.id}. {account_type.name}")
    choice: int = click.prompt("\nEscolha o tipo da conta", type=int)
    account_type = next((a for a in account_types if a.id == choice), None)
    if account_type:
        click.echo(f"\nTipo da conta: {account_type.name}")
    else:
        click.echo("\nTipo de conta não encontrado. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        add_new_account(budget)
        
    account_balance: float = click.prompt("\nSaldo atual", type=float, default=0.0)
    account_balance_date: datetime = click.prompt("\nData do saldo (dd/mm/aaaa) ou <enter> para data atual", type=str, default=datetime.now().strftime("%d/%m/%Y")) 
    
    account_impact_budget: bool = click.confirm("\nA conta impacta o orçamento?", default=False)
    
    new_account: Account = Account(
            name=account_name,
            budget_id=budget.id,
            account_type=account_type,
            impact_budget=account_impact_budget,
            balance=account_balance,
            balance_date=datetime.strptime(account_balance_date, "%d/%m/%Y") if account_balance_date else None
        )
    
    print(f"----\n{new_account = }\n----")
    
    click.echo("\n1. Salvar")
    click.echo("9. Cancelar")
    choice: int = click.prompt("\nEscolha uma opção", type=int)
    
    if choice == 1:        
        session = db.SessionLocal()
        try:
            # Recarrega o objeto account_type na mesma sessão
            account_type = session.query(AccountType).filter_by(id=account_type.id).first()
            new_account.account_type = account_type  # Associa o objeto recarregado
            session.add(new_account)
            session.commit()
            click.echo(f'\nConta "{new_account.name}" criada com sucesso!')
            click.pause("\nPressione Enter para continuar...")
        except Exception as e:
            session.rollback()
            click.echo(f"\nErro ao salvar conta: {e}")
            click.pause("\nPressione Enter para continuar...")
        finally:
            session.close()
        open_budget(budget)
    elif choice == 9:
        open_budget(budget)
    else:
        click.echo("\nOpção inválida. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        open_budget(budget)
        
        
def open_account(budget=Budget, account=Account) -> None:
    click.clear()
    click.echo(f"\n## CONTA: {account.name} ##\n")
    
    click.echo("9. Voltar ao orçamento\n")
    
    choice: int = click.prompt("\nEscolha uma opção", type=int)
    
    if choice == 9:
        open_budget(budget)