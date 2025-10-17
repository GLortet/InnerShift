from pathlib import Path
from nlp_analysis import analyze_text

def test_nlp_basic():
    txt = "Je me sens motivé, j'avance sur un plan concret avec des valeurs et de l'impact."
    res = analyze_text(txt)
    assert res.sentiment in {"POSITIVE", "NEGATIVE"}
    assert isinstance(res.keywords, list)
    assert isinstance(res.intelligences, dict)
