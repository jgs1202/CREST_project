import csv   #csvモジュールをインポートする
import numpy as np
from nltk.tokenize import word_tokenize

def to1Line():
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

    Line = []
    row = 0
    for i in range(lines):
        for j in range(length):
            try:
                Line.append(List[i][j])
            except:
                None

    f=open('1Line_Txt.csv', 'w')
    writer = csv.writer(f)#, lineterminator='\n')
    writer.writerow(Line)
    f.close()

    leng=len(Line)
    print(leng)
    LineSingle = []
    i=0
    j=0
    for i in range(leng):
        if (i%500 == 0):
            print("i = " + str(i))
        try:
            LineSingle.append(Line[i])
        except:
            None
        for j in range(leng):
            if i < j:
                try:
                    if(Line[i] == Line[j]):
                        del Line[j]
                        j -= 1
                except:
                    None
    f=open('1LineSingle.csv', 'w')
    writer = csv.writer(f)#, lineterminator='\n')
    writer.writerow(LineSingle)
    f.close()



if __name__ == "__main__":
    to1Line()
