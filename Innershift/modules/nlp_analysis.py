import spacy
from sentence_transformers import SentenceTransformer, util
import numpy as np

# Chargement des modèles
nlp = spacy.load("fr_core_news_sm")
sbert_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

# Dictionnaire des intelligences multiples et de leurs champs lexicaux
INTELLIGENCES = {
    "logico-mathématique": [
        "logique", "analyse", "raisonnement", "problème", "résolution", "formule", "structure"
    ],
    "linguistique": [
        "langue", "écriture", "parole", "lecture", "expression", "mot", "discours"
    ],
    "kinesthésique": [
        "mouvement", "corps", "toucher", "geste", "physique", "sport", "danse"
    ],
    "musicale": [
        "musique", "rythme", "chant", "mélodie", "instrument", "écoute", "voix"
    ],
    "visuo-spatiale": [
        "image", "vision", "forme", "graphique", "dessin", "couleur", "carte"
    ],
    "interpersonnelle": [
        "relation", "équipe", "écoute", "collaboration", "entraide", "communication"
    ],
    "intrapersonnelle": [
        "réflexion", "émotion", "conscience", "introspection", "valeurs", "identité", "motivation"
    ],
    "naturaliste": [
        "nature", "animal", "écologie", "plante", "environnement", "climat", "forêt"
    ]
}

def analyser_texte(texte):
    """Analyse un texte pour détecter les intelligences dominantes, extraire les mots-clés et déduire le thème principal."""

    # Nettoyage linguistique du texte
    doc = nlp(texte)
    mots_cles = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]

    # Embedding du texte global
    embeddings_texte = sbert_model.encode([texte], convert_to_tensor=True)

    # Analyse des similarités avec chaque intelligence
    scores = {}
    for intelligence, mots_cles_thema in INTELLIGENCES.items():
        # Création d’un mini-texte pour chaque intelligence
        thema_text = " ".join(mots_cles_thema)
        emb_thema = sbert_model.encode([thema_text], convert_to_tensor=True)
        sim = util.pytorch_cos_sim(embeddings_texte, emb_thema).item()
        scores[intelligence] = round(sim * 10, 2)  # Score sur 10

    # Thème dominant = score le plus élevé
    theme_dominant = max(scores, key=scores.get)

    return {
        "mots_cles": mots_cles,
        "scores_intelligences": scores,
        "theme_dominant": theme_dominant
    }
