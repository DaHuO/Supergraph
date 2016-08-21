#!/usr/bin/python

def comp (n):
	seen = set()
	i = 1
	while True:
		r = i*n
		s = str(r)
		for c in s:
			seen.add(c)
		if len(seen) == 10:
			return r
		i += 1

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input())  # read a list of integers, 2 in this case
	if(n == 0):
		print "Case #{}: ".format(i) + "INSOMNIA"
	else:
		print "Case #{}: {}".format(i, comp(n))
	# check out .format's specification for more formatting options



