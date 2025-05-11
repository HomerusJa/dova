from typing import Annotated, cast

import psutil
import typer

from dova.daemon.controller import (
    get_daemon_pid_from_file,
    is_daemon_running,
    set_daemon_pid_to_file,
    stop_daemon,
)
from dova.daemon.main import run_daemon

from ._initialize import ContextObjectWithRepoPath

daemon_app = typer.Typer(
    name="daemon",
    help=(
        "Manage the Dova background sync service that keeps your tasks in sync with "
        "the cloud"
    ),
    no_args_is_help=True,
    callback=ContextObjectWithRepoPath.callback,
)


@daemon_app.command()
def start(
    ctx: typer.Context,
    blocking: Annotated[
        bool,
        typer.Option(
            help=(
                "Run the daemon in the current process instead of background. "
                "Useful for debugging and seeing log output directly."
            )
        ),
    ] = False,
    force: Annotated[
        bool,
        typer.Option(
            help=(
                "Force start a new daemon instance even if one is already running. "
                "Warning: This may cause sync conflicts."
            )
        ),
    ] = False,
    with_shell: Annotated[
        bool,
        typer.Option(
            help=(
                "Open the daemon in a new terminal window to monitor its output. "
                "Only works in non-blocking mode."
            ),
        ),
    ] = False,
):
    """Start the Dova sync daemon.

    The daemon runs in the background and ensures your tasks and checkpoints
    are synchronized with the cloud in real-time.
    """
    ctx.obj = cast(ContextObjectWithRepoPath, ctx.obj)

    if not force and is_daemon_running(ctx.obj.repo_path):
        ctx.obj.logger.warning("Daemon is already running. Use --force to override.")
        return

    if with_shell and blocking:
        ctx.obj.logger.warning(
            "Cannot use --with-shell in non-blocking mode. Ignoring."
        )

    if blocking:
        run_daemon(ctx.obj.repo_path, ctx.obj.logger)
    else:
        # Run this command with the blocking flag in another Process
        cmd = [
            "dova",
            *(["--verbose"] if ctx.obj.verbose else []),
            f"--log-file={ctx.obj.repo_path / '.dova' / 'daemon.log'}",
            "daemon",
            "start",
            "--blocking",
            "--force",
        ]
        ctx.obj.logger.debug(f"Running command: {' '.join(cmd)}")
        process = psutil.Popen(
            cmd if not with_shell else " ".join(cmd),
            shell=with_shell,
            # When not using shell, we need to pass list of args
            # When using shell, we need to pass a string
        )
        set_daemon_pid_to_file(ctx.obj.repo_path, process.pid)


@daemon_app.command()
def stop(ctx: typer.Context):
    """Stop the Dova sync daemon.

    Safely stops the background sync process. Your local changes will be
    synchronized when you start the daemon again.
    """
    stop_daemon(ctx.obj.repo_path)


@daemon_app.command()
def status(ctx: typer.Context):
    """Check the Dova sync daemon status.

    Shows whether the daemon is running and its process ID.
    Use this to verify if background sync is active.
    """
    if is_daemon_running(ctx.obj.repo_path):
        pid = get_daemon_pid_from_file(ctx.obj.repo_path)
        typer.echo(f"Daemon is running with PID {pid}")
        return
    else:
        typer.echo("Daemon is not running")
