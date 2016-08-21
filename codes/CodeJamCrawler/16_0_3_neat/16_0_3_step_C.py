import os, sys
import itertools

T = int(input())

primes = set()
def isPrime(x):
  if x in primes:
    return x
  for i in primes:
    if not x % i:
      return None
  else:
    primes.add(x)
    return x

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return i
    return n

def firstDivisor(x):
	if isPrime(x):
		return None
	for p in primes:
		if x%p  == 0:
			return p
	return None

for t in range(T):
	res = "0"
	N,J = map(int,raw_input().strip().split(" "))
	
	print("Case #{0}:".format(t+1) )
	for c0 in itertools.product([0,1], repeat = N-2):
		l = list(c0)
		# print( " " + str(l) )
		
		isGood = True
		divisors = []
		for b in (2,3,4,5,6,7,8,9,10):
			v = b ** (N-1) + 1 
			weight = b ** (N-2)
			for c in l:
				v += c * weight
				weight /= b
			fd = largest_prime_factor( v)
			if fd == v:
				isGood = False
			else:
				divisors.append( fd )
			# print( " B: {0} V: {1} FD: {2}".format( b, v, fd ) )

		if isGood:
			full_number =  "1{0}1".format( "".join( [ str(x) for x in l ] ) )
			print ("{0} {1}".format( full_number, " ".join( [str(x) for x in divisors ] ) ) )
			J-=1

		if J == 0:
			break
				
		
