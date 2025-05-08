import logging
from dataclasses import dataclass

from dova.core.logging import get_logger


@dataclass
class ContextObject:
    verbose: bool = False
    logger: logging.Logger = get_logger("default")
