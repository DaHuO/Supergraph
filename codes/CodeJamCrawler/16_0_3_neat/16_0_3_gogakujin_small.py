# coding: utf-8

import os, sys, re, string
import math,random

def is_prime(v):
	for i in xrange(2, int(math.sqrt(v)) + 1):
		if v % i == 0:
			return False
	return True

prime_cache = {}
def is_prime_c(v):
	if prime_cache.has_key(v):
		return prime_cache[v]
	prime_cache[v] = is_prime(v)
	return prime_cache[v]

def inter(n, bits, base):
	res, rate = 1, 1
	for i in xrange(n - 2):
		rate *= base
		res += ((bits >> i) & 1) * rate
	return res + rate * base

def search_divisor(v):
	res = []
	for i in xrange(2, int(math.sqrt(v))):
		if v % i == 0:
			res.append(i)
			if len(res) > 2:
				break
	return res
divisor_cache = {}
def search_divisor_c(v):
	if not divisor_cache.has_key(v):
		divisor_cache[v] = search_divisor(v)
	ary = divisor_cache[v]
	return ary[int(random.random() * len(ary))]

def solve(n, j):
	bits = 0
	res = []
	used = {}
	while len(res) < j:
		flag, table = True, [0] * 9
		for base in xrange(2, 11):
			value = inter(n, bits, base)
			if is_prime_c(value):
				flag = False
				break
			table[base - 2] = value
		if flag:
			bits_s = '1' + format(bits, "0%db" % (n - 2)) + '1'
			divisors = " ".join(map(lambda x: str(search_divisor_c(x)), table))
			if not used.has_key(divisors):
				res.append(bits_s + ' ' + divisors)
				used[divisors] = True
				#print "found %d %s %s" % (len(res), bits_s, divisors)
			#else:
			#	print "used %s %s" % (bits_s, divisors)
		bits = (bits + 1) & ((1 << (n - 2)) - 1)
	return res

def main():
	t = int(sys.stdin.readline())
	for i in xrange(1, t + 1):
		n, j = map(int, sys.stdin.readline().split(" "))
		print "Case #%d:" % i
		print "\n".join(solve(n, j))

if __name__ == '__main__':
	main()


