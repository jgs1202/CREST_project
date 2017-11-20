import os
import csv
from numpy.random import *


List = []
os.chdir("path to search-result")
for file in os.listdir():
	if (file != ".DS_Store") and (file != "result_stack.csv"):
		with open(file, 'rt') as f:
			dataReader = csv.reader(f)
			data = [ e for e in dataReader]
			print(file)
			for i in range(200):
				if data[i].count("0") == 5:
					break
				else:
					List.append(data[i])

print(List)

with open("result_stack.csv", 'w') as g:
	writer = csv.writer(g, lineterminator='\n')
	writer.writerows(List)
