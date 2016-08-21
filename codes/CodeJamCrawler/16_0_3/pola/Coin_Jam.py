#!/usr/bin/env python3
import sys
import math

def toBase(s,b):
	r = s[::-1]
	result = 0
	for p in range(len(s)):
		result += int(r[p]) * (b ** p)
		
	return result

def divisor(n):
	for x in range(2,int(math.sqrt(n))+2):
		if (n % x) == 0:
			return x
	return 0

def solve(N,J):
	items = []
	for x in range( 2 ** (N-2)):
		pc = "1%s1" % (format(x,'0%db' % (N-2)))
		item = [ pc ]
		for b in range(2,11):
			inb = toBase(pc,b)
			divi = divisor(inb)
			if divi:
				item.append('%s' % divi)
			else:
				item = None
				break
		if item:
			items.append(item)

		if len(items) == J:
			break

	return items

cases = int(sys.stdin.readline())

for case in range(cases):
	line = sys.stdin.readline()[:-1].split(" ")
	N = int(line[0])
	J = int(line[1])
	print("Case #%d:" % (case+1))
	s = solve(N,J)
	for x in range(len(s)):
		print(" ".join([ "%s" % x for x in s[x]]))
