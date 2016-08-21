
from primefac import *
import numpy as np
from stopit import ThreadingTimeout as Timeout, threading_timeoutable as timeoutable  #doctest: +SKIP



def fac(x):
	return pollardRho_brent(x)

def randomvec(n):
	v=  np.random.randint(2,size=n)
	v[0] = v[-1] = 1
	return ''.join(str(x) for x in v)

def get_numbers(vec): 
	return [int(vec,b) for b in range(2,11)]

def get_factors(ivec):
	with Timeout(0.1) as timeout_ctx:
		return [fac(x) for x in ivec]
	return []

def all_not_prime(ivec):
	return all(not isprime(x) for x in ivec[::-1])

n = int(raw_input())
m = int(raw_input())



ans = {}


print 'Case #1:'
for i in range(m):
	while True:
		vec = randomvec(n)
		if vec not in ans:
			xs = get_numbers(vec)
			if all_not_prime(xs):
				ans[vec]=1
				factors = get_factors(xs)
				if factors:
					print vec,' '.join(map(str,factors))
					break
