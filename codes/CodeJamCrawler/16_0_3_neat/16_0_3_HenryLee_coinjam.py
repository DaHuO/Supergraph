import math
import random
import sys

def convert(num, base):
	string = []
	while num > 0:
		if num % 2 == 0:
			string.append(0)
		else:
			string.append(1)
		num /= 2

	string.reverse()

	ret = 0
	
	for e in string:
		ret *= base
		ret += e

	return ret

def check(num, div):
	for i in range(2, 11):
		print (convert(num, i) % div)

def gen_start(div):
	for i in xrange(0b1000000000000001, 0b1111111111111111, 2):
		found = 1
		for j in range(2, 11):
			if convert(i, j) % div != 0:
				found = 0
		if found == 1:
			print "found one! %d " % i
			return i

def gen_inc(div):
	start = div

	for i in xrange(start, 1000*1000*1000, 2):
		found = 1
		for j in range(2, 11):
			if convert(i, j) % div != 0:
				found = 0
				break;

		if found == 1:
			print "found one! %d " % i
			return i

def primality_test(n, k = 7):
	if n < 6:
		return [False, False, True, True, False, True][n]
	elif n & 1 == 0:
		return False
	else:
		s, d = 0, n - 1
		while d & 1 == 0:
			s, d = s + 1, d >> 1
		for a in random.sample(xrange(2, min(n - 2, sys.maxint)), min(n - 4, k)):
			x = pow(a, d, n)
			if x != 1 and x + 1 != n:
				for r in xrange(1, s):
					x = pow(x, 2, n)
					if x == 1:
						return False
					elif x == n - 1:
						a = 0
						break
				if a:
					return False
			return True

def trial_divisor(num):
	for i in xrange(2, 1000*1000):
		if num % i == 0:
			return i
	
	return 0

def gen_all():
	count = 0
	#for i in xrange(0b1000000000000001, 0b1111111111111111, 2):
	for i in xrange(0b10000000000000000000000000000001, 0b11111111111111111111111111111111, 2):
		found = 1

		for j in range(2, 11):
			c = convert(i, j)
			if (primality_test(c)):
				found = 0
				break

		if found == 1:
			divisors = [];
			for j in range(2, 11):
				c = convert(i, j)
				d = trial_divisor(c)
				if d == 0:
					found = 0
					break;
				else:
					divisors.append(d)

			if found == 0:
				continue

			if len(divisors) != 9:
				print "Error"

			print bin(i),
			for j in divisors:
				print j,
			print
				
			count += 1
			if count >= 500:
				break;

gen_all()
#gen_inc(23)
#gen_start(23)
#gen_all(33759, 1023)
#gen_all(35490, 1365)
#check(43690, 17)
#check(21845, 17)
