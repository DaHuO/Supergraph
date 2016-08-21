#!usr/bin/python
import math


def smallestdivisor(n):
	"""returns the smallest non-trivial divisor of n"""
	d = 2  # to begin
	while n % d != 0:
		d = d+1
	return d


def factors(n):
	"""returns the prime factorization of n"""
	if n == 1:
		return [ ]  # empty list
	else:
		p = smallestdivisor(n)
	return [p] + factors(n/p)

def baseConvert(coin, base):
	#base is 2, or 3, or 4,..., or 10
	lt = len(coin)
	sum = 0
	for i in xrange(0, lt):
		bt = int(coin[i])
		#print "bt: {}".format(bt)
		sum = sum +bt* base**(lt-(i+1))
		#print "sum: {}, basePowered: (base**(lt-i)): {}".format(sum, base**(lt-i))
	return sum



def leastDivisor(n):
	n = int(n)
	for i in xrange(2, n/2):
	#	print i
		if (n%i == 0):
			return i


def isPrime(n):
	if n==2 or n==3: return True
	if n%2==0 or n<2: return False
	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
		if n%i==0:
	        	return False
	return True


def containsPrime(lst):
	for i in lst:
		if isPrime(int(i)):
			return False
	return True


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, j = [int(s) for s in raw_input().split(" ")]
	c = 0
	start = 1+2**(n-1)
	coins=[]
	coinindex=0
	lst=[]
	mlst=[]
	smdlst=[]
	msmdlst=[]
	while (c<j):
		bb, ab = bin(start).split("b")
		index=0
		badCoin = False
		for k in xrange(2, 11):
#			print "listStatus: {}, k:{}".format(lst, k)
			if isPrime(baseConvert(ab, k)):
#				print "bad number, prime: {}\nlstStatus: {}".format(baseConvert(ab, k), lst)
		#		print "bad coin: {}".format(ab)
				badCoin = True
				lst=[]
				start = start + 2
				break
			lst.append(baseConvert(ab, k))
		if (not badCoin):
		#	print "good start:{}".format(start)
		#	print "good coin:{}".format(ab)
			badCoin = False
			start = start + 2
			coins.append(ab)
		#	print "coins:{}".format(coins)
			c = c + 1
#			print "*****************c {}*************".format(c)
			mlst.append(lst)
			for a in lst:
#				print a
				smdlst.append(leastDivisor(a))
#			print smdlst
			msmdlst.append(smdlst)
			smdlst=[]
			lst=[]
	print "Case #{}:".format(i)
	for x,y in zip(coins, msmdlst):
		print "{} {}".format(x, " ".join(map(str, y)))
