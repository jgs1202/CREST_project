import csv
import nltk
from nltk.corpus import wordnet

f = open("1Line.csv", 'rt')
g = open('1Line.csv', 'rt')
lines = len(f.readlines())
dataReader = csv.reader(g)
data = [ e for e in dataReader]
List =[[0] for n in range(lines)]
box =[[0] for n in range(lines)]
f.close()
g.close()

length=0
for i in range(lines):
    box[i]=str(data[i])
    box[i]=box[i][2:-2]
    List[i]=word_tokenize(box[i])
for i in range(lines):
    num = len(List[i])
    if i == 0:
        length = num
    elif num > length:
        length = num

def
    word ="sample"
    word = input ("Enter word which have synonym you want. ")
    for i in range(lines):
        for j in range(length)
            try:

    w1 = wordnet.synset('nuclei.n.01')
    w2 = wordnet.synset('boat.n.01') # n denotes noun
    print(w1.wup_similarity(w2))
