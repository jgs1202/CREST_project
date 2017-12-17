import nltk
from nltk.tokenize import word_tokenize
import csv

f = open('../../ data/220text.csv', 'rt')
dataReader = csv.reader(f)
data = [ e for e in dataReader]
f.close()
print(data)
words = []
kind = []
List = []
length = len(data)
for i in range(length):
    data[i] = str(data[i])[2:-2]
    word = nltk.pos_tag(word_tokenize(data[i]))
    for j in word:
        if j[1][0] == 'V':
            kind.append(j)
    # kind = nltk.pos_tag(text)
# print(kind)
print(kind[1])
# for i in kind:
#     if i[1][0] == 'V':
#         print(i)
print(sorted(kind))
kind = sorted(kind)
length = len(kind)
for i in range(length):
    if i == 0:
        num = 1
        old = kind[i]
    if i != 0:
        if kind[i] == old:
            num += 1
            print('same')
        if kind[i] != old:
            List.append([kind[i-1][0], kind[i-1][1], num])
            old = kind[i]
            num = 1
print(List)

f = open('220verbs.csv', 'w')
writer = csv.writer(f)
for i in List:
    writer.writerow(i)
f.close()
