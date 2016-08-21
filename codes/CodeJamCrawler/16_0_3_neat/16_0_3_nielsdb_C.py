from math import sqrt

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1)
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

primelist = list(sieve((2**18)))
primeset = set(primelist)
def is_prime(n):
    return n in primeset

divisors = {}
def divisor(n):
	if n in divisors:
		return divisors[n]
	index = 0
	while index < len(primelist) and primelist[index] < n:
		if n%primelist[index] == 0:
			divisors[n] = primelist[index]
			return primelist[index]
		index+=1

print "Case #1:"
nbCases = int(raw_input())
for caseNb in range(1,nbCases+1):
	N, J = map(int, raw_input().split(" "))

	jamcoinsfound = 0
	for i in range(2**(N-1), 2**N):
		if i % 2 == 0:
			continue

		iStr = "{0:b}".format(i)

		for base in range(2,11):
			cur = int(iStr, base)
			if is_prime(cur):
				break
		else:
			out = [iStr]
			for base in range(2,11):
				cur = int(iStr, base)
				out.append(str(divisor(cur)))
			if not "None" in out:
				jamcoinsfound+=1
				print " ".join(out)
		if jamcoinsfound == J:
			break
