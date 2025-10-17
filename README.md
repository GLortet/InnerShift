# InnerShift 🧠✨
**L’IA qui t’aide à te comprendre avant de te changer.**

InnerShift transforme un enregistrement audio en un **rapport PDF** (mots‑clés, tonalité émotionnelle, carto PCM* heuristique*, hypothèses d’intelligences multiples, recommandations).

> ⚠️ PCM® est une marque. Ici, l’analyse PCM est **heuristique** (mappages textuels) et non une certification officielle.

## 🚀 Démarrage rapide
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt

# clé API OpenAI
setx OPENAI_API_KEY "sk-..."        # Windows
# export OPENAI_API_KEY="sk-..."     # macOS/Linux

python main.py --audio sample.wav --user "Gilles"
```

## 📦 Pipeline

```
audio_processing → nlp_analysis → profile_manager → report_generator → PDF
```

## 📁 Arborescence

```
innershift/
 ├─ main.py
 ├─ audio_processing.py
 ├─ nlp_analysis.py
 ├─ profile_manager.py
 ├─ report_generator.py
 ├─ utils/
 │   └─ text_utils.py
 ├─ config/
 │   └─ settings.json
 ├─ assets/
 │   ├─ logos/innershift_logo.png (optionnel)
 │   └─ fonts/(optionnel)
 ├─ data/
 │   ├─ audio/{recordings, transcriptions}
 │   ├─ reports/pdf
 │   └─ user_profiles.json
 ├─ tests/
 ├─ requirements.txt
 └─ README.md
```

## 🔜 Roadmap courte

* [ ] UI (Streamlit) pour enregistrer et lancer l’analyse
* [ ] Graph historique des scores par séance
* [ ] Export JSON complet du rapport (+ API)
