from pathlib import Path
from typing import Annotated

import typer

from dova.core.repo import find_repo, init_repo

from ._context import ContextObject


def init(
    ctx: typer.Context,
    path: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            writable=True,
            resolve_path=True,
            help="Path to initialize Dova project in (default: current working directory)",
        ),
    ] = Path.cwd(),
):
    """Initialize a new Dova project"""
    ctx.obj.ensure_object(ContextObject)
    if find_repo(path) is not None:
        ctx.obj.logger.warning(f"Repository already exists at {path}")
        return
    init_repo(path)


def sync():
    """Trigger a manual sync"""
    typer.echo("Sync triggered (placeholder)")
