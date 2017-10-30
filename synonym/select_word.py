#coding:utf-8

import csv   #csvモジュールをインポートする
import numpy as np
from nltk.tokenize import word_tokenize

f = open('sampletxt.csv', 'rt')
g = open('sampletxt.csv', 'rt')
lines = len(f.readlines())
dataReader = csv.reader(g)
data = [ e for e in dataReader]
List =[[0] for n in range(lines)]
box =[[0] for n in range(lines)]
f.close()
g.close()
#words=np.zeros((lines,1), dtype=object)
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

def searchWrite():
    word="sample"
    word = input("Enter your serching word : ")
    WordF = word[0].upper()
    print("the first of word is ")
    print(WordF)
    Word = WordF + word[1:]
    wordBig = word.upper()
    serchList = np.zeros((200,5), dtype=object)
    SerchList = np.zeros((200,5), dtype=object)
    SERCHLIST = np.zeros((200,5), dtype=object)

    row = 0
    for i in range(lines):
        for j in range(length):
            try:
                if List[i][j] == word:
                    N=0
                    col = 0
                    for N in range(5):
                        if j-2+N > -1:
                            try:
                                serchList[row][N] = (List[i][j-2+N])
                            except:
                                None
                                col += 1
                    row += 1
            except:
                None
            # serchList[row][col] = (data[i][j])
            # col += 1
            # if ( data[i][j+1] is not None ):
            #     print("yes")
            #     serchList[row][col] = (data[i][j+1])
            #     col += 1
            # row += 1
    print(serchList)

    row = 0
    for i in range(lines):
        for j in range(length):
            try:
                if List[i][j] == Word:
                    N=0
                    col = 0
                    for N in range(5):
                        if j-2+N > -1:
                            try:
                                SerchList[row][N] = (List[i][j-2+N])
                            except:
                                None
                            col += 1
                    row += 1
            except:
                None
            # serchList[row][col] = (data[i][j])
            # col += 1
            # if ( data[i][j+1] is not None ):
            #     print("yes")
            #     serchList[row][col] = (data[i][j+1])
            #     col += 1
            # row += 1
#print(SerchList)

    row = 0
    for i in range(lines):
        for j in range(length):
            try:
                if List[i][j] == wordBig:
                    N=0
                    col = 0
                    for N in range(5):
                        if j-2+N > -1:
                            try:
                                SERCHLIST[row][N] = (List[i][j-2+N])
                            except:
                                None
                            col += 1
                    row += 1
            except:
                None
            # serchList[row][col] = (data[i][j])
            # col += 1
            # if ( data[i][j+1] is not None ):
            #     print("yes")
            #     serchList[row][col] = (data[i][j+1])
            #     col += 1
            # row += 1
#print(SERCHLIST)

    f = open(word+'.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(serchList.tolist())
    f.close()
    g = open(word+'_first_letter.csv', 'w')
    Writer = csv.writer(g, lineterminator='\n')
    Writer.writerows(SerchList.tolist())
    g.close()
    h = open(word+'_letter.csv', 'w')
    WRITER = csv.writer(h, lineterminator='\n')
    WRITER.writerows(SERCHLIST.tolist())
    h.close()

repeat = "y"
while repeat == "y":
    searchWrite()
    print ('Do you want to search a word again?')
    repeat = input('y/n : ')
