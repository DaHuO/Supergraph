import os
import random
_mrpt_num_trials = 5 # number of bases to test
from random import randint
from fractions import gcd
from math import sqrt

def basen(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (basen(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def f(x):
	""" function for pollard's rho """
	return x**2 + 1

def factor(n,b):
	""" Factor using Pollard's p-1 method """

	a = 2;
	for j in range(2,b):
		a = a**j % n
	
	d = gcd(a-1,n);

	if 1 < d < n: return d;
	else: return -1;

def PollardRho(N):
	if N%2 == 0:
		return 2
	if N%3 == 0:
		return 3
	if N%5 == 0:
		return 5
	else:
	    x = random.randint(1, N-1)
	    y = x
	    c = 120
	    g = 1
	    while g==1:             
	            x = ((x*x)%N+c)%N
	            y = ((y*y)%N+c)%N
	            y = ((y*y)%N+c)%N
	            g = gcd(abs(x-y),N)
	    if g == N:
	    	return -1
	    return g
def isp(n):
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    #assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite


n = int(input())
for i in range(1, n+1):
	n, m = [int(s) for s in input().split(" ")]
	base2 = (pow(2,n-1))+1
	base2b= bin(base2)[2:]
	base3 = int((base2b),3)
	base4 = int((base2b),4)
	base5 = int((base2b),5)
	base6 = int((base2b),6)	
	base7 = int((base2b),7)
	base8 = int((base2b),8)
	base9 = int((base2b),9)
	base10 = int((base2b),10)	
	print("Case #{}:".format(i))
	while m:
		#print(str(base2)+" "+str(base5))
		if isp(base2) or isp(base3) or isp(base4) or isp(base5) or isp(base6) or isp(base7) or isp(base8) or isp(base9) or isp(base10):
			base2 = base2 + 2
			base2b= bin(base2)[2:]
			base3 = int((base2b),3)
			base4 = int((base2b),4)
			base5 = int((base2b),5)
			base6 = int((base2b),6)
			base7 = int((base2b),7)
			base8 = int((base2b),8)
			base9 = int((base2b),9)
			base10 = int((base2b),10)
			continue
		m = m - 1
		#print("counting")
		print("{} {} {} {} {} {} {} {} {} {}".format(bin(base2)[2:],PollardRho(base2),PollardRho(base3),PollardRho(base4),PollardRho(base5),PollardRho(base6),PollardRho(base7),PollardRho(base8),PollardRho(base9),PollardRho(base10)))
		base2 = base2 + 2
		base2b= bin(base2)[2:]
		base3 = int((base2b),3)
		base4 = int((base2b),4)
		base5 = int((base2b),5)
		base6 = int((base2b),6)
		base7 = int((base2b),7)
		base8 = int((base2b),8)
		base9 = int((base2b),9)
		base10 = int((base2b),10)
		
