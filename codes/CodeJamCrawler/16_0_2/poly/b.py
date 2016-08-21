def solve(p):
	prev = p[0]
	count = 0
	for i in range(1, len(p)):
		c = p[i]
		if c != prev:
			count = count + 1
		prev = c
	if prev == '-':
		count = count + 1
	return count

T = input()
for i in range(T):
    p = raw_input()
    print "Case #%d: %s" % ((i+1), str(solve(p)))
