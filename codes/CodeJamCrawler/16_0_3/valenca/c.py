from math import sqrt,ceil
from random import sample,seed
from pprint import pprint

def primes_sieve(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False
	
  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

				
T=input()
N,J=map(int,raw_input().split())

seed(0)

fin=[]

primes=primes_sieve(2**24)

print "Case #1:"

while(len(fin)<J):
	s='1' + "".join(sample((['0']*N+['1']*N),N-2))+'1'
	e=[s]
	for i in range(2,11):
		n = int(s,i)
		if n in primes:
			break
		for j in range(3,999,2):
			if n%j ==0:
				e.append(j)
				break
		if len(e)==10:
			if e not in fin:
				fin.append(e)

for e in fin:
	print "%s %d %d %d %d %d %d %d %d %d" % tuple(e)

