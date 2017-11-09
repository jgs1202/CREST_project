import csv   #csvモジュールをインポートする
import numpy as np

def search_dup():
    f = open('feature_words.csv', 'rt')
    g = open('feature_words.csv', 'rt')
    lines = len(f.readlines())
    dataReader = csv.reader(g)
    data = [ e for e in dataReader]
    List =[]
    box =[[0] for n in range(lines)]
    f.close()
    g.close()
    print(lines)
    i = 0
    j = 0
    #print(data)
    for i in range (lines):
        for j in range (lines):
            if i < j:
                if data[i] == data[j]:
                    print("oh")
                    print(i)
                    print(j)
                    List.append(data[i])
    print (List)
    f=open('duplicate_words.csv', 'w')
    writer = csv.writer(f)#, lineterminator='\n')
    writer.writerow(List)
    f.close()


if __name__ == "__main__":
    search_dup()
