import json
from fpdf import FPDF # type: ignore
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from datetime import datetime
import os

def nettoyer_texte(text):
    """Remplace les caractères spéciaux pour assurer la compatibilité avec fpdf."""
    remplacements = {
        '’': "'", '“': '"', '”': '"', '–': '-', '—': '-', '…': '...',
        '«': '"', '»': '"', '•': '-', 'œ': 'oe', 'Œ': 'Oe', '–': '-'
    }
    for old, new in remplacements.items():
        text = text.replace(old, new)
    return text

# === CONFIGURATION ===
user_id = "gilles_001"
profile_path = "C:/Users/33671/PoC_AI_Coach/data/profiles/gilles_001.json"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_path = f"C:/Users/33671/PoC_AI_Coach/data/reports/rapport_innershift_{user_id}_{timestamp}.pdf"
chart_path_1 = f"C:/Users/33671/PoC_AI_Coach/data/reports/intelligence_chart_{timestamp}.png"
chart_path_2 = f"C:/Users/33671/PoC_AI_Coach/data/reports/evolution_chart_{timestamp}.png"

# === LECTURE DU PROFIL ===
with open(profile_path, "r", encoding="utf-8") as f:
    profil = json.load(f)

scores = profil["intelligences"]
labels = [k.capitalize() for k in scores.keys()]
values = list(scores.values())

# === GRAPH 1: PROFIL D’INTELLIGENCES ===
fig, ax = plt.subplots()
ax.barh(labels, values)
ax.set_xlim(0, 10)
ax.set_title("Profil d'intelligences multiples")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(chart_path_1)
plt.close()

# === GRAPH 2: ÉVOLUTION TEMPORELLE ===
evolution = {}
for interaction in profil.get("interactions", profil.get("historique", [])):
    for k, v in interaction["scores_intelligences"].items():
        evolution.setdefault(k, []).append(v)

fig, ax = plt.subplots()
for k, v in evolution.items():
    ax.plot(v, label=k)
ax.set_title("Évolution des intelligences au fil des interactions")
ax.set_xlabel("Interactions")
ax.set_ylabel("Score")
ax.set_ylim(0, 10)
ax.legend()
plt.tight_layout()
plt.savefig(chart_path_2)
plt.close()

# === PDF GENERATION ===
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# PAGE 1 : COUVERTURE
pdf.add_page()
pdf.set_font("Arial", 'B', 20)
pdf.cell(0, 20, "Rapport de Coaching - InnerShift", ln=True, align='C')
pdf.set_font("Arial", '', 14)
pdf.ln(10)
pdf.cell(0, 10, f"Utilisateur : {user_id}", ln=True)
pdf.cell(0, 10, f"Généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M')}", ln=True)
pdf.ln(20)
pdf.set_font("Arial", 'I', 12)
pdf.multi_cell(0, 10, nettoyer_texte("Ce document synthétise votre état cognitif et émotionnel à travers les dernières conversations analysées par notre moteur NLP et IA de coaching personnalisé."))

# PAGE 2 : PROFIL D’INTELLIGENCES
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, nettoyer_texte("Votre Profil d'Intelligences Multiples"), ln=True)
pdf.image(chart_path_1, x=25, w=160)
pdf.ln(10)

# Résumé dynamique
pdf.set_font("Arial", '', 12)
for k, v in scores.items():
    if v > 8:
        commentaire = f"Votre intelligence {k} est un pilier : continuez à l'exploiter à fond."
    elif v >= 6:
        commentaire = f"Votre intelligence {k} est bien présente et peut être valorisée davantage."
    else:
        commentaire = f"L'intelligence {k} pourrait être développée avec des exercices adaptés."
    pdf.multi_cell(0, 8, f"- {commentaire}")

# PAGE 3 : EVOLUTION
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, nettoyer_texte("Évolution de vos capacités dans le temps"), ln=True)
pdf.image(chart_path_2, x=25, w=160)
pdf.ln(10)

# PAGE 4 : CONCLUSION
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, nettoyer_texte("Conclusion & Recommandations"), ln=True)
pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, nettoyer_texte("Vos récentes conversations révèlent une tendance forte vers le développement personnel et l'expression des émotions. "
                     "Nous recommandons de continuer vos efforts dans les dimensions déjà fortes tout en explorant les axes moins dominants "
                     "pour équilibrer votre développement cognitif.\n\nMerci de votre confiance et à très bientôt pour une nouvelle analyse approfondie."))

pdf.ln(20)
pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 10, nettoyer_texte("InnerShift • Transform your voice into insight"), ln=True, align='C')

# SAVE PDF
pdf.output(report_path)
print(f"✅ Rapport sauvegardé dans : {report_path}")