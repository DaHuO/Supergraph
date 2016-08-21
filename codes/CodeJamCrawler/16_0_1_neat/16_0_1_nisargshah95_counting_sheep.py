T = input()

for i in xrange(T):

	N = input()

	if N == 0:
		print "Case #"+str(i+1)+": INSOMNIA"
		continue

	num = N

	digits = [False for j in xrange(10)]
	count = 0
	found = 0

	while True:

		for digit in map(int, list(str(num))):
			if digits[digit] == False:
				digits[digit] = True
				count += 1
				if count == 10:
					found = 1
					break

		if found: break
		num += N

	print "Case #"+str(i+1)+": "+str(num)