import pickle
import re
from nltk.stem.lancaster import LancasterStemmer

pairList = pickle.load(open("pairList", 'rb'))
stemmer = LancasterStemmer()

r = re.compile('[A-Za-z][A-Za-z]+')
wordX = [r.findall(x[4]) for x in pairList]
wordX = [' '.join([stemmer.stem(x) for x in y]) for y in wordX]
pickle.dump(wordX, open("pairX", 'wb'))