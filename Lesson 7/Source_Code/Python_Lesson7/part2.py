import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import trigrams
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

data = open("input.txt", "r")

tokens = []
while True:
    try:
        line = data.readline()
        if not line:
            break
        #tokens.append(nltk.word_tokenize(str(line)))
        print(ne_chunk(pos_tag(wordpunct_tokenize(line))))

    except UnicodeDecodeError:
        pass
tokens = sum(tokens, [])

#prints all tokens from file
#for w in tokens:
#    print(w)

## Part of Speech tagging
#print(nltk.pos_tag(tokens))

##Stemming
#sStemmer = SnowballStemmer('english')
#for w in tokens:
#    if w.isalpha():
#        print(sStemmer.stem(w))

## Lemmatizer
#lem = WordNetLemmatizer()
#for w in tokens:
#    if w.isalpha():
#        print(lem.lemmatize(w))

## Trigrams
#print(list(trigrams(tokens)))


data.close()