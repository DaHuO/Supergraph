from itertools import count
from math import sqrt
import pickle

MAX_PRIME = 3333333333333334
KNOWN_PRIMES = [2]
try:
	for x in count(3):
		if x == MAX_PRIME:
			break
		is_prime = True
		if len(KNOWN_PRIMES) != 0 and x <= KNOWN_PRIMES[-1]:
			continue

		for possible_devisor in KNOWN_PRIMES:
			if x % possible_devisor == 0:
				is_prime = False
				break

		if is_prime:
			#print x
			KNOWN_PRIMES.append(x)

		if len(KNOWN_PRIMES) % 1000 == 0:
			print KNOWN_PRIMES[-1]

	print len(KNOWN_PRIMES)

	
finally:
	with open(r"D:\Code Jam 2016\Coin\primes.p", "wb") as fd:
		pickle.dump(KNOWN_PRIMES, fd)


