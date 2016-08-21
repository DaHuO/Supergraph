#!/usr/bin/env python
import re
t = int(raw_input())

for case in range(t):
	stack = raw_input()
	similars = re.findall('((?:\+)+|(?:\-)+)', stack)
	if '+' in similars[-1]:
		similars.remove(similars[-1])
	print "Case #{}: {}".format( case+1, len(similars) )
