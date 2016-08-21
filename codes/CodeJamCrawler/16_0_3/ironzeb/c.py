from __future__ import print_function

import sys

f = sys.stdin
T = int(f.readline())

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def not_prime(n, k=9):
	for i in range(2, min(n, k)):
		if n % i == 0:
			return i
	return False

def solve(N, J):
	# generate J jamcoins of length N
	minN, maxN = "1" + "0" * (N - 2) + "1", "1" * N
	min_nums = [int(n, i+2) for i, n in enumerate([minN] * 9)]
	max_nums = [int(n, i+2) for i, n in enumerate([maxN] * 9)]

	j = dict()
	k = 9
	nums = [n for n in min_nums]

	while True:
		while nums[0] < max_nums[0]:
			if all(not_prime(n, k) for n in nums):
				j[nums[-1]] = [not_prime(n, k) for n in nums]

			if len(j) >= J:
				return j

			s = baseN(nums[0] + 2, 2)
			for i in range(len(nums)):
				nums[i] = int(s, i+2)

		nums = [n for n in min_nums]
		k += 10

	# for i in range(int(min_nums[0]), int(max_nums[0]) + 1, 2):
	# 	s = str(baseN(i, 2))
	# 	foundPrime = False
	# 	for u in range(len(primes)):
	# 		base = u + 2
	# 		if int(s, base) in primes[u]:
	# 			foundPrime = True
	# 			break
	# 	if not foundPrime:
	# 		j.append(s)

	# 	if len(j) >= J:
	# 		return j

	return j

for t in range(1, T+1):
	N, J = map(int, f.readline().strip().split())
	ans = solve(N, J)
	print("Case #{}:".format(t))
	for j, v in ans.items():
		print(j, " ".join(map(str, v)))

