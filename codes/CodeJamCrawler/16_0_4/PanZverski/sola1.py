tests = input()
for test in range(1, tests + 1):
	k, c, s = map(int, raw_input().split())
	s = ' '.join(map(str, range(1, s + 1)))
	print "Case #%d: %s" % (test, s)
