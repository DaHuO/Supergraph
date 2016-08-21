num = input()
for case in range(1, num + 1):
	print "Case #{}:".format(case),
	s = raw_input()
	n = 0
	for i in range(1, len(s)):
		if s[i] != s[i-1]:
			n += 1
	if s[-1] == '-':
		n += 1
	print n
