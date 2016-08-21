import sys

def number_in_base(x,b,n):
	result = 1
	bb = b;
	for i in xrange(n-2):
		result += (bb if (1 << i) & x else 0)
		bb *= b
	result += bb
	return result

"""
finds smallest non-trivial possible divisor. For primes it returns 1
see https://en.wikipedia.org/wiki/Primality_test#Pseudocode
"""
def find_divisor(n):
	if n <= 3:
		return 1
	if n % 2 == 0:
		return 2
	if n % 3 == 0:
		return 3
	i = 5
	while i <= 1000000:
		if n % i == 0:
			return i
		i += 2
		if n % i == 0:
			return i
		i += 4
	return 1

cases = input()
for i in range(1,cases+1):
	print "Case #%d:"%i
	n,j=map(int, sys.stdin.readline().strip().split())
	already_found = 0
	for number_binary in xrange(0,2**(n-2)):
		divisors=[]
		x=0
		for b in range(2,11):
			x = number_in_base(number_binary, b, n)
			d = find_divisor(x)
			if d > 1:
				divisors.append(d)
			else:
				break
		if (len(divisors)==9):
			print x,
			for d in divisors:
				print d,
			print
			already_found += 1
		if (already_found >= j):
			break