def observe_num(x,digits):
	while x > 0:
		digits[x%10] = 1
		x /= 10
	if sum(digits) == 10:
		return True
	return False

T = int(raw_input().strip())
for i in xrange(1,T+1):
	N = int(raw_input().strip())
	if N == 0:
		print "Case #" + str(i) + ": INSOMNIA"
		continue
	digits = 10*[0]
	s = N
	for j in xrange(100):
		if observe_num(s,digits):
			print "Case #" + str(i) + ": " + str(s)
			break
		s += N
	if sum(digits) != 10:
		print "Case #" + str(i) + ": INSOMNIA"
