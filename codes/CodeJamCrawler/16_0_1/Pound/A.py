
import os
from sys import *
				

T = int(stdin.readline())
for t in xrange(T):
	N = str(stdin.readline())	
	index = ['0','1','2','3','4','5','6','7','8','9']
	counter = 1
	res = 0
	while len(index) > 0:		
		num = str(counter*int(N)) 
		if int(num) == 0:
			res = 'INSOMNIA'
			break
		else:
			count = 0
			for n in num:
				count = count+1
				if n in index:
					index.remove(n)
					if len(index)==0:
						res = num
						break
				elif count == len(num):
					break
		counter += 1		

	print "Case #%d:" %(t+1), res

	
	
	
	
	
	
	
	