import platform
import socket
from contextlib import contextmanager
from pathlib import Path

from dova.core.errors import DovaException
from dova.core.logging import get_logger
from dova.core.repo import is_repo

logger = get_logger(__name__)


class DeamonConnectionError(DovaException):
    """Raised when there is an error communicating with the Dova daemon."""


def get_free_port() -> int:
    """Get a free port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


@contextmanager
def daemon_connection(repo_root: Path):
    """Context manager for setting up the IPC socket."""
    if not is_repo(repo_root):
        raise DeamonConnectionError(
            f"Repository at {repo_root} is not a Dova repository."
        )

    if platform.system() == "Windows":
        port_file = repo_root / ".dova" / "ipc.port"
        if port_file.exists():
            with open(port_file, "r") as f:
                port = int(f.read())
        else:
            port = get_free_port()
            with open(port_file, "w") as f:
                f.write(str(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("localhost", port))
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        if not hasattr(socket, "AF_UNIX"):
            raise RuntimeError("Unix domain sockets not supported on this platform.")
        sock_path = repo_root / ".dova" / "ipc.sock"
        # We can ignore safely here as the platform is guaranteed to provide this.
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)  # type: ignore[attr-defined]
        sock.bind(str(sock_path))
    else:
        raise RuntimeError("Unsupported operating system.")

    try:
        yield sock
    finally:
        sock.close()
