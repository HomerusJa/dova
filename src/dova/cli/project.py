from pathlib import Path
from typing import Annotated

import typer

from dova.core.repo import init_repo


def init(
    ctx: typer.Context,
    path: Annotated[
        Path,
        typer.Argument(
            default=Path.cwd(),
            exists=True,
            file_okay=False,
            writable=True,
            resolve_path=True,
            help="Path to initialize Dova project in (default: current working directory)",
        ),
    ],
):
    """Initialize a new Dova project"""
    init_repo(path)


def sync():
    """Trigger a manual sync"""
    typer.echo("Sync triggered (placeholder)")
