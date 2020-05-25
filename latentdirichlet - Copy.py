from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

import warnings
warnings.simplefilter("ignore", DeprecationWarning)
# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA
 
# Helper function
def topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        return " ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]])
        

number_topics = 1
number_words = 5

def find_topics(data):
    count_vectorizer = CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform(data)
    lda = LDA(n_components=number_topics, n_jobs=-1)
    lda.fit(count_data)

    return topics(lda, count_vectorizer, number_words)
