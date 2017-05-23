from nltk.tokenize import RegexpTokenizer
import numpy
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

import nltk
import nltk.corpus




tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
doc_a = "Brocolli is Sidharth good to eat. My brother likes to eat good Sidharth brocolli, but not my mother."
doc_b = "My mother spends a lot Sidharth of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that Sidharth driving Sidharth may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform Sidharth well at school, but my mother Sidharth never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is Sidharth good for your Sidharth health." 

# compile sample documents into a list
doc=nltk.corpus.abc.raw()
doc_set=nltk.word_tokenize(doc)
#doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
lsamodel = gensim.models.lsimodel.LsiModel(corpus, num_topics=4, id2word = dictionary)
i=0
p=5
print(lsamodel.print_topics(num_topics=4, num_words=5))
print id
for topic in lsamodel.show_topics(num_topics=10, formatted=False):
        i = i + 1
        print "Topic #" + str(i) + ":",
        print dictionary[i],
        print "  "
        
      

