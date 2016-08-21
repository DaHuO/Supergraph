#!/usr/bin/python
import pdb
import os

def r(i, n):
	if type(n) == int:
		print 'Case #%d: %d' %(i+1, n)
	else:
		print 'Case #%d: INSOMNIA' % (i+1)
	return

T = input()
#print T
for i in range(T):
	N = input()
	#print N
	#pdb.set_trace()
	if N == 0:
		r(i, 'INSOMNIA')
		continue
	dig = range(10)
	ti = 1
	while True:
		#print 'N = ' + str(N*ti)
		for j in str(N*ti):
			#print 'removing ' + j
			if dig.count(int(j)) > 0:
				dig.remove(int(j))
		if len(dig) == 0:
			r(i, N*ti)
			break
		ti += 1

