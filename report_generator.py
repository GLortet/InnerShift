from __future__ import annotations
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

OUTPUT = Path("data/reports/pdf")
OUTPUT.mkdir(parents=True, exist_ok=True)

def _plot_intelligences(intel: Dict[str, float], out_png: Path) -> None:
    labels = list(intel.keys())
    values = [intel[k] for k in labels]
    plt.figure()
    plt.bar(labels, values)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()

def generate_pdf(user: str, analysis: Dict[str, Any]) -> Path:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = OUTPUT / f"innershift_report_{ts}.pdf"

    # Chart intelligences
    chart = OUTPUT / f"intel_{ts}.png"
    _plot_intelligences(analysis.get("intelligences", {}), chart)

    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2*cm, height - 2*cm, f"Rapport InnerShift – {user}")

    # Sentiment
    c.setFont("Helvetica", 12)
    c.drawString(2*cm, height - 3.2*cm, f"Sentiment: {analysis.get('sentiment')} ({analysis.get('sentiment_score'):.2f})")
    c.drawString(2*cm, height - 4.0*cm, f"PCM (heuristique): {analysis.get('pcm_guess')}")

    # Keywords
    c.drawString(2*cm, height - 5.0*cm, "Mots‑clés:")
    y = height - 5.6*cm
    for k, freq in analysis.get("keywords", [])[:12]:
        c.drawString(2.4*cm, y, f"• {k} ({freq})")
        y -= 0.5*cm
        if y < 3*cm:
            c.showPage(); y = height - 2*cm

    # Insert chart
    c.showPage()
    c.drawImage(str(chart), 2*cm, height/2 - 4*cm, width=width-4*cm, preserveAspectRatio=True, mask='auto')

    # Footer
    c.setFont("Helvetica", 9)
    c.drawString(2*cm, 1.5*cm, "InnerShift – Rapport généré automatiquement")

    c.save()
    try:
        chart.unlink(missing_ok=True)
    except Exception:
        pass
    return pdf_path
