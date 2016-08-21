with open('countingsheep.large') as file:
	cases = int(file.next())
	for case in xrange(cases):
		num = int(file.next())
		if num == 0:
			print "Case #%d: INSOMNIA" % (case + 1)
		else:
			cur = 0
			digits = set()
			while len(digits) < 10:
				cur = cur + num
				digits.update(int(digit) for digit in str(cur))
			print "Case #%d: %d" % (case + 1, cur)
