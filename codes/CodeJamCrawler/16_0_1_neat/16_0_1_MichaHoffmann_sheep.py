def getDigits(m):
	result = []
	while m > 0:
		result.append(m%10)
		m = (m - m%10)/10
	return result

def f(n):
	seenNumbers = set([])
	i = 1
	while len(seenNumbers) < 10:
		m = i*n
		seenNumbers = seenNumbers.union(set(getDigits(m)))
		i += 1
		if i > 10**(3*len(getDigits(n))):
			return "INSOMNIA"
	return m
		

t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	print "Case #{}: {}".format(i+1, f(n))

