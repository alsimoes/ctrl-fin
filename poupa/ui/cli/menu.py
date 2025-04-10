# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path
import click


def welcome() -> None:
    click.echo("\nBEM VINDO AO POUPA SIMÃO CLI!\n")
    click.echo("## MENU INICIAL ##\n")
    click.echo("1. Abrir último orçamento") # TODO Adicionar lõgica para abrir o último orçamento
    click.echo("2. Listar orçamentos")
    click.echo("3. Criar novo orçamento")
    click.echo("\n9. Exit")
    choice = click.prompt("\nPlease choose an option", type=int)
    click.clear()
    
    if choice == 1:
        click.echo("\nSELECIONADO: Item abrir último orçamento selecionado\n")
        welcome()
    elif choice == 2:
        click.echo("\nSELECIONADO: Item listar orçamentos selecionado.\n")
        welcome()
    elif choice == 3:
        click.echo("\nSELECIONADO: Item criar novo orçamento selecionado.\n")
        welcome()
    elif choice == 9:
        click.echo("\nExiting...")
        quit()
    else:
        click.echo("\nInvalid option. Please try again.")
        welcome()
        
        
def show_menu() -> None:
    click.clear()
    click.echo("\n## NOVO ORÇAMENTO ##\n")
    click.echo("\n9. Exit")
    choice = click.prompt("\nPlease choose an option", type=int)
    
    if choice == 1:
        click.echo("\nSELECIONADO: Item abrir último orçamento selecionado\n")
        show_menu()
    elif choice == 2:
        click.echo("\nSELECIONADO: Item listar orçamentos selecionado.\n")
        show_menu()
    elif choice == 3:
        click.echo("\nSELECIONADO: Item criar novo orçamento selecionado.\n")
        show_menu()
    elif choice == 9:
        click.echo("\nExiting...")
        quit()
    else:
        click.echo("\nInvalid option. Please try again.")
        show_menu()