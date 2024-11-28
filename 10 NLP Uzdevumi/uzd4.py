from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

analyzer = SentimentIntensityAnalyzer()
translator = Translator()

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts" # ja atstāj kā "Neitrāls produkts, nekas īpašs." tad atgriež ka teikums negatīvs
]

for sentence in sentences:
    translated_sentence = translator.translate(sentence, src='lv', dest='en').text

    sentiment_score = analyzer.polarity_scores(translated_sentence)
    compound_score = sentiment_score['compound']

    if compound_score >= 0.05:
        mood = "pozitīvs"
    elif compound_score <= -0.05:
        mood = "negatīvs"
    else:
        mood = "neitrāls"
    
    print(f"Teikums: '{sentence}' -> Noskaņojums: {mood}")
