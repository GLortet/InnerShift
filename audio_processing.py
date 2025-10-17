from __future__ import annotations
import os
from pathlib import Path
from typing import Optional

from openai import OpenAI

DATA_DIR = Path("data")
AUDIO_DIR = DATA_DIR / "audio"
TRANS_DIR = AUDIO_DIR / "transcriptions"

for p in (AUDIO_DIR, TRANS_DIR):
    p.mkdir(parents=True, exist_ok=True)

def transcribe_audio(audio_path: str, language: str = "fr") -> str:
    """Transcrit un fichier audio via OpenAI Whisper‑1.
    Requiert OPENAI_API_KEY.
    """
    client = OpenAI()
    audio_path = Path(audio_path)
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio introuvable: {audio_path}")

    with open(audio_path, "rb") as f:
        resp = client.audio.transcriptions.create(
            model="whisper-1",
            file=f,
            language=language
        )
    text = resp.text.strip()

    # Sauvegarde de la transcription
    out = TRANS_DIR / f"{audio_path.stem}.txt"
    out.write_text(text, encoding="utf-8")
    return text
