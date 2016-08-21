#!/usr/bin/env python3
import sys

def solve(S):
	c = list(S[0])
	j = list(S[1])
	a = [ [], [] ]
	for i in [ 0, 1]:
		for x in range(len(c)):
			if S[i][x] == "?":
				a[i].append(x)

	dife = ( 1000000 , [], [])
	formC = "%%0%dd" % len(a[0])
	formJ = "%%0%dd" % len(a[1])
	for cN in range( 10 ** len(a[0])):
		for jN in range( 10 ** len(a[1])):
			cS = formC % cN
			jS = formJ % jN
			for i in range(len(a[0])):
				c[a[0][i]] = cS[i]
			for i in range(len(a[1])):
				j[a[1][i]] = jS[i]

			d = abs( int("".join(c)) - int("".join(j)) )
			if d < dife[0]:
				dife = ( d , c[:], j[:])
			elif (d == dife[0]) and ( c < dife[1] ):
				dife = ( d , c[:], j[:])
			elif (d == dife[0]) and ( dife[1] == c ) and ( j < dife[2] ):
				dife = ( d , c[:], j[:])
		
	return ["".join(dife[1]), "".join(dife[2])]

cases = int(sys.stdin.readline())

for case in range(cases):
	S = sys.stdin.readline()[:-1].split(" ")
	print("Case #%d: %s" % (case+1,' '.join(solve(S))))
