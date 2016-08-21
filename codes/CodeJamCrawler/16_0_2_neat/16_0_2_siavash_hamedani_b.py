import sys
import itertools
import numpy as np

def solve(inp):
	inp = list(inp)
	if(inp==[]):return 0
	inp = map(lambda x:"+" if x=="-" else "-",inp)
	inp = inp[::-1]
	return 1+solve(itertools.dropwhile(lambda x:x=="+",inp[::-1]))



for i in range(int(sys.stdin.readline())):
	print "Case #%d: %s"%(i+1,solve(itertools.dropwhile(lambda x:x=="+",sys.stdin.readline()[:-1][::-1])))