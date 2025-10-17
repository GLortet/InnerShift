"""Audio processing stubs."""

from __future__ import annotations

from pathlib import Path


def transcribe_audio(audio_path: Path | str, language: str = "fr") -> str:
    """Return a transcription for the given audio file."""
    raise NotImplementedError
