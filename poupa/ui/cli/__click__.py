# -*- coding: utf-8 -*-
#
# Copyright (c) 2025, Poupa Simão
# All rights reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import click

class CLI:
    @staticmethod
    def clear():
        click.clear()
    
    @staticmethod
    def prompt(message, type=str, default=None):
        return click.prompt(message, type=type, default=default)

    @staticmethod
    def echo(message):
        click.echo(message)

    @staticmethod
    def pause(message):
        click.pause(message)
        
    @staticmethod
    def confirm(message):
        click.confirm(message)
        
    @staticmethod
    def print_table(headers, rows, prefix="", suffix=""):
        straight_lines = prefix + "".join(["-" * (len(header) + 2) for header in headers]) + suffix
        click.echo(straight_lines)
        click.echo("| " + " | ".join(headers) + " |")
        click.echo(straight_lines)
        for row in rows:
            click.echo("| " + " | ".join(row) + " |")
        click.echo(straight_lines)
        click.echo(f"{len(rows)} orçamento(s) encontrado(s)\n".rjust(len(straight_lines)+1))
        
    @staticmethod
    def print_title(title: str):
        """Imprime um título formatado com bordas."""
        width = 60  # Largura total da linha
        border = "+" + "=" * (width - 2) + "+"
        padded_title = f"| {title:^{width - 4}} |"
        click.echo(border)
        click.echo(padded_title)
        click.echo(border + "\n")
        
    @staticmethod
    def print_subtitle(title: str):
        """Imprime um título formatado com bordas."""
        width = 60  # Largura total da linha
        border = "+" + "-" * (width - 2) + "+"
        padded_title = f"| {title:^{width - 4}} |"
        click.echo(border)
        click.echo(padded_title)
        click.echo(border + "\n")