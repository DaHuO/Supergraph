def sleep(n):
	a = int(n)
	count = 1
	numbers = [0,1,2,3,4,5,6,7,8,9]
	x = True
	if n == 0:
		return "INSOMNIA"
	while x:
		current = [int(d) for d in str(a)]
		for digit in current:
			if digit in numbers:
				numbers.remove(digit)
		if not numbers:
			x = False
			return a
		count += 1
		a = n*count

t = int(raw_input())
for i in xrange(1, t + 1):
	n = int(raw_input())
	print "Case #{0}: {1}".format(i, sleep(n))