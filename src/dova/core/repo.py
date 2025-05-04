from pathlib import Path

from .errors import RepoNotFoundException


def init_repo(path: Path) -> None:
    """Initialize a new Dova repository at the given path."""
    (path / ".dova").mkdir(exist_ok=True)


def _is_drive_root(path: Path) -> bool:
    """Return True if the path is the root of the filesystem (e.g., '/' or 'C:\\')."""
    return path == path.parent


def find_repo(start_path: Path) -> Path:
    """Search upwards from start_path for a Dova repository and return its root path.

    Raises:
        RepoNotFoundException: If no repository is found.
    """
    path = start_path.resolve()
    while True:
        if (path / ".dova").is_dir():
            return path
        if _is_drive_root(path):
            break
        path = path.parent
    raise RepoNotFoundException(
        f"No repository found in parent directories of {start_path}"
    )
