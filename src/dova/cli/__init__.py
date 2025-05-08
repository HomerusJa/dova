import logging
from pathlib import Path
from typing import TypedDict

import typer

from .self import self_app
from .task import task_app
from .daemon import daemon_app
from .project import init, sync

from dova.core.logging import setup_logging
from dova.core.repo import find_repo, RepoNotFoundException

app = typer.Typer(
    help="🐾 Dova – A task-centric version control system", no_args_is_help=True
)

app.add_typer(self_app)
app.add_typer(task_app)
app.add_typer(daemon_app)

app.command()(init)
app.command()(sync)


class ContextObject(TypedDict):
    verbose: bool
    logger: logging.Logger
    repo_path: Path | None


@app.callback()
def initialize(ctx: typer.Context, verbose: bool = False):
    ctx.ensure_object(ContextObject)
    ctx.obj["verbose"] = verbose
    setup_logging(logging.DEBUG if verbose else logging.INFO)
    cli_logger = logging.getLogger("dova.cli")
    ctx.obj["logger"] = cli_logger

    try:
        ctx.obj["repo_path"] = find_repo(Path.cwd())
    except RepoNotFoundException:
        ctx.obj["repo_path"] = None
        cli_logger.warning("No repository found in current directory")
