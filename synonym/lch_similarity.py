import csv
import nltk
from nltk.corpus import wordnet
import numpy as np
from operator import itemgetter

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
        nList.append(wordnet.synset(data[0][i]+'.n.02'))
        nWord.append(data[0][i])
        nList.append(wordnet.synset(data[0][i]+'.n.03'))
        nWord.append(data[0][i])
    except:
        None
# i=0
# for i in range(lines):
#     try:
#         aList.append(wordnet.synset(data[0][i]+'.a.01'))
#         aWord.append(data[0][i])
#         aList.append(wordnet.synset(data[0][i]+'.a.02'))
#         aWord.append(data[0][i])
#         aList.append(wordnet.synset(data[0][i]+'.a.03'))
#         aWord.append(data[0][i])
#     except:
#         None

nlen=len(nList)
#alen=len(aList)
print(nlen)
#print(alen)
Nlen = float(nlen)*float(nlen-1)/2
#Alen = float(alen)*float(alen-1)/2
nSim = np.zeros((int(Nlen),3), dtype=object)
#aSim = np.zeros((int(Alen),3), dtype=object)
# nlen = 10
print(Nlen)
#print(Alen)
i=0
j=0
k=0
for i in range (nlen):
    for j in range (nlen):
        if i<j:
            similar = nList[i].wup_similarity(nList[j])
            if similar > 0.2:
                nSim[k][0]=nWord[i]
                nSim[k][1]=nWord[j]
                nSim[k][2]=similar
                k += 1
                if k % 10000==0:
                    print(k)
print(nSim[:100])
nosim=nSim.tolist()
nosim.sort(key=itemgetter(2), reverse=True)

# i=0
# j=0
# k=0
# for i in range (100):#alen):
#     for j in range (100):#alen):
#         if i<j:
#             aSim[k][0]=aWord[i]
#             aSim[k][1]=aWord[j]
#             aSim[k][2]=str(aList[i].wup_similarity(aList[j]))
#             k = k + 1
#             if k % 10000==0:
#                 print(k)
# adsim=aSim.tolist()
# print(aSim.shape)
#print(adsim)

f=open('lch_similarity.csv', 'w')
writer = csv.writer(f)
for i in nosim:
    writer.writerow(i)
f.close()
