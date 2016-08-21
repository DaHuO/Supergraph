#!/usr/bin/env python3
import sys

def solve(w):

	d = []

	f = { 'Z': 0, 'W': 2,  'U': 4, 'X': 6, 'G': 8 }
	s = { 'O': 1, 'T': 3,  'F': 5, 'V': 7, }

	c = [ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" ]

	for m in [ f, s ]:
		for k,v in m.items():
			ocu = w.count(k)
			for cant in range(ocu):
				d.append("%s" % v)
				for x in c[v]:
					w = w.replace(x,"",1)
	if w:
		d.append( '9' * int(len(w)/4) )

	d.sort()
	return "".join(d)

cases = int(sys.stdin.readline())

for case in range(cases):
	w = sys.stdin.readline()[:-1]
	print("Case #%d: %s" % (case+1,solve(w)))
