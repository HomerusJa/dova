import contextlib
import importlib.metadata
import typer

app = typer.Typer(help="🐾 Dova – A task-centric version control system")

# -- Self group (meta commands) --
self_group = typer.Typer(name="self", help="Commands for the management of Dova itself")

@self_group.command()
def version():
    """Get Dova's version"""
    version: str = "unknown"
    with contextlib.suppress(importlib.metadata.PackageNotFoundError):
        version = importlib.metadata.version(__name__)
    typer.echo(f"Version: {version}")

app.add_typer(self_group)


# -- Task group --
task_app = typer.Typer(name="task", help="Manage tasks")

@task_app.command("list")
def list_tasks():
    """List all tasks"""
    typer.echo("Listing tasks (placeholder)")

@task_app.command("create")
def create_task(title: str):
    """Create a new task"""
    typer.echo(f"Task created: {title} (placeholder)")

@task_app.command()
def begin(task_id: int):
    """Begin work on a task"""
    typer.echo(f"Beginning work on task {task_id} (placeholder)")

@task_app.command()
def switch(task_id: int):
    """Switch to working on a different task"""
    typer.echo(f"Switched to task {task_id} (placeholder)")

@task_app.command()
def status():
    """Show current task and change status"""
    typer.echo("Status: (placeholder)")

@task_app.command()
def save(message: str):
    """Save a checkpoint with a message"""
    typer.echo(f"Saved checkpoint: {message} (placeholder)")

@task_app.command()
def review():
    """Request feedback on current task"""
    typer.echo("Review requested (placeholder)")

@task_app.command()
def approve(task_id: int):
    """Approve changes for a task"""
    typer.echo(f"Approved task {task_id} (placeholder)")

@task_app.command()
def complete(task_id: int):
    """Mark task as complete"""
    typer.echo(f"Completed task {task_id} (placeholder)")

@task_app.command()
def history():
    """Show task history"""
    typer.echo("History: (placeholder)")

app.add_typer(task_app)


# -- Project-level commands --
@app.command()
def init():
    """Initialize a new Dova project"""
    typer.echo("Initializing Dova repository...")

@app.command()
def sync():
    """Trigger a manual sync"""
    typer.echo("Sync triggered (placeholder)")
