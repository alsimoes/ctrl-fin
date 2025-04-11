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
from poupa.model.budget import Budget
import poupa.model.database as db

def main() -> None:
    click.clear()
    click.echo("\nBEM VINDO AO POUPA SIMÃO CLI!\n")
    click.echo("## MENU INICIAL ##\n")
    click.echo("1. Abrir último orçamento")
    click.echo("2. Listar orçamentos")
    click.echo("3. Criar novo orçamento")
    click.echo("4. Atualizar banco de dados")
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
        add_new_budget()
    elif choice == 4:
        db.update_db()
        click.echo("\nBanco de dados atualizado com sucesso!")
        click.pause("\nPressione Enter para continuar...")
        main()
    elif choice == 9:
        click.echo("\nExiting...")
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
    click.echo("\n2. Cancelar")
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
    elif choice == 2:
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
        click.pause("Pressione Enter para continuar..")
        main()
    click.echo(f"{len(list_budgets)} orçamento(s) encontrado(s).")
    click.echo(f"+---------+------------------------------+--------------------+--------------------+")
    click.echo(f"| SELECAO | ORÇAMENTO                    | DATA DE INÍCIO     | ÚLTIMA ATUALIZAÇÃO |")
    click.echo(f"+---------+------------------------------+--------------------+--------------------+")
    for budget in list_budgets:
        start_date: datetime = budget.start_date.strftime("%d/%m/%Y") if budget.start_date else "N/A"
        update_date: datetime  = budget.update_date.strftime("%d/%m/%Y") if budget.update_date else "N/A"
        click.echo(f"| {budget.id:<7} | {budget.name:<28} | {start_date:<18} | {update_date:<18} |")
    click.echo(f"+---------+------------------------------+--------------------+--------------------+")
    click.echo(f"\n\n{len(list_budgets)+1}. Voltar ao menu inicial")
    choice: int = click.prompt("\nEscolha um orçamento ou a opção voltar", type=int)
    
    if choice <= len(list_budgets):
        budget: Budget = next((b for b in list_budgets if b.id == choice), None)
        if budget:
            click.pause(f"\nO número selecionado foi [{choice}], orçamento [{budget.name}].")
            open_budget(budget)
        else:
            click.echo("\nOrçamento não encontrado. Por favor, tente novamente.")
            click.pause("Pressione Enter para continuar...")
            list_budgets()
    elif choice == (len(list_budgets)+1):
        main()
    else:
        click.echo("\nOpção inválida. Por favor, tente novamente.")
        click.pause("Pressione Enter para continuar...")
        list_budgets()
        
def open_budget(budget=Budget) -> None:
    #TODO Implementar lógica para listar orçamentos
    pass
