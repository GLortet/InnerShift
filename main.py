"""Command-line interface for InnerShift."""

from __future__ import annotations

import argparse
from typing import Sequence


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(description="InnerShift command-line interface")
    parser.add_argument("--audio", help="Path to the audio file", required=False)
    parser.add_argument("--user", help="Identifier of the user", required=False)
    return parser


def main(argv: Sequence[str] | None = None) -> str:
    """Parse arguments and return a placeholder result."""
    parser = build_parser()
    parser.parse_args(list(argv) if argv is not None else None)
    return "TODO"


if __name__ == "__main__":
    print(main())
