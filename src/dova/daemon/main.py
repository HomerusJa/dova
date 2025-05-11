import logging
from pathlib import Path

from dova.daemon.communication import daemon_connection


def run_daemon(repo_root: Path, logger: logging.Logger):
    logger.info("Starting dummy daemon")
    with daemon_connection(repo_root) as sock:
        sock.listen()
        conn, _ = sock.accept()
        with conn:
            data = conn.recv(1024)
            logger.info(f"Received: {data!r}")
            conn.sendall(b"Hello from daemon")
