from random import *

T = input()

#a = [-1]*2500
i = 1
ml = list()
while(T):
	N = input()
	a = [-1]*2500
	for j in xrange(2*N-1):
		l = raw_input().split(' ')
		#print l
		for k in l:
			if(a[int(k)]==0):
				a[int(k)] = 1
			else:
				a[int(k)] = 0

	for j in range(2500):
		if(a[j] == 0):
			ml.append(str(j))

	print 'Case #'+str(i)+': '+' '.join(ml)
	ml = list()
	i += 1
	T -= 1