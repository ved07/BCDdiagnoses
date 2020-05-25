import nltk
import csv
from nltk import ngrams
import sim
import numpy as np
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
def remove_stops(example_sent):
    stop_words = set(stopwords.words('english')) 
  
    word_tokens = word_tokenize(example_sent) 
  
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
  
    filtered_sentence = [] 
  
    for w in word_tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
    return filtered_sentence
  
#print(word_tokens) 
#print(filtered_sentence) 
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet as wn
nltk.download("wordnet")
def get_word_similarity(w1,w2):
    w1.replace("","_")
    w2.replace("","_")
    cb = wn.synset('{}.n.01'.format(w2))
    ib = wn.synset('{}.n.01'.format(w2))
    return cb.wup_similarity(ib)

with open('data.csv', newline='') as f:
  reader = csv.reader(f)
  row1 = next(reader)  # gets the first line
#print(row1)
symptoms = row1

#ines = input("How do you feel?")

def get_most_similar_symptoms(ms):
    sims = []
    for symp in symptoms:
        sims.append(sim.sim2(ms, symp))
    return [symptoms[np.argmax(sims)],sims[np.argmax(sims)]]
#Algorithm layer 1: simplest but least usable layer
def commons(a,b):
  lista = ("/".join(a).lower()).split("/")
  listb = ("/".join(b).lower()).split("/")
  
  return len(list(set(lista).intersection(listb)))



number_topics = 1
number_words = 5

def get_word_synonyms_from_sent(word, sent):
    word_synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemma_names():
            if lemma in sent and lemma != word:
                word_synonyms.append(lemma)
    return len(word_synonyms)



def ngramsw(text, n):
    words = text.split()
    return [ words[i:i+n] for i in range(len(words)-n+1) ]

def tri_split(sentence):
    n = 3
    sentence = " ".join(remove_stops(sentence))
    trigrams = ngramsw(sentence,n)
    m = []
    for gram in trigrams:
        m.append(" ".join(gram))
    return m

#def trigram_syns()
#def common_word()
def find_symps_basic(sentence):

    tris = tri_split(sentence)
    sentence = " ".join(remove_stops(sentence))
    symptomsret = []
    for sym in symptoms:
        if sym.lower() in sentence:
            symptomsret.append(sym)
    
    #tops = find_topics([sentence])
    for word in sentence:
        word = word.replace("ing","")
        mm = get_most_similar_symptoms(word)
        if(mm[1]>0.77575757):
            print("syn {0} with similarity {1} of word {2}".format(mm[0],mm[1],word))
            symptomsret.append(mm[0])

    
    for sym in tris:
        for symptom in symptoms:
            print(sim.sim(sym,symptom))
            if sim.sim(sym,symptom) > 0.65:
                symptomsret.append(symptom)
    return list(set(symptomsret))
def intersect_2(a,b):
    m = []
    for x in b:
        if x.lower() in a:
            m.append(x)
        else:
            pass
    return m

def intersect_and_remove(a,b):
    commons_ = intersect_2(a,b)
    for elem in commons_:
        print(elem)
        a.replace(elem,"")
    return [commons_,a]

#Algorithm layer 2: extra ones that are nouns
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stug
def find_simps(a,b):
    v = intersect_and_remove(a,b)

    symptomss = v[0]
    print(symptomss)
    remaining_words = v[1]
    print(remaining_words)
    tokenized = nltk.word_tokenize(remaining_words)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    print(nouns)
    for noun in nouns:
        symptomss.append(noun) 
    return symptomss
