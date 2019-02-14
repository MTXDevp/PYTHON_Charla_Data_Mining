import nltk
import nltk
from nltk.corpus import movie_reviews
import random
from nltk.corpus import twitter_samples
print (twitter_samples.fileids())
# https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python

# autocompletado PNL

# "Titanic es una gran pelIcula".
# "Titanic no es una gran pelIcula".
# "El Titanic es una pelIcula". neutral

#APRENDIZAJE SUPERVISADO

#PILLAMOS PALABRAS POSTIVIAS DE LA FRASE Y HACEMOS UN RECUENTO DE ELLAS BUSCADO LA NATURALEZA POSITIVA

#las reglas de Bayes para formar las probabilidades de clasificacion

# Natural Language Toolkit.

#bolsas de palabras

#naive bayes

#clasificador

nltk.download('movie_reviews')



documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


#clasificador Bayesiano ingenuo es un clasificador probabilistico fundamentado en el teorema de Bayes
featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))

classifier.show_most_informative_features(5)
