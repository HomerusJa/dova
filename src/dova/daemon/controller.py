from pathlib import Path

import psutil

from dova.core.logging import get_logger

logger = get_logger(__name__)


def set_daemon_pid_to_file(repo_root: Path, pid: int) -> None:
    """Set the daemon PID to the PID file at .dova/daemon.pid."""
    pid_file_path = repo_root / ".dova" / "daemon.pid"
    pid_file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(pid_file_path, "w") as f:
        f.write(str(pid))
    logger.debug(f"Daemon PID {pid} written to {pid_file_path}")


def get_daemon_pid_from_file(repo_root: Path) -> int | None:
    """Get the daemon PID from the PID file at .dova/daemon.pid."""
    pid_file_path = repo_root / ".dova" / "daemon.pid"
    if not pid_file_path.exists():
        return None
    with open(pid_file_path, "r") as f:
        content = f.read()
        try:
            return int(content)
        except TypeError:
            logger.warning(f"Invalid PID file content {content!r}")
            return None


def is_daemon_running(repo_root: Path) -> bool:
    """Check if the daemon process is running."""
    pid = get_daemon_pid_from_file(repo_root)
    if pid is None:
        return False
    try:
        psutil.Process(pid)
        return True
    except psutil.NoSuchProcess:
        return False


def stop_daemon(repo_root: Path) -> None:
    """Stop the daemon process."""
    pid = get_daemon_pid_from_file(repo_root)
    if pid is None:
        logger.warning("Daemon process not found.")
    try:
        logger.info(f"Stopping daemon process with PID {pid}")
        process = psutil.Process(pid)
        process.kill()
    except psutil.NoSuchProcess:
        logger.warning("Daemon process not found.")
