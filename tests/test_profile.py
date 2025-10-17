"""Tests for the profile manager module."""

from __future__ import annotations

from modules import profile_manager


def test_update_profile_stub() -> None:
    """Ensure the profile manager stub is defined."""
    assert hasattr(profile_manager, "update_profile")
