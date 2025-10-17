"""Tests for the audio processing module."""

from __future__ import annotations

from modules import audio_processing


def test_transcribe_audio_stub() -> None:
    """Ensure the audio transcription stub is defined."""
    assert hasattr(audio_processing, "transcribe_audio")
