"""Tests for the report generator module."""

from __future__ import annotations

from modules import report_generator


def test_generate_report_stub() -> None:
    """Ensure the report generator stub is defined."""
    assert hasattr(report_generator, "generate_report")
