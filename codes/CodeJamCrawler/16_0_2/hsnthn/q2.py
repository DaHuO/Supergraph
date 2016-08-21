def re(l, n):
	for i in xrange(n+1):
		if l[i] == '-':
			l[i] = '+'
		else:
			l[i] = '-'

def solve(s):
	l = list(s)

	c = 0

	for i in reversed(xrange(len(l))):
		if l[i] == '-':
			re(l, i)
			c += 1

	return c

inf = open("input.txt", "r")
outf = open("output.txt", "wr")

t = inf.readline().rstrip()

for i in xrange(1, int(t)+1):
	s = inf.readline().rstrip()
	r = solve(s)
	print s, r
	outf.write("Case #%d: %s\n" % (i, r))

inf.close()
outf.close()



"""
-+-+

+-+-
-+-+
+-++
-+++
++++

--+-
++-+
--++
++++
"""

