import csv   #csvモジュールをインポートする
import numpy as np
from nltk.tokenize import word_tokenize

f = open('sampletxt2.csv', 'rt')
dataReader = csv.reader(f)
data = [ e for e in dataReader]
f.close()
#print(data)
 #n行1列のテキスト行列
word_tokenize_list = word_tokenize(str(data))
print (word_tokenize_list)
