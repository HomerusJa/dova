class DovaException(Exception):
    """Base exception for all Dova-related errors."""


class RepoNotFoundException(DovaException):
    """Raised when a Dova repository could not be found."""
