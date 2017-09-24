import pickle
import random
import sklearn.decomposition as d
from sklearn.feature_extraction.text import CountVectorizer

wordX = pickle.load(open("pairX", 'rb'))

def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_):
                message = "Topic #%d: " % topic_idx
                message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
                print(message)
        print()

# saves the model, vectorizer as well as associated parameters
def perform_lda(max_df, min_df, topics, ngram):
        vectorizer = CountVectorizer(stop_words='english', max_df=max_df, min_df=min_df, ngram_range=ngram)
        matrixX = vectorizer.fit_transform(wordX)
        lda = d.LatentDirichletAllocation(n_components=topics, max_iter=10, verbose=1)
        lda.fit(matrixX)
        return [lda, vectorizer, max_df, min_df, topics, ngram]

i = 1

# Interates through the param space
for ngram in [(1,1)]:
        for topics in [7,8,9,10,11,12,13,14,15,16]:
                res = perform_lda(0.2, 0.005, topics, ngram)
                pickle.dump(res, open("result" + str(i), "wb"))
                i += 1