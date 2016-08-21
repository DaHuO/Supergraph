#! /usr/bin/env python

import sys, getopt
from collections import defaultdict as dd

#######################
## I/O functions begin
def processInput():
	# yields test cases
	T = int(raw_input())
	for i in range(T):
		N, J = map(int, raw_input().split())
		yield (N,J)
	return


def writeOutput(results):
	for result in results:
		print result
	return

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

P = {i for i in primes(2**16)}


def string_base(s, k):
	total = 0
	for c in s:
		total *= k
		total += int(c)
	return total

## I/O functions begin
#######################
def check_string(s, N):
	if len(s) != N or s[0] != "1" or s[-1] != "1":
		return False
	L = []
	for k in range(2, 11):
		#print k
		x = string_base(s,k)
		if x in P:
			return False
		else:
			done = False
			for p in P:
				if x % p == 0:
					L.append(p)
					done = True
				if done:
					break
			if not done:
				return False
	assert len(L) == 9, len(L)		
	return L

def check_coin(N, s, L):
	assert len(s) == N
	assert s[0] == "1"
	assert s[-1] == "1"
	for k in range(2,10):
		assert string_base(s, k) not in P

def ALGORITHM(test_case):
	N, J = test_case
	old_j = J
	outputs = []
	x = 2**(N-1) + 1
	while True:
		s = bin(x)[2:]
		L = check_string(s, N)
		if L:
			#print s, L
			check_coin(N, s, L)
			outputs.append((s, L))
			J -= 1
		if J == 0:
			break
		x = x + 2
	assert len(outputs) == old_j, len(outputs)
	result = ""
	for (s, L) in outputs:
		line = "\n"
		line += str(s)
		line += " " + " ".join(map(str, L))
		result += line
	return result

	
def basic_test():
	pass

def runAlgorithm():
	results = []
	for test_case in processInput():
		results.append(ALGORITHM(test_case))

	for i in range(len(results)):
		results[i] = "Case #" + str(i+1) + ": " + results[i] + "\n"

	writeOutput(results)

if __name__ == "__main__":
	basic_test()
	runAlgorithm()
