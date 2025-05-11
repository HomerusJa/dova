from pathlib import Path

from .logging import get_logger

_logger = get_logger(__name__)


def init_repo(path: Path) -> None:
    """Initialize a new Dova repository at the given path."""
    (path / ".dova").mkdir(exist_ok=True)


def _is_drive_root(path: Path) -> bool:
    """Return True if the path is the root of the filesystem (e.g., '/' or 'C:\\')."""
    return path == path.parent


def is_repo(path: Path) -> bool:
    """Return True if the given path is a Dova repository."""
    return (path / ".dova").is_dir()


def find_repo(
    start_path: Path, max_iterations: int = 100, marker_dir: str = ".dova"
) -> Path | None:
    """Search upwards from start_path for a folder containing marker_dir."""
    path = start_path.resolve()
    for _ in range(max_iterations):
        if (path / marker_dir).is_dir():
            _logger.debug(f"Found repository at {path}")
            return path
        if _is_drive_root(path):
            break
        path = path.parent

    _logger.debug(
        f"Repository marker '{marker_dir}' not found after {max_iterations} iterations"
    )
    return None
