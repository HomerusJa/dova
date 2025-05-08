import contextlib
import importlib.metadata

import typer

self_app = typer.Typer(
    name="self", help="Commands for the management of Dova itself", no_args_is_help=True
)


@self_app.command()
def version():
    """Get Dova's version"""
    version: str = "unknown"
    with contextlib.suppress(importlib.metadata.PackageNotFoundError):
        version = importlib.metadata.version(__name__)
    typer.echo(f"Version: {version}")
