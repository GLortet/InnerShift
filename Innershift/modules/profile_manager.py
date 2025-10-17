import json
import os
from datetime import datetime

def charger_profil(user_id):
    chemin = f"data/profiles/{user_id}.json"
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Création d'un profil vierge
        return {
            "id": user_id,
            "intelligences": {},  # Moyennes des scores cumulés
            "historique": []       # Liste des interactions avec détail NLP
        }

def sauvegarder_profil(user_id, data):
    chemin = f"data/profiles/{user_id}.json"
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def mettre_a_jour_profil(profil, analyse_nlp, texte_brut):
    """Mise à jour du profil avec les données d'une nouvelle interaction"""

    # Ajouter au journal
    interaction = {
        "timestamp": datetime.now().isoformat(),
        "texte": texte_brut,
        "mots_cles": analyse_nlp["mots_cles"],
        "theme_dominant": analyse_nlp["theme_dominant"],
        "scores_intelligences": analyse_nlp["scores_intelligences"]
    }
    profil["historique"].append(interaction)

    # Calcul progressif de la moyenne des intelligences
    total_scores = {k: 0 for k in analyse_nlp["scores_intelligences"].keys()}
    for entry in profil["historique"]:
        for k, v in entry["scores_intelligences"].items():
            total_scores[k] += v

    n = len(profil["historique"])
    profil["intelligences"] = {k: round(v / n, 2) for k, v in total_scores.items()}

    return profil
