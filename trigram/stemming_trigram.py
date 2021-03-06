# -*- coding: utf-8 -*-


import re
import nltk
import string

def cleanhtmlfun(raw):
  cleanit = re.compile('<.*?>')
  text = re.sub(cleanit, '', raw)
  return text



f=open('wiki_00', "r",encoding="utf8")
raw=f.read()
raw=cleanhtmlfun(raw)

from nltk.tokenize import TreebankWordTokenizer
tbw=TreebankWordTokenizer()
tokens=tbw.tokenize(raw)
tokens = [''.join(c for c in s if c not in string.punctuation) for s in tokens]
tokens = [s for s in tokens if s]

from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("english")
tokens=[stemmer.stem(word) for word in tokens]




trigrams=nltk.ngrams(tokens,3)
fdist_trigrams=nltk.FreqDist(trigrams) 
unique_trigrams=fdist_trigrams.B()  #This gives the total number of trique unigrams





import matplotlib.pyplot as plt

Y = fdist_trigrams.values()
Y = sorted(Y, reverse=True)
X = range(len(Y))
plt.figure()
plt.loglog(X, Y)
plt.xlabel('Trigram')
plt.ylabel('Frequency')
plt.title('Trigram Frequencies')
plt.grid()
plt.show()

size=0
for freq in Y:
    size+=freq

count=0
most_freq_trigrams=0
corp_req=0.70*size
for freq in Y:
    count+=freq
    most_freq_trigrams+=1   #This gives the number of unique trigrams required to cover 70% of the corpus
    if count>=corp_req:
        break