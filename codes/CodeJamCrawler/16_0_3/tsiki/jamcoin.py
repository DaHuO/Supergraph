
import sys
import math
import itertools
from collections import defaultdict

sys.stdin.readline().rstrip()

j, n = map(int, sys.stdin.readline().rstrip().split())

#num = 1 << n
#num += 1

num = [1] + [0]*(j-2) + [1]

def add(s):
	i = len(s) - 1
	while s[i] == 1:
		i -= 1
	s[i] = 1
	i += 1
	while i < len(s):
		s[i] = 0
		i += 1
	s[-1] = 1

def getdiv(numero):
	i = 2
	while i*i <= numero and i < numero and i < 1000:
		if numero % i == 0:
			return i
		i += 1
	return -1

tot = 0
print "Case #1:"
while tot < n:
	divs = []
	for base in xrange(2,11):
		curnum = int("".join(map(str, num)), base)
		d = getdiv(curnum)
		if d > 0:
			divs.append(d)
		else:
			divs = []
			break
	if len(divs) == 9:
		print "".join(map(str, num)), " ".join(map(str, divs))
		tot += 1
	add(num)
	
		











