"""pytest-fluentbit-logging."""

from importlib_metadata import PackageNotFoundError, version

__version__ = "0.1.5"
try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    pass


from .additional_information import (
    additional_session_information_callback,
    additional_test_information_callback,
)
from .plugin import get_session_uid, get_test_uid

__all__ = [
    "additional_session_information_callback",
    "additional_test_information_callback",
    "get_session_uid",
    "get_test_uid",
]
