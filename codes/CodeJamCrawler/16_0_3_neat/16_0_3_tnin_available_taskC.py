from sympy import isprime  # https://en.wikipedia.org/wiki/SymPy
primes=[2]
for i in range(3, 2**15-1, 2):
	if isprime(i): primes.append(i)

import sys
T = case = -1
file = open(sys.argv[1], 'r')

for x in file:
	case += 1
	if case==0:
		T = int(x)
		continue

	print 'Case #%d:' % case
	x = x.split(' ')
	N = int(x[0])
	J = int(x[1])
	done = 0

	candidate = (1L<<(N-1)) - 1
	while done < J:
		candidate += 2
		binc = bin(candidate)[2:]
		factors = []
		for b in range(2, 11):
			interpretation = int(binc, b)
			found = 0
			for p in primes:
				if interpretation % p == 0:
					found = p
					break
			if found==0: break
			factors.append(found)
		if len(factors) >= 9:
			print binc,
 			for f in factors: print str(f),
			print
			done += 1
	
	if case==T:
		break
