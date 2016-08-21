# Python 2.7.11 :: Anaconda 2.5.0 (64-bit)
import sys
import copy

def result(p):
	if len(p)==0:
		return 0
	else:
		while len(p)>0 and p[-1]==1:
			p=p[:-1]
		add=0
		while len(p)>0 and p[-1]==-1:
			p=p[:-1]
			add=1
		return add+result([-1*x for x in p])

cases = input()
i=1
for line in sys.stdin:
	pancakes=line.strip()
	pancakes = list(1 if x=='+' else -1 for x in pancakes)
	print "Case #%d: %d" % (i,result(pancakes))
	i+=1