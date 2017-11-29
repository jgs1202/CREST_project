#coding:utf-8

import csv   #csvモジュールをインポートする
import numpy as np
from nltk.tokenize import word_tokenize
from operator import itemgetter

f = open('feature_words_all.csv', 'rt')
dataReader = csv.reader(f)
data = [ e for e in dataReader]
f.close()
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = data[i][j].lower()

merge=[]

wordList =[]
lines = len(data)
print(lines)
for i in range(lines):
    for j in range(len(data[i])):
            if data[i][j] not in wordList:
                if data[i][j] != None:
                    wordList.append(data[i][j])

wordList.sort
length = len(wordList)
# print(wordList)
for i in range(lines):
    for j in range(length):
        words=[]
        if wordList[j] in data[i]:
            if len(wordList[j]) != 0:
                words.append(wordList[j])
                for k in data[i]:
                    if len(k) != 0:
                        words.append(k)
                # print(words)
                # print(words)
                merge.append(words)
# print(merge)

# print('none =')
merge.sort(key=itemgetter(0))
# print(merge)
lenm = len(merge)
old = merge[0][0]
for i in range(1,lenm):
    try:
        if merge[i][0] == old:
            merge[i][0] = None
        else:
            old = merge[i][0]
    except:
        pass

# print(merge)

f=open('feature_tree_all.csv', 'w')
writer = csv.writer(f)
for i in merge:
    writer.writerow(i)
f.close()
