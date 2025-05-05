import logging
from rich.logging import RichHandler


def setup_logging(
    level: int = logging.INFO,
    log_to_file: bool = False,
    file_path: str = "dova.log",
    rich_tracebacks: bool = True,
) -> None:
    """Set up logging for the Dova application.

    Args:
        level (int): Logging level (e.g., logging.DEBUG).
        log_to_file (bool): Whether to also log to a file.
        file_path (str): File path for the log file.
        rich_tracebacks (bool): Whether to use rich tracebacks in logs.
    """
    handlers = [RichHandler(rich_tracebacks=rich_tracebacks, show_path=False)]

    if log_to_file:
        file_handler = logging.FileHandler(file_path)
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
