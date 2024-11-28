from translate import Translator

translator = Translator(from_lang="lv", to_lang="en")

texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translations = []
for text in texts_lv:
    translated_text = translator.translate(text)
    translations.append((text, translated_text))

for original, translated in translations:
    print(f"Teksts: '{original}' -> Tulkots: '{translated}'")
