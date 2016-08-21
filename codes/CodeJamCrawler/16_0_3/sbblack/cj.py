import sys, os

from fractions import gcd
infile = r'c:\cj2016\in.txt'

inf = open(infile,'r')
otf = open(r'c:\cj2016\out.txt','w')


import random

def brent(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:             
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break
         
        return g    

def find_first_factor(num):
	i = 2
	while (True):
		if num % i == 0:
			return i
		i += 1

def rabinMiller(num):
	# Returns True if num is a prime number.

	s = num - 1
	t = 0
	while s % 2 == 0:
		# keep halving s while it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		t += 1

	for trials in range(5): # try to falsify num's primality 5 times
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (num - 1):
				if i == t - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True


def isPrime(num):
	# Return True if num is a prime number. This function does a quicker
	# prime number check before calling rabinMiller().

	if (num < 2):
		return False # 0, 1, and negative numbers are not prime

	# About 1/3 of the time we can quickly determine if num is not prime
	# by dividing by the first few dozen prime numbers. This is quicker
	# than rabinMiller(), but unlike rabinMiller() is not guaranteed to
	# prove that a number is prime.
	lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

	if num in lowPrimes:
		return True

	# See if any of the low prime numbers can divide num
	for prime in lowPrimes:
		if (num % prime == 0):
			return False

	# If all else fails, call rabinMiller() to determine if num is a prime.
	return rabinMiller(num)


nocase = int(inf.readline())
otf.write('Case #1:\n')
for i in range(1,nocase+1):

	N, J = inf.readline().split(' ')
	
	N=int(N.strip())
	J= int(J.strip())
	jcount = 0
	
	n = 0
	while (True):
		numstr = "{0:0" + str(N-2) + "b}"
		testnums = '1' + numstr.format(n) + '1'

		foundprime = False
		for b in range(2,11):
			if isPrime(int(testnums,b)):
				foundprime = True
				break
		
		if not foundprime:
			otf.write(testnums)
			print 'j= ' + str(jcount)
			print testnums			
			for b in range(2,11):
				print 'factoring ' + str(int(testnums,b))
				otf.write(' ' + str(brent(int(testnums,b))))
				print 'done factoring'
			jcount += 1
			
			if jcount == J:
				break
			else:
				otf.write('\n')
		n += 1
			
	#otf.write('Case #' + str(i) + ': ' + str(x) + '\n')

inf.close()
otf.close()


# find right most -
# if left most is -, flip and recurse
# if left most is +, flip all left +'s, flip to right most - and recurse