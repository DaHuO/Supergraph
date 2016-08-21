import numpy as np 
from collections import Counter
import string

# grab input
with open('A-large.in', 'r') as f:
	content = f.readlines()

T = int(content[0]) # of cases
data = [[val for val in line.split()] for line in content[1:]]

result = [] # list of results

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

M=0
for i in range(T):
	N = int(data[M][0])	
	row = data[M+1]
	row = map(int, row)
	
	ans = []
	
	while sum(row) > 0:

		i1 = row.index(max(row))
		row[i1] -= 1
		i2 = row.index(max(row))
		if 2*row[i2] > sum(row):
			row[i2] -= 1
			evac = alpha[i1] + alpha[i2]
		else:
			evac = alpha[i1]
		ans.append(evac)
	
	result.append(ans)



	
	M += 2; 


# print result


#write to output
with open('Alarge.txt','w+') as f:
	for count, num in enumerate(result):
		#f.write("Case #%i: %d\n" % (count+1, item for item in result[count]))	
		f.write("Case #%i: " % (count+1))
		for i in result[count]:
			f.write(i + " ")
		f.write("\n")
		