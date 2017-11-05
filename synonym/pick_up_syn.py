import csv
import numpy as np
from operator import itemgetter

g = open('wup_similarity.csv', 'rt')
dataReader = csv.reader(g)
data = [ e for e in dataReader]
length = len(data)
List = []
row = 0
i=0
for i in range(length):
    name1 = data[i][0]
    name2 = data[i][1]
    f1 = data[i][0][0]
    f2 = data[i][1][0]
    Name1 = f1.upper() + name1[1:]
    Name2 = f2.upper() + name2[1:]
    if (name1 != name2) and (Name1 != Name2):
        List.append(data[i])

print(List)
