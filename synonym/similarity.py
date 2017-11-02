import csv
import nltk
from nltk.corpus import wordnet
import numpy as np

g = open('1LineSingle.csv', 'rt')
dataReader = csv.reader(g)
data = [ e for e in dataReader]
nList = []
nWord = []
aList = []
aWord = []
g.close()

lines = len(data[0])

length=0
for i in range(lines):
    try:
        nList.append(wordnet.synset(data[0][i]+'.n.01'))
        nWord.append(data[0][i])
    except:
        None
i=0
for i in range(lines):
    try:
        aList.append(wordnet.synset(data[0][i]+'.a.01'))
        aWord.append(data[0][i])
    except:
        None

nlen=len(nList)
alen=len(aList)
print(nlen)
print(alen)
Nlen = float(nlen)*float(nlen-1)/2
Alen = float(alen)*float(alen-1)/2
nSim = np.zeros((int(Nlen),3), dtype=object)
aSim = np.zeros((int(Alen),3), dtype=object)

print(Nlen)
print(Alen)

i=0
j=0
k=0
for i in range (10):#nlen):
    for j in range (100):#nlen):
        if i<j:
            nSim[k][0]=nWord[i]
            nSim[k][1]=nWord[j]
            nSim[k][2]=nList[i].wup_similarity(nList[j])
            k += 1

print(nSim[:100])


    # w1 = wordnet.synset('nuclei.n.01')
    # w2 = wordnet.synset('boat.n.01') # n denotes noun
    # print(w1.wup_similarity(w2))
