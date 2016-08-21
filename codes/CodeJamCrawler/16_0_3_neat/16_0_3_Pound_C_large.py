import os
from sys import *

T = int(stdin.readline())
for t in xrange(T):
	(N, J) = map(int, stdin.readline().split())
	print "Case #%d:" %(t+1)
	minnum = str(10**(N-1)+1)
	
	n = minnum
	ntotal = []
	while len(ntotal) < J:
		list = []
		# print n
		for i in xrange(2,11): # change to base 2 - 10
			num = int(n,i)
			for j in xrange(2,100):
				if num % j == 0:
					list.append(j)
					break	
				elif j == 99:
					i = 10
					break							
		if len(list) == 9:
			ntotal.append(n)			
			print num, " ".join(str(x) for x in list)
		# increase number by '10' in base 2
		n = bin(int(str(n),2)+int('10',2))[2:]				

	
