def findDivisor(n):
	d = 2
	while d != n and d < 400:
		#print d
		if n % d == 0:
			return d
		else:
			d += 1
	return 0

def isJam(n):
	divisors = list()
	if n[len(n)-1] != '1':
		return (False, [])
	elif n[0] != '1':
		return (False, [])

	for base in range(2, 11):
		decimal = int(n, base)
		#print "TESTING n = %s" % n
		divisor = findDivisor(decimal)
		#print "BASE %d --> Div : %d" % (base, divisor)

		if divisor:
			divisors.append(str(divisor))
			continue
		else:
			return (False, [])
	return (True, divisors)

def increment_binary_string(s):
	return '{:04b}'.format(1 + int(s, 2))


# Number of test cases
t = int(raw_input())

for i in xrange(1, t+1):
	first = False
 	n, j = [int(s) for s in raw_input().split(" ")]
 	result = []
 	divisors = []

	binary = '1' + "".join(['0' for z in range(0,n-2)]) + '0'
	x = binary
 	for j in xrange(1, j+1):
 		while True:
 			x = increment_binary_string(x)
 #			print x
	 		jam = isJam(x)
	 		if jam[0] is True:
	 			if not first:
	 				first = True
	 				print "Case #{}:".format(str(i))
				print "{} {}".format(str(x), " ".join(jam[1]))
				#decimal += 1
				break 