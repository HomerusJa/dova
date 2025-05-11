from pathlib import Path
from typing import Annotated

import typer

from dova.core.repo import find_repo, init_repo


def init(
    ctx: typer.Context,
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            writable=True,
            help="Path to initialize Dova project in (default: cwd)",
        ),
    ] = Path("."),
):
    """Initialize a new Dova project"""
    path = path.resolve()
    if find_repo(path) is not None:
        ctx.obj.logger.warning(f"Repository already exists at {path}")
        return
    init_repo(path)
    ctx.obj.logger.info(f"Dova project initialized at {path}")


def sync():
    """Trigger a manual sync"""
    typer.echo("Sync triggered (placeholder)")
