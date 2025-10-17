import spacy
from textblob import TextBlob
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize
import re

# Initialisation de Spacy
nlp = spacy.load("fr_core_news_sm")

# Télécharger une fois uniquement si pas encore fait
nltk.download('punkt')

# Fonction d'analyse complète
def analyser_texte(texte):
    doc = nlp(texte)
    
    # Extraction mots-clés importants (sans stopwords et ponctuation)
    mots_cles = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

    # Analyse de sentiment (positif/négatif/neutre)
    sentiment = analyser_emotions(texte)
    
    # Détection du type de phrases
    types_phrases = detecter_types_phrases(texte)
    
    # Sujets abordés (noms propres ou noms significatifs)
    sujets = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]

    return {
        "mots_cles": mots_cles,
        "emotion_globale": emotion_globale(texte),
        "repartition_phrases": analyser_phrases(texte),
        "sujets_abordes": list(set(sujets))
    }

# Détection d'émotion globale simplifiée (Positive/Neutre/Négative)
def emotion_globale(texte):
    analyse = TextBlob(texte)
    polarite = analyse_sentiment(texte)
    if polarite(texte) > 0.1:
        return "Positive"
    elif polarite(texte) < -0.1:
        return "Négative"
    else:
        return "Neutre"

# Fonction de polarité avec TextBlob
from textblob import TextBlob
def polarite(texte):
    blob = TextBlob(texte)
    return blob.sentiment.polarity

# Détail des émotions
def emotion_globale(texte):
    polarite = TextBlob(texte).sentiment.polarity
    if polarite >= 0.4:
        return "Très positive"
    elif polarite >= 0.1:
        return "Positive"
    elif polarite > -0.1:
        return "Neutre"
    elif polarite > -0.4:
        return "Négative"
    else:
        return "Très négative"

# Répartition type de phrases
def repartition_type_phrases(texte):
    phrases = nltk.sent_tokenize(texte, language='french')
    repartition = {"Question": 0, "Exclamation": 0, "Affirmation": 0}
    for phrase in phrases:
        if phrase.strip().endswith('?'):
            repartition["Question"] += 1
        elif phrase.strip().endswith('!'):
            repartition["Exclamation"] += 1
        else:
            repartition["Affirmation"] = repartition.get("Affirmation", 0) + 1
    return repartition

# Extraction polarité pour précision émotionnelle
from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
blob = TextBlob("bonjour")

def polarite(texte):
    tb = Blob(texte, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    return tb.sentiment[0]

# Fonction complète combinée
def analyser_phrases_emotions(texte):
    phrases = nltk.sent_tokenize(texte, language='french')
    emotions = [emotion_globale(phrase) for phrase in phrases]
    return dict(Counter(emotions))

# Analyse finale améliorée qui combine tout
def analyse_complete(texte):
    return {
        "mots_cles": analyser_texte(texte)["mots_cles"],
        "sentiment_general": emotion_globale(texte),
        "phrases": analyser_phrases_emotions(texte),
        "sujets_principaux": Counter(analyser_texte(texte)["mots_cles"]).most_common(5),
        "questions_posees": sum(1 for phrase in nltk.sent_tokenize(texte, language='french') if phrase.endswith('?'))
    }

if __name__ == "__main__":
    exemple_texte = "Je suis ravi de faire ce PoC avec toi ! Mais comment puis-je améliorer mon approche ?"
    resultat = analyse_texte(exemple_texte)
    print(resultat)
