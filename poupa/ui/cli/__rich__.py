# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt

class CLI:
    console = Console()

    @staticmethod
    def clear():
        """Limpa a tela."""
        CLI.console.clear()

    @staticmethod
    def prompt(message, type=str, default=None):
        try:
            if type == int:
                return IntPrompt.ask(message, default=default)
            elif type == str:
                return Prompt.ask(message, default=default)
            else:
                raise ValueError("Tipo não suportado. Use 'int' ou 'str'.")
        except ValueError:
            CLI.console.print("[bold red]Entrada inválida! Por favor, tente novamente.[/bold red]")
            return CLI.prompt(message, type=type, default=default)
        
    @staticmethod
    def echo(message: str, style: str = "white"):
        """Exibe uma mensagem ao usuário com estilo opcional."""
        CLI.console.print(message, style=style)

    @staticmethod
    def pause(message: str = "Pressione Enter para continuar..."):
        """Pausa a execução até o usuário pressionar Enter."""
        CLI.console.print(f"[bold yellow]{message}[/bold yellow]")
        input()  # Aguarda o usuário pressionar Enter

    @staticmethod
    def confirm(message: int, default=False):
        """Solicita uma confirmação do usuário (sim/não)."""
        return Confirm.ask(f"[bold cyan]{message}[/bold cyan]", default=default)

    @staticmethod
    def choice(message: str, choices=list, default=str or None):
        """Exibe uma mensagem ao usuário com estilo opcional."""
        choice = Prompt.ask(f"[bold white]{message}[/bold white]", choices=choices , default=default)
        return int(choice)

    @staticmethod
    def print_table(headers, rows):
        """Exibe uma tabela formatada."""
        table = Table(show_header=True, header_style="bold magenta")
        for header in headers:
            table.add_column(header, style="dim", justify="center")

        for row in rows:
            table.add_row(*row)

        CLI.console.print(table)

    @staticmethod
    def print_title(title: str):
        """Imprime um título formatado com bordas, utilizando exatamente 90 colunas."""
        panel = Panel(
            f"[bold white]{title:^89}[/bold white]",
            border_style="bold green",
            padding=(1, 2),
            width=90
        )
        CLI.console.print(panel)

    @staticmethod
    def print_subtitle(title: str):
        """Imprime um subtítulo formatado com bordas."""
        panel = Panel(
            f"[bold cyan]{title:^89}[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
            width=90
        )
        CLI.console.print(panel)