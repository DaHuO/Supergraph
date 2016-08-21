import math
from itertools import product

def any_base(num, base):
	val = 0
	num = num[-1::-1]
	for i in xrange(len(num)):
		if num[i] == '1':
			val += base ** i
	return val

def is_prime(num):
	return num % 2 != 0 and all(num % i for i in xrange(3, int(math.ceil(math.sqrt(num))), 2))

def find_divisor(num):
	for i in xrange(2, num):
		if num % i == 0:
			return i

t = input()
n, j = map(int, raw_input().split())
c = map(lambda x: str(1) + "".join(x) + str(1), product('01', repeat = n - 2))

jams = 0

print "Case #1:"
#print c

for i in c:
	#print i
	flag = 1
	if jams == j:
		break
	for base in xrange(2, 11):
		if is_prime(any_base(i, base)):
			flag = 0
			break
	if flag == 1:
		print i,
		for base in xrange(2, 10):
			print find_divisor(any_base(i, base)),
		print find_divisor(any_base(i, 10))
		jams += 1
