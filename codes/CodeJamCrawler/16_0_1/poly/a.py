def solve(n):
	found = set()
	tmp = n
	ok = False
	for i in range(1, 10000):
		s = str(tmp)
		for c in s:
			found.add(c)
		if len(found) == 10:
			ok = True
			break;
		tmp = tmp + n
	if not ok:
		return "INSOMNIA"
	return tmp

T = input()
for i in range(T):
    n = input()
    print "Case #%d: %s" % ((i+1), str(solve(n)))
