import sys
import re
import os

def GetRepr(x, base):
	ret = 0
	basePow = 1
	while (x):
		ret += (x & 1) * basePow
		basePow *= base
		x >>= 1
	return ret

def GetDivisor(n):
# Slow but good for checking
	i = 2
	while i*i <= n:
		if n%i==0:
			return i
		i += 1
	return 0 # no divisor -> possible prime

def gcd(a, b):
	while (b != 0):
		r = a % b
		a = b
		b = r
	return a

def g(x, n):
	return (x*x+1) % n

MAX_TRY = 100

def PollardRho(n):
	x = 2
	y = 2
	d = 1
	c = 0
	while d == 1 and c < MAX_TRY:
		c += 1
		x = g(x, n)
		y = g(g(y,n), n)
		dxy = x-y
		if (dxy < 0):
			dxy = -dxy
		d = gcd(dxy, n)
	if d == n or c==MAX_TRY: 
		return 0
	else:
		return d

def CoinToStr(c, nbit):
	s = ''
	bmask = 1<<(nbit-1)
	while bmask:
		if (c & bmask):
			s += '1'
		else:
			s += '0'
		bmask >>= 1
	return s

D = 10

def main():
	divisors = [0 for i in range(D+1)]

	T = int(input())
	for t in range(1, T+1):
		cs = 'Case #'+ str(t) +':'
		print(cs)

		N, J = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
#		N = 32 # 16 # 6
#		J = 500 # 50 # 3

		j = 0
		coinBitsStart = (1 << (N - 1)) + 1
		coinBitsEnd = 1 << N
		for i in range(coinBitsStart,coinBitsEnd, 2):
			bFoundPrime = 0
			b = 2
			while (b <= D and bFoundPrime==0):
				nBase = GetRepr(i, b)
				divisors[b] = PollardRho(nBase)
				if (divisors[b] == 0):
					bFoundPrime = 1
				b += 1

			if (bFoundPrime==0):
				s = CoinToStr(i, N)
				for b in range(2, D+1):
					s += ' ' + str(divisors[b])
				print(s)

				j += 1
				if (j == J):
					break

main()
