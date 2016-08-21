from math import sqrt
from itertools import count, islice

def isPrime(n):
	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def smallestDivisor(number):
	for i in xrange(2, number/2+1):
		if number%i == 0:
			return i

def prettyPrint(number, divisors):
	st = str(number)
	for div in divisors:
		st = st + " " + str(div)
	return st

def solve(N, J):
	found = 0
	for x in xrange(0, pow(2, N-2)):
		divisors = []
		st = "1" + str(bin(x)[2:].zfill(N-2)) + "1"
		for base in xrange(2, 11):
			based = int(st, base=base)
			if isPrime(based):
				break
			else:
				divisors.append(smallestDivisor(based))
		if len(divisors) == 9:
			found = found + 1
			print prettyPrint(based, divisors)
		if found == J:
			break


T = int(raw_input())

for i in xrange(1, T + 1):
  N, J = [int(s) for s in raw_input().split(" ")]
  print "Case #{}:".format(i)
  solve(N, J)