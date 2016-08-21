from math import sqrt; from itertools import count, islice

def is_prime(n):
	isPrime = True;
	for i in islice(count(2), int(sqrt(n)-1)):
		if not (n%i):
			isPrime = False
			break
	return (isPrime, i)



# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	N, J = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	n = N-2
	j = 0
	print "Case #{}:".format(i)                       
	for i in xrange(n**2):
		b = bin(i)[2:]
		l = len(b)
		b = str(0) * (n - l) + b
		s = "1" + b + "1"
		found = True
		f = []
		for x in xrange(9):
			y = x+2
			val = 0
			for p in xrange(N):
				val = val + int(s[(N-p)-1])*(y**p)
			(retVal, factor) = is_prime(val)
			if (retVal == True):
				found = False
	 			break
	 		else:
	 			f.append(str(factor))
	 	if (found == True):
	 		print "{} {}".format(s, ' '.join(f)) 
	 		j = j + 1
	 		if (j == J):
	 			break
	 
	# check out .format's specification for more formatting options