from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any

from transformers import pipeline
from utils.text_utils import normalize, top_keywords

@dataclass
class NLPResult:
    text: str
    sentiment: str
    sentiment_score: float
    keywords: list[tuple[str, int]]
    pcm_guess: str
    intelligences: Dict[str, float]

# Heuristiques simples (à ajuster/entraîner plus tard)
PCM_HINTS = {
    "Analyseur": ["données", "preuve", "logique", "structure", "processus", "mesure"],
    "Énergiseur": ["fun", "challenge", "rapide", "gagner", "impact", "audace"],
    "Empathique": ["ressens", "émotion", "écoute", "bienveillance", "besoin", "relation"],
    "Persévérant": ["valeurs", "conviction", "cohérence", "sens", "engagement"],
    "Travaillomane": ["objectif", "plan", "efficacité", "résultat", "délai"],
    "Rêveur": ["idée", "vision", "imaginer", "sensibilité", "créatif"],
    "Promoteur": ["action", "deal", "vente", "opportunité", "direct"]
}

INTELLIGENCE_HINTS = {
    "logico-math": ["calcul", "optimiser", "logique", "structure", "modèle"],
    "linguistique": ["mot", "parole", "écrire", "raconter", "texte"],
    "spatiale": ["image", "visualiser", "dessin", "carte", "schéma"],
    "kinesthésique": ["mouvement", "corps", "geste", "physique"],
    "musicale": ["rythme", "musique", "son", "mélodie"],
    "interpersonnelle": ["équipe", "ensemble", "relation", "écoute"],
    "intrapersonnelle": ["moi", "introspection", "conscience", "valeurs"],
    "naturaliste": ["nature", "environnement", "écologie", "plante"]
}

_sentiment_pipe = None

def _get_sentiment_pipe():
    global _sentiment_pipe
    if _sentiment_pipe is None:
        _sentiment_pipe = pipeline("sentiment-analysis")
    return _sentiment_pipe

def score_hints(text: str, hints: dict[str, list[str]]) -> dict[str, float]:
    t = text.lower()
    scores = {}
    for label, words in hints.items():
        scores[label] = sum(t.count(w.lower()) for w in words)
    total = sum(scores.values()) or 1.0
    return {k: v / total for k, v in scores.items()}

def guess_pcm(scores: dict[str, float]) -> str:
    return max(scores.items(), key=lambda kv: kv[1])[0]

def analyze_text(text: str, top_k: int = 12) -> NLPResult:
    text = normalize(text)
    sp = _get_sentiment_pipe()
    s = sp(text[:512])[0]  # limiter pour vitesse
    sentiment = s["label"].upper()
    score = float(s["score"]) if "score" in s else 0.5

    kw = top_keywords(text, k=top_k)
    pcm_scores = score_hints(text, PCM_HINTS)
    intel_scores = score_hints(text, INTELLIGENCE_HINTS)

    return NLPResult(
        text=text,
        sentiment=sentiment,
        sentiment_score=score,
        keywords=kw,
        pcm_guess=guess_pcm(pcm_scores),
        intelligences=intel_scores
    )
