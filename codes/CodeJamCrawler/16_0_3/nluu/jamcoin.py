#!/usr/bin/python

import itertools
import math

primes = []

def convert_to_base(a, base):
	# print('before convert: ' + str(a))
	result = 0
	for i in range(0, len(a)):
		j = len(a) - i - 1
		if a[i] == 1:
			result += int(math.pow(base, j))
			# print('tmp res: ' + str(result) + ' with j: ' + str(j) + ' and i: ' + str(i))

	# print('converted: ' + str(result) + " in base: " + str(base))
	return result

def check_prime(n):
	if n in primes:
		return -1
	for i in range(2, int(math.sqrt(n))):
		if n % i == 0:
			return i
	primes.append(n)
	return -1

def check_coin(a):
	# print('check a:' + str(a))
	ret = []
	for i in range(2, 11):
		res = check_prime(convert_to_base(a, i))
		if res == -1:
			return None
		else:
			ret.append(res)

	return ret

def find_coins(n, j):
	lst = [''.join(seq) for seq in itertools.product('01', repeat=n-2)]
	lst_full = ['1' + a + '1' for a in lst]
	count = 0
	print("Case #1:")
	for k in lst_full:
		ret = check_coin([int(elem) for elem in list(k)])
		if ret is not None:
			for div in ret:
				k += ' ' + str(div)
			print k
			count += 1
			if count == j:
				break
	# print('count: ' + str(count))

if __name__ == '__main__':
	find_coins(16, 50)

