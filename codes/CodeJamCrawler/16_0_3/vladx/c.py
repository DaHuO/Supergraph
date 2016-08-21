import sys
import math
from multiprocessing import Process, Lock

sys.stdin.readline()
n,j = map(int, sys.stdin.readline().split())

precalc_powers = [[base**i for i in xrange(0, n)] for base in xrange(0, 11)]

def get_divisor(x):
	for i in xrange(2, int(math.sqrt(x)) + 2):
		if x % i == 0:
			return i
	return 1

def powmod(a, n, mod):
	res = 1
	while n:
		if n & 1:
			res *= a
		res %= mod
		a *= a
		a %= mod
		res %= mod
		n >>= 1
	return res

def is_prime(x):
	return powmod(3, x-1, x) == 1

print('Case #1:')

def solve_range(rstart, rend, j, lock):
	for x in xrange(rstart, rend):
		if j == 0: break
		binary_form = '1%s1' % (('{0:0%db}' % (n-2)).format(x))
		numbers = []
		for base in xrange(2, 11):
			number, i = 0, n-1
			for p in binary_form:
				if int(p) == 1: number += precalc_powers[base][i]
				i -= 1
			if is_prime(number):
				break
			numbers.append(number)
		if len(numbers)==9:
			divisors = map(lambda x: str(get_divisor(x)), numbers)
			lock.acquire()
			print('%s %s' % (binary_form, ' '.join(divisors)))
			lock.release()
			j -= 1

#solve_range(1, 2**(n-2))

T = 128
t = []
step = 2**(n-2) / T
lock = Lock()
for i in xrange(T):
	t.append(Process(target=solve_range, args=(1+i*step, 1+(i+1)*step, j, lock)))

for i in xrange(T):
	t[i].start()

for i in xrange(T):
	t[i].join()