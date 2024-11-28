from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
words = text.lower().replace('.', '').replace(',', '').split()

word_count = Counter(words)
print("Vārdu biežums:", word_count)
