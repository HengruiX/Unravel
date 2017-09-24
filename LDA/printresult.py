import sklearn.decomposition as d
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import sys

res = sys.argv[1]
num = int(sys.argv[2])

def print_top_words(model, feature_names, n_top_words):
        for topic_idx, topic in enumerate(model.components_): 
                message = "Topic #%d: " % topic_idx
                message += " ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]])
                print(message)
        print()

 
res = pickle.load(open(res, "rb"))
print_top_words(res[0], res[1].get_feature_names(), num)