# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from poupa.ui.cli.__rich__ import CLI
from poupa.ui.cli import navigation

from poupa.controller.account_controller import AccountController, AccountTypeController


def open_budget(budget) -> None:
    CLI.clear()
    CLI.print_title("POUPA SIMÃO CLI")
    CLI.skip_line()
    CLI.print_subtitle(f"ORÇAMENTO: {budget.name}")

    account_controller = AccountController()
    account_type_controller = AccountTypeController()

    # Obtém as contas associadas ao orçamento
    list_accounts = account_controller.get_accounts_by_budget_id(budget.id)
    if not list_accounts:
        CLI.echo("Nenhuma conta encontrada.", lines_before=1, lines_after=1)
        CLI.echo("1. Adicionar nova conta", lines_before=1)
        CLI.echo("9. Menu anterior", lines_after=1)
        choice: int = CLI.prompt("Escolha uma opção", type=int)
        if choice == 1:
            navigation.add_new_account(budget)
        elif choice == 9:
            navigation.list_budgets()

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
            f"{account_type_controller.get_account_type_by_id(account.account_type_id).name if account.account_type_id else None:<18}",
            f"{account.balance if account.balance else '-':>13}",
            f"{account.update_date.strftime('%d/%m/%Y') if account.update_date else None:>13}",
        ]
        for account in list_accounts
    ]
    CLI.print_table(headers, rows)

    CLI.echo(f"        6. Adicionar nova conta", lines_before=2)
    CLI.echo(f"        7. Editar conta")
    CLI.echo(f"        8. Excluir conta")
    CLI.echo(f"        9. Menu anterior")
    
    choices = [str(a.id) for a in list_accounts] + ["6", "7", "8", "9"] 
    CLI.skip_line()
    choice: str = CLI.choice("Escolha um orçamento ou uma das opções do menu", choices=choices, default="1")

    if choice <= len(list_accounts):
        account = next((b for b in list_accounts if b.id == choice), None)
        if account:
            navigation.open_account(budget, account)
        else:
            CLI.echo("Conta não encontrada. Por favor, tente novamente.", lines_before=1, lines_after=1)
            CLI.pause("Pressione Enter para continuar...")
            navigation.list_budgets()
    elif choice == 6:
        navigation.add_new_account(budget)
    elif choice == 7:
        # TODO: Implement editing an account
        pass
    elif choice == 8:
        # TODO: Implement deleting an account
        pass
    elif choice == 9:
        navigation.list_budgets()
    else:
        CLI.echo("Opção inválida. Por favor, tente novamente.", lines_before=1, lines_after=1)
        CLI.pause("Pressione Enter para continuar...")
        navigation.open_budget()