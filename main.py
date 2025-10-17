from __future__ import annotations
import argparse
from typing import Any, Dict

from audio_processing import transcribe_audio
from nlp_analysis import analyze_text
from profile_manager import update_profile
from report_generator import generate_pdf

def run(audio_path: str, user: str) -> str:
    print("[1/4] Transcription…")
    text = transcribe_audio(audio_path)

    print("[2/4] Analyse NLP…")
    res = analyze_text(text)

    analysis: Dict[str, Any] = {
        "text": res.text,
        "sentiment": res.sentiment,
        "sentiment_score": res.sentiment_score,
        "keywords": res.keywords,
        "pcm_guess": res.pcm_guess,
        "intelligences": res.intelligences,
    }

    print("[3/4] Mise à jour du profil…")
    profile = update_profile(user, analysis)

    print("[4/4] Génération du PDF…")
    pdf_path = generate_pdf(user, analysis)

    print(f"✅ Terminé. Rapport: {pdf_path}")
    return str(pdf_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="InnerShift – audio → PDF")
    parser.add_argument("--audio", required=True, help="Chemin du fichier audio")
    parser.add_argument("--user", required=True, help="Identifiant utilisateur (nom)")
    args = parser.parse_args()
    run(args.audio, args.user)
