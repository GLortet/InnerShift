from datetime import datetime
import os
from modules.audio_processing import transcrire_audio
from modules.nlp_analysis import analyser_texte
from modules.profile_manager import charger_profil, sauvegarder_profil, mettre_a_jour_profil
from modules.report_generator import generer_rapport_pdf

def main():
    # --- Configuration utilisateur ---
    user_id = "gilles_001"
    fichier_audio = "data/conversation/test_audio.mp3"

    # --- Vérification fichier ---
    if not os.path.exists(fichier_audio):
        print(f"❌ Erreur : Le fichier {fichier_audio} n'existe pas ! Vérifie le chemin.")
        return

    # --- Chargement du profil ---
    profil = charger_profil(user_id)

    # --- Transcription ---
    print("🎙️ Transcription en cours...")
    texte_transcrit = transcrire_audio(fichier_audio)
    print("✅ Transcription terminée.")

    # --- Analyse NLP enrichie ---
    print("🧠 Analyse NLP...")
    analyse = analyser_texte(texte_transcrit)
    print("✅ Analyse terminée.")

    # --- Mise à jour du profil ---
    profil = mettre_a_jour_profil(profil, analyse, texte_transcrit)
    sauvegarder_profil(user_id, profil)

    # --- Affichage résumé ---
    print("\n===== Résumé de l'interaction =====")
    print(f"Texte :\n{texte_transcrit}\n")
    print(f"Thème dominant : {analyse['theme_dominant']}")
    print(f"Scores intelligences :")
    for k, v in analyse['scores_intelligences'].items():
        print(f" - {k.capitalize()} : {v}/10")

    print("\n✅ Interaction analysée et profil mis à jour !")

    rapport_pdf_path = f"data/reports/rapport_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    generer_rapport_pdf(user_id, profil, rapport_pdf_path)

if __name__ == "__main__":
    main()
