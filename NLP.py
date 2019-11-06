import fuzzy
# Convert up to 10 characters to phonetic character
soundex = fuzzy.Soundex(10)
# Text to process
word = 'phone'
soundex(word)

#Doc2vec
#stemming, lemmatization, n-grams, stop word removal etc

#Import packages
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

## Exapmple document (list of sentences)
doc = ["I love data science",
        "I love coding in python",
        "I love building NLP tool",
        "This is a good phone",
        "This is a good TV",
        "This is a good laptop"]

# Tokenization of each document
tokenized_doc = []
for d in doc:
    tokenized_doc.append(word_tokenize(d.lower()))
tokenized_doc

# Convert tokenized document into gensim formated tagged data
tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_doc)]
tagged_data


## Train doc2vec model
model = Doc2Vec(tagged_data, vector_size=20, window=2, min_count=1, workers=4, epochs = 100)
# Save trained doc2vec model
model.save("test_doc2vec.model")
## Load saved doc2vec model
model= Doc2Vec.load("test_doc2vec.model")
## Print model vocabulary
model.wv.vocab




#Doc2vec
#Weighted sum of word vectors
#Skip thought vectors
#Bag-of-words
#TF-IDF
#FastSent
…etc

https://www.thinkinfi.com/2019/10/simple-explanation-of-doc2vec.html
