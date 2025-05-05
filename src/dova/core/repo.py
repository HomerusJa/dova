from pathlib import Path

from .errors import DovaException
from .logging import get_logger


_logger = get_logger(__name__)


class RepoNotFoundException(DovaException):
    """Raised when a Dova repository could not be found."""


def init_repo(path: Path) -> None:
    """Initialize a new Dova repository at the given path."""
    (path / ".dova").mkdir(exist_ok=True)


def _is_drive_root(path: Path) -> bool:
    """Return True if the path is the root of the filesystem (e.g., '/' or 'C:\\')."""
    return path == path.parent


def find_repo(
    start_path: Path, max_iterations: int = 100, marker_dir: str = ".dova"
) -> Path:
    """Search upwards from start_path for a repository marked by a specific directory.

    Raises:
        RepoNotFoundException: If no repository is found.
    """
    path = start_path.resolve()
    for i in range(max_iterations):
        if (path / marker_dir).is_dir():
            _logger.debug(f"Found repository at {path}")
            return path
        if _is_drive_root(path):
            break
        path = path.parent

    _logger.warning(
        f"Repository marker '{marker_dir}' not found after {i + 1} iterations"
    )
    raise RepoNotFoundException(
        f"No repository found in parent directories of {start_path}"
    )
