# BCDdiagnoses
BCD Diagnoses , introducing a new and intuitive way of medical diagnosis
## Frontend
The design of the UI is an incredibly important aspect of any online software. The Homepage should be eye-catching, demonstrated by the hero slider and having the majority of the element on one window allows for a more lightweight and easily implemented with smartphone support. Media queries and the use of the viewport width allowed for responsive design, and many buttons and the "sticky navigation-bar" encourage the visitor to try out the application - and appealing to users is important for the frontend developer to ensure. Sleek effects such as parallax scrolling and the switching navigation-bar also help captivate the users, and mobile support widens the range of people willing to use our application. All this easily connects with the simply designed input form, intended for easy use for those in all ages. The use of modals also helps keeps the interface tidy, as well as being an effective method of giving out forms or information when connecting to the backend via flask.
## NLP
The NLP  (Natural Language Processing) element of out app was fairly difficult because the usual approach to NLP in an app like this is using a lot of training data, word2vec and a neural network. 
Unfortunately for us, collecting example data for each symptom would have taken  too long in the timeframe given. To combat this we used a range of elegant techniques to try and classify symptoms the best way possible.As well as this, I decided over using heavier methods such as word2vec, elmo and bert embeddings due to the speed and (graphical) processing power required to process so many repeats of these algorithms. This is more of a problem for us since we host it on a cloud server with limited processing power nonetheless.

### Latent Dirichlet Allocation
Latent Dirichlet Allocation is an amazing algorithm for many reasons. It is fast and finds the lnked topics of text in seconds. model that allows sets of observations to be explained by unobserved groups thus showing which parts of data are more or less similar and the variation between them. The LDA in our case was used to find the general relative topics by cutting out extras. Our LDA returns a symptom which is further cut down into the most similar (using Wu-palmer and cosine similarity) and we use this to boost speeds. 

### Wu-palmer similarity metric with WordNet
Wu-palmer is used to find the similarity between words. Usually similarity metrics such as cosine distance, siamese manhattan lstms and other measures are used to find the similarity between two sentences but Wu-palmer is knowledge based and used to find the the semantic (or meaning related) similarity between two words. This means that if someone uses words that are slightly different to exact language, the symptoms can still be correctly identified.

### Cosine similarity, 
We used cosine similarity combined with trigrams to scan over the text and identify symptoms which have mixed up words. Splitting a sentence into trigrams looks like this:

Initial sentence:
``` 
The quick brown fox jumps over the lazy dog
```
Into trigrams:
```
The quick brown, quick brown fox, brown fox jumps, fox jumps over. jumps over the, over the lazy, the lazy dog
```

Cosine similarity is a vector based algorithm. It starts by removing stopwords. Then it uses TF-IDF to find the resulant 
