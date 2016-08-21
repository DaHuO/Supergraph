def xyz(x):
	return (True if x == '+' else False)
def solve(s):
	flipped = True
	counter = 0
	for i in range(len(s) - 1, -1, -1):
		if flipped ^ s[i]:
			flipped = not flipped
			counter += 1
	return counter
t = int(raw_input())
for i in range(t):
	s = map(xyz, raw_input())
	print "Case #%d: %d" % (i + 1, solve(s))