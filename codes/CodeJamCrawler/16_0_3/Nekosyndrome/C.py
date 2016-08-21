import math
import random
import sys
from fractions import gcd

def check(n, a, s, d):
	x = pow(a,d,n)
	if x==1: return True
	
	for i in range(s):
		if pow(a, 2**i * d, n) == n-1:
			return True
	
	return False

def is_prime(x):
	if(x==2): return True
	if(x<2 or x%2==0): return False

	# x-1 = 2^s * d
	s = 0
	d = x-1
	while d%2 == 0:
		d >>= 1
		s += 1

	for i in range(40):
		a = random.randint(2,x-1)
		if not check(x, a, s, d) : return False
	return True

n=32
j=500
ar = [1] * (n+2)
ar2 = [1] * (n+2)
vis = {}

def check2():
	global ar
	global ar2
	for dd in range(2, 11):
		x = 0
		for i in range(1,n+1):
			x = x*dd + ar[i]
		ar2[dd] = x
		if ar2[dd]%2!=0 and ar2[dd]%3!=0 and ar2[dd]%5!=0 and ar2[dd]%7!=0 and ar2[dd]%11!=0: return False
		#if is_prime(x): return False
	return True

def fac(n):
	for i in range(2,15):
		if n%i==0:
			return i
	return -1

def dfs():
	global j
	global ar
	global ar2
	global vis

	while True:
		if j<=0: break
		
		#gen a number
		for i in range(2,n): ar[i] = random.randint(0,1)
		tmp = 0
		for i in range(2,n): tmp = tmp*10 + ar[i]
		tmp = str(tmp)
		if tmp in vis: continue
		vis[tmp] = True

		if check2():
			j -= 1

			for i in range(1,n+1): sys.stdout.write( str(ar[i]) )
			for dd in range(2,11):
				sys.stdout.write(" ")
				fac2 = fac(ar2[dd])
				sys.stdout.write( str(fac2) )
				assert(ar2[dd]%fac2 == 0)
			print("")
			sys.stderr.write(str(j))
			sys.stderr.write("\n")


print("Case #1:")
dfs()
