import logging
from pathlib import Path

from rich.logging import RichHandler


def setup_logging(
    level: int = logging.INFO,
    file_path: Path | None = None,
    rich_tracebacks: bool = True,
) -> None:
    """Set up logging for the Dova application.

    Args:
        level: Logging level (e.g., logging.DEBUG).
        file_path: File path for the log file or None if no log file should be created.
        rich_tracebacks: Whether to use rich tracebacks in logs.
    """
    handlers: list[logging.Handler] = [
        RichHandler(rich_tracebacks=rich_tracebacks, show_path=False)
    ]

    if file_path is not None:
        file_handler = logging.FileHandler(file_path.resolve())
        file_formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        handlers.append(file_handler)

    logging.basicConfig(
        level=level,
        format="%(message)s",
        handlers=handlers,
        force=True,  # override any existing config
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger for the given name."""
    return logging.getLogger(name)
