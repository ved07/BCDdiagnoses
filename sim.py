import nltk
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import bigrams
nltk.download('punkt')
# pickle
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def sim(text1, text2):
  try:
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
  except:
    return ("Can't get the cosine similarity of this one, maybe its all stop words.")  

#Moved this to a different file cos its like 27 lines long
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def sim2(text1, text2):
  try:
    text1 = " ".join(list(text1))
    text2 = " ".join(list(text2))
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]
  except:
    t = list(text1.replace(" ",""))
    y = list(text2.replace(" ",""))
    m = len(intersection(t,y))
    x = len(t)
    y = len(y)
    avg = float((len(t)+len(y))/2)
    return float(m/avg)



