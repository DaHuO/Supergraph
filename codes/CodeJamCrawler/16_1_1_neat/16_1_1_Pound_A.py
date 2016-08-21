import os
from sys import *

T = int(stdin.readline())

for t in xrange(T):
	S = str(stdin.readline())	
	for s in xrange(len(S)):
		if s == 0:
			res = [S[0]]
		elif s!=0 and S[s]!='\n':
			if S[s] >= res[0]:
				res = [S[s]]+res
			elif S[s] < res[0]:
				res = res+[S[s]]	
	
	print "Case #%d:" %(t+1), "".join(str(x) for x in res)
