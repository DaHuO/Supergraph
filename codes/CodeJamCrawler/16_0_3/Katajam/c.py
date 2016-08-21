# python 2.7

import itertools

SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def getCoins(x, j):
	coins = []
	cnt = 0
	a = itertools.product(['0', '1'], repeat = x-2)
	for i in a: 
		got = list(i); got.insert(0, 1); got.append(1)

		num = ''.join(map(str, got))
		ans = [num]
		for base in range(2, 11):
			number = int(num, base)
			for prime in SMALL_PRIMES:
				if number%prime == 0:
					ans.append(prime)
					break
					
			if len(ans) == 10: 
				coins.append(ans)
				cnt += 1
				break

		if cnt == j: return coins
	return coins

def solution(n, j):
	jamcoins = getCoins(n, j)
	for i in jamcoins:
		print ' '.join(map(str, i))

n = int(raw_input())
for i in range(n):
	data = raw_input().split()
	N, J = int(data[0]), int(data[1])

	print "Case #{}:".format(i+1)
	solution(N, J)


