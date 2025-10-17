"""NLP analysis stubs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(slots=True)
class AnalysisResult:
    """Structured result of an NLP analysis."""

    text: str
    sentiment: str
    sentiment_score: float
    keywords: Sequence[str]


def analyze_text(text: str) -> AnalysisResult:
    """Analyze raw text and return a structured result."""
    raise NotImplementedError
