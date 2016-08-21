#!/usr/bin/python

import math
import sys

def to_base(n, b):
	if (b == 10):
		return n

	i = 0
	result = 0
	
	while n > 0:
		if (n % 10) > 0:
			result += b ** i
		i += 1 
		n /= 10
		
	return result


def eratostene(max):
	numeri = [False] * max

	numeri[0] = False
	numeri[1] = True


	for i in xrange(2,max):
		numeri[i] = True;

	for i in xrange(2, long(math.sqrt(max))):
		if (numeri[i] > 0):
			j = i*2
			while (j < max):
				numeri[j] = False;
				j += i

	primes = []

	for i in xrange(2,max):
		if (numeri[i] == True):
			primes.append(i);
		
		
	return primes
	
	
def solve(primes, number, current):
	global J
	
	if (J == 0):
		return;
	
	if (current >= len(str(number))-1):	
		solution = []
		for b in xrange(2,11):
			bnumber = to_base(number,b)
			found = False
			for p in primes:
				if bnumber <= p:
					break
				if bnumber % p == 0:
					solution.append(p)
					found = True
					break
			if (not found):
				break;
				
		if len(solution) == 9:
			sys.stdout.write("{}".format(number)),
			for s in solution:
				sys.stdout.write(" {}".format(s)), 
				
			sys.stdout.write("\n")
				
			J -= 1;
		return;
			
	solve(primes, number, current + 1)
	solve(primes, number + 10**current, current + 1)
				
	
N = 32
global J
J = 500



number = 10**(N-1) + 1	

primes = eratostene(100000)

print "Case #1:"
solve(primes, number, 1)

if (J > 0):
	print "ERRORE!"


