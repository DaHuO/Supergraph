#!/usr/bin/env python3
import functools
import sys

def count(x):
	return functools.reduce(lambda x,y: x + y , [ i[0] for i in x ] , 0)

def empty(x):
	return  count(x) == 0

def valid(x):
	for i in x:
		if (i[0] < 0):
			return False
		N = count(x)
		if N==0:
			return True
		if ((1.0 * i[0]) / N ) > .5:
			return False
	return True

def int2asc(i):
	return chr(ord('A')+i)
	
def solve(p):

	d = []
	N = len(p)
	x = []
	for i in range(len(p)):
		x.append( (p[i], i ))

	while not empty(x):
		x.sort(reverse=True)
		f = x[0]
		
		rem1 = [ ( f[0]-1, f[1]) ] + x[1:]
		rem2 = [ ( f[0]-2, f[1]) ] + x[1:]

		if valid( rem2 ):
			d.append( '%s%s' % (int2asc(f[1]),int2asc(f[1])))
# 			print('rem2', x, rem2, int2asc(f[1]), int2asc(f[1]))
			x = rem2
		elif valid( rem1 ):
			d.append( int2asc(f[1]) )
# 			print('rem1', x, rem1)
			x = rem1
		elif len(p) > 1:
			g = x[1]
			rem3 = [ ( f[0]-1, f[1]), ( g[0]-1, g[1]) ] + x[2:]
			if valid( rem3 ):
# 				print('rem3', x, rem3, int2asc(f[1]), int2asc(g[1]))
				d.append( "%s%s" % (int2asc(f[1]), int2asc(g[1])) )
				x = rem3


	return " ".join(d)

cases = int(sys.stdin.readline())

for case in range(cases):
	N = int(sys.stdin.readline()[:-1])
	P = [ int(i) for i in sys.stdin.readline()[:-1].split(' ')]
	print("Case #%d: %s" % (case+1,solve(P)))
