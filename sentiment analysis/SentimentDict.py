#Sentiment dictionary
import re



def readFiles(sentimentDictionary):

    posDictionary = open('../Corpora/positive-words.txt', 'r', encoding="ISO-8859-1")
    posWordList = re.findall(r"[a-z\-]+", posDictionary.read())

    negDictionary = open('../Corpora/negative-words.txt', 'r', encoding="ISO-8859-1")
    negWordList = re.findall(r"[a-z\-]+", negDictionary.read())

    for i in posWordList:
        sentimentDictionary[i] = "+"
    for i in negWordList:
        sentimentDictionary[i] = "-"
