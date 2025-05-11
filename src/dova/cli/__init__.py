import typer

from ._initialize import ContextObject
from .daemon import daemon_app
from .project import init, sync
from .self import self_app
from .task import task_app

app = typer.Typer(
    help="🐾 Dova - A task-centric version control system",
    no_args_is_help=True,
    callback=ContextObject.callback,
)

app.add_typer(self_app)
app.add_typer(task_app)
app.add_typer(daemon_app)

app.command()(init)
app.command()(sync)
