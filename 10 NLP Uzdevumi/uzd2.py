import langid

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

for text in texts:
    language, _ = langid.classify(text)
    print(f"Teksts: '{text}' -> Valoda: {language}")
