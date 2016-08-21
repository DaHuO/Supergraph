#!/usr/bin/env python
from string import maketrans

inp = "+-"
out = "-+"
trans = maketrans(inp, out)

t = int(raw_input())
for i in xrange(1, int(t) + 1):
	n = raw_input()
	stack = n
	count = 0
	ans=count
	while '-' in stack:
		target = stack.rfind('-')
		flip = stack[:target+1]
		left = stack[target+1:]

		#flip = flip[::-1]
		flip2 = flip.translate(trans)

		stack = flip2+left

		count += 1
		ans=count
	print "Case #{}: {}".format(i, ans)

