from gensim.models import Word2Vec

sentences = [["māja", "ir", "liela"], ["dzīvoklis", "atrodas", "Rīgā"], ["jūra", "ir", "skaista"]]
model = Word2Vec(sentences, vector_size=50, min_count=1)

word_vectors = {word: model.wv[word] for word in ["māja", "dzīvoklis", "jūra"]}
print("Vārdu vektori:", word_vectors)

similarities = model.wv.most_similar("māja")
print("Līdzīgākie vārdi vārdam 'māja':", similarities)
