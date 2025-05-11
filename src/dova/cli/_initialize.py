import logging
from dataclasses import dataclass
from pathlib import Path

import typer

from dova.core.logging import get_logger, setup_logging
from dova.core.repo import find_repo


@dataclass
class ContextObject:
    verbose: bool
    logger: logging.Logger
    main_logger: logging.Logger

    @staticmethod
    def callback(
        ctx: typer.Context, verbose: bool = False, log_file: Path | None = None
    ) -> None:
        setup_logging(logging.DEBUG if verbose else logging.INFO, file_path=log_file)
        main_logger = get_logger("dova")
        cli_logger = get_logger("dova.cli")
        ctx.obj = ContextObject(
            verbose=verbose, logger=cli_logger, main_logger=main_logger
        )


@dataclass
class ContextObjectWithRepoPath(ContextObject):
    repo_path: Path | None = None

    @staticmethod
    def callback(ctx: typer.Context):
        repo_path = find_repo(Path.cwd())
        if repo_path is None:
            ctx.obj.logger.error("No Dova repository found in current directory.")
            raise typer.Exit(code=1)
        ctx.obj = ContextObjectWithRepoPath(
            verbose=ctx.obj.verbose,
            logger=ctx.obj.logger,
            main_logger=ctx.obj.main_logger,
            repo_path=repo_path,
        )
