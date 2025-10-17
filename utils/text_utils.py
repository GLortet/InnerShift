from __future__ import annotations
import re
from collections import Counter

STOPWORDS_FR = set("""
au aux avec ce ces dans de des du elle en et il ils je la le les leur lui ma mais me même mes moi mon ne nos notre nous on ou par pas pour qu que qui sa se ses son sur ta te tes toi ton tu un une vos votre vous c d l j m n s t y à où est sont été être ai as avons avez ont suis es sommes êtes étaient étais était serais serait serions seriez seraient
""".split())

TOKEN_RE = re.compile(r"[\\w'-]+", re.UNICODE)

def normalize(text: str) -> str:
    return re.sub(r"\\s+", " ", text).strip()

def tokenize(text: str) -> list[str]:
    tokens = [t.lower() for t in TOKEN_RE.findall(text)]
    return [t for t in tokens if t not in STOPWORDS_FR and len(t) > 2]

def top_keywords(text: str, k: int = 10) -> list[tuple[str, int]]:
    tokens = tokenize(text)
    return Counter(tokens).most_common(k)
