import csv
import numpy as np
from operator import itemgetter

g = open('name of input data', 'rt')
dataReader = csv.reader(g)
data = [ e for e in dataReader]
length = len(data)
print(length)

for i in range(length):
    row=[]
    for j in range(100):
        try:
            if len(data[i][j]) != 0:
                row.append(data[i][j].upper())
        except:
            data[i] = row
            break



for i in range(length):
    if i%10000 == 0:
        print(i)
    try:
        searchData = data[i]
        if searchData in data[i+1:]:
            del data[i]
    except:
        pass

try:
    for i in range(length):
        row=[]
        for j in range(100):
            try:
                if len(data[i][j]) != 0:
                    row.append(data[i][j].lower())
            except:
                data[i] = row
                break
except:
    pass


data.sort(key=itemgetter(0))

f=open('name of output data', 'w')
writer = csv.writer(f)
for i in data:
    writer.writerow(i)
f.close()