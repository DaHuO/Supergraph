import os
from sys import *
import numpy

T = int(stdin.readline())
for t in xrange(T):
	S = str(stdin.readline())	
	# change - to 0, + to 1
	num = []
	for s in S:
		if s == '+':			
			num.append(1)
		elif s == '-':		
			num.append(0)
	num = numpy.asarray(num)	
	flip = 0
	while len(num) > 0:
		if num[len(num)-1] == 1:
			num = numpy.delete(num,len(num)-1)			
		elif num[len(num)-1]==0:
			num = ~num+2
			flip += 1		
	print "Case #%d:" %(t+1), flip
