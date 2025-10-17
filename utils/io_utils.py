"""Input/output utility stubs."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def read_json(path: Path | str) -> Any:
    """Read JSON content from disk."""
    raise NotImplementedError


def write_json(path: Path | str, data: Any) -> None:
    """Write JSON content to disk."""
    raise NotImplementedError
