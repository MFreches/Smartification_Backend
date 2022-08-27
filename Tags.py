from ctypes import sizeof
import nltk
# nltk.download()
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from numpy.lib.type_check import real


def Tagsfunction(fname):
    sw = set(stopwords.words('english'))
    tosend = []
    tokenized = sent_tokenize(fname)
    print(tokenized)
    for i in tokenized:
        word_list = nltk.word_tokenize(i)
        word_list = [w for w in word_list if not w in sw]
        tagged = nltk.pos_tag(word_list, tagset="universal")
        a = []
        y = -1
        f = 0
        realWord = [item[0] for item in tagged]
        print("Words:")
        print(realWord)
        pos = [item[1] for item in tagged]
        print("POS: ")
        print(pos)
        for x in pos:
            y += 1
            if(x == "."):
                continue
            if(x == "NOUN"):
                a.append(y)
            if(x == "ADJ"):
                a.append(y)
            if(x == "NUM"):
                a.append(y)
                if(y+1 <= len(pos)):
                    y = y+1
                    a.append(y)
                    y = y-1
            if(x == "VERB"):
                a.append(y)

        while f < len(a):
            if realWord[a[f]] == 'would' or realWord[a[f]] == 'will' or realWord[a[f]] == 'Would' or realWord[a[f]] == 'Will' or realWord[a[f]] == 'have' or realWord[a[f]] == 'Have' or realWord[a[f]] == 'used' or realWord[a[f]] == 'Used' or realWord[a[f]] == 'want' or realWord[a[f]] == 'Want':
                f += 1
                continue
            if realWord[a[f]] in tosend:
                f += 1
                continue
            else:
                print("Added:" + realWord[a[f]])
                tosend.append(realWord[a[f]])
                f += 1
    print("Sending:")
    print(tosend)
    return tosend
