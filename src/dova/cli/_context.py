import logging
from dataclasses import dataclass, field

from dova.core.logging import get_logger


@dataclass
class ContextObject:
    verbose: bool = False
    logger: logging.Logger = field(default_factory=lambda: get_logger("dova.cli"))
