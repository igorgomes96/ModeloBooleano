import nltk

def loadStopWords():
    stopwords = nltk.corpus.stopwords.words("portuguese")
    return stopwords

def tokenize(texto):
    tokens = nltk.word_tokenize(texto)
    stopwords = loadStopWords()
    stemmer = nltk.stem.RSLPStemmer()
    tokens = [token for token in tokens if token not in stopwords]
    tokens = [stemmer.stem(token) for token in tokens]
    #tokens = list(filter(lambda token: token not in stopwords, tokens))
    #tokens = list(map(lambda token: stemmer.stem(token), tokens))
    return tokens