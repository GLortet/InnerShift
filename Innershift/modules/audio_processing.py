import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import os

# Chargement du modèle Whisper
model = whisper.load_model("base")

def enregistrer_audio(nom_fichier, duree=10, frequence=44100):
    """Enregistre un fichier audio depuis le micro sur une durée donnée (en secondes)."""
    print(f"Enregistrement ({duree} secondes)...")
    audio = sd.rec(int(duree * frequence), samplerate=frequence, channels=1, dtype='int16')
    sd.wait()  # Attendre la fin de l'enregistrement
    write(nom_fichier, frequence, audio)
    print(f"Fichier enregistré : {nom_fichier}")

def transcrire_audio(fichier_audio):
    """Transcrit un fichier audio en texte avec Whisper."""
    if not os.path.exists(fichier_audio):
        raise FileNotFoundError(f"❌ Erreur : Le fichier {fichier_audio} n'existe pas.")
    print("Transcription en cours avec Whisper...")
    result = model.transcribe(fichier_audio)
    return result["text"]
