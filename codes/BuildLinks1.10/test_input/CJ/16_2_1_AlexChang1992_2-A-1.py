import numpy as np
from numpy.linalg import lstsq

digitsStr = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
digits = [i for i in xrange(10)]
matrix = [[0 for j in xrange(10)] for i in xrange(26)]

for i, s in enumerate(digitsStr):
	for c in s:
		matrix[ord(c)-ord('A')][i]+=1

'''
for i in xrange(26):
	for j in xrange(10):
		print matrix[i][j],
	print ''
'''

matrix = np.array(matrix)
T = int(raw_input())
for k in xrange(T):
	tmp = raw_input()
	b = [0 for i in xrange(26)]
	for c in tmp:
		b[ord(c)-ord('A')]+=1
	b = np.array(b)
	s = ''
	l = list(lstsq(matrix, b.T)[0])
	# print l
	for i, n in enumerate(l):
		nI = int(round(n))
		while nI > 0:
			s+=chr(ord('0')+i)
			nI-=1
	print "Case #{}: ".format(k+1)+s
