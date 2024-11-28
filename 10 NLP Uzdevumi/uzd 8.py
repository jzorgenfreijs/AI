import spacy
from googletrans import Translator

translator = Translator()
nlp = spacy.load("en_core_web_sm")

text_latvian = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

translated = translator.translate(text_latvian, src='lv', dest='en') # spacy multivalodu modelis neatpazina starp personu un organizaciju tapēc tulko uz angļu
text_english = translated.text
print(f"Pārtulkots teksts: {text_english}")

doc = nlp(text_english)

for ent in doc.ents:
    print(f"Atpazītā frāze: {ent.text} -> Kategorija: {ent.label_}")
