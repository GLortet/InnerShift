"""Report generation stubs."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping, Any


def generate_report(user_id: str, analysis: Mapping[str, Any], output_dir: Path | str | None = None) -> Path:
    """Generate a report for the given user and return the output path."""
    raise NotImplementedError
