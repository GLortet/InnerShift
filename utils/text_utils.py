"""Utility helpers for text processing."""

from __future__ import annotations


def normalize_text(text: str) -> str:
    """Normalize text for downstream processing."""
    raise NotImplementedError


def extract_keywords(text: str, top_k: int = 10) -> list[str]:
    """Return the top keywords from the given text."""
    raise NotImplementedError
