c = input()

case = 1
while case <= c:
	s = raw_input()
	res = s[0]
	for i in xrange(1, len(s)):
		if ord(s[i]) >= ord(res[0]):
			res = s[i] + res
		else:
			res += s[i]
	
	print "Case #" + str(case) + ": " + res
	case += 1