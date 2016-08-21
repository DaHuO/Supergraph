import sys

def solve(k, c, s):
	if s < (k / 2) :
		return "IMPOSSIBLE"

	if c == 1 and s < k :
		return "IMPOSSIBLE"

	result = ""

	if c == 1 :
		for i in range(k) :
			result += str(i + 1) + " "
	else :
		base = pow(k, c - 1)
		for i in range(k / 2) :
			pos = base * (i * 2) + i * 2 + 2
			result += str(pos) + " "
		if k % 2 == 1 :
			result += str(pow(k, c))

	return result

rl = lambda: sys.stdin.readline()
T = int(rl())

for i in range(T):
	seq = str(rl())
	l = seq.split()
	
	k = int(l[0])
	c = int(l[1])
	s = int(l[2])

	result = solve(k, c, s)
	print "Case #%d: %s" % (i + 1, result)
