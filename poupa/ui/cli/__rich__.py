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
    def prompt(message, type=str, default=None, lines_before: int = 0, lines_after: int = 0):
        """Solicita uma entrada do usuário com suporte a espaçamento antes e depois."""
        for _ in range(lines_before):
            CLI.console.print("")
        try:
            if type == int:
                result = IntPrompt.ask(message, default=default)
            elif type == str:
                result = Prompt.ask(message, default=default)
            else:
                raise ValueError("Tipo não suportado. Use 'int' ou 'str'.")
        except ValueError:
            CLI.console.print("[bold red]Entrada inválida! Por favor, tente novamente.[/bold red]")
            return CLI.prompt(message, type=type, default=default)
        for _ in range(lines_after):
            CLI.console.print("")
        return result

    @staticmethod
    def echo(message: str, style: str = "white", lines_before: int = 0, lines_after: int = 0):
        """Exibe uma mensagem ao usuário com estilo opcional e pula linhas antes e/ou depois."""
        for _ in range(lines_before):
            CLI.console.print("")
        CLI.console.print(message, style=style)
        for _ in range(lines_after):
            CLI.console.print("")

    @staticmethod
    def skip_line(lines: int = 1):
        """Adiciona linhas em branco no console."""
        for _ in range(lines):
            CLI.console.print("")

    @staticmethod
    def pause(message: str = "Pressione Enter para continuar...", lines_before: int = 0, lines_after: int = 0):
        """Pausa a execução até o usuário pressionar Enter, com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        CLI.console.print(f"[bold yellow]{message}[/bold yellow]")
        input()
        for _ in range(lines_after):
            CLI.console.print("")

    @staticmethod
    def confirm(message: str, default=False, lines_before: int = 0, lines_after: int = 0):
        """Solicita uma confirmação do usuário (sim/não), com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        result = Confirm.ask(f"[bold cyan]{message}[/bold cyan]", default=default)
        for _ in range(lines_after):
            CLI.console.print("")
        return result

    @staticmethod
    def choice(message: str, choices=list, default=str or None, lines_before: int = 0, lines_after: int = 0):
        """Exibe uma mensagem ao usuário com opções de escolha, com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        choice = Prompt.ask(f"[bold white]{message}[/bold white]", choices=choices, default=default)
        for _ in range(lines_after):
            CLI.console.print("")
        return int(choice)

    @staticmethod
    def print_table(headers, rows, lines_before: int = 0, lines_after: int = 0):
        """Exibe uma tabela formatada, com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        table = Table(show_header=True, header_style="bold magenta")
        for header in headers:
            table.add_column(header, style="dim", justify="center")

        for row in rows:
            table.add_row(*row)

        CLI.console.print(table)
        for _ in range(lines_after):
            CLI.console.print("")

    @staticmethod
    def print_title(title: str, lines_before: int = 0, lines_after: int = 0):
        """Imprime um título formatado com bordas, utilizando exatamente 90 colunas, com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        panel = Panel(
            f"[bold white]{title:^89}[/bold white]",
            border_style="bold green",
            padding=(1, 2),
            width=90
        )
        CLI.console.print(panel)
        for _ in range(lines_after):
            CLI.console.print("")

    @staticmethod
    def print_subtitle(title: str, lines_before: int = 0, lines_after: int = 0):
        """Imprime um subtítulo formatado com bordas, com suporte a espaçamento."""
        for _ in range(lines_before):
            CLI.console.print("")
        panel = Panel(
            f"[bold cyan]{title:^89}[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
            width=90
        )
        CLI.console.print(panel)
        for _ in range(lines_after):
            CLI.console.print("")