# coding=utf-8#!/usr/bin/python
import sys
import itertools
import math

file = open(sys.argv[1], 'r')
writeFile = open(str(sys.argv[2]), 'w')


def isPrime(num):
	if num < 1:
		return -1
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			return i
	return -1


def coinJam(N, J):
	C = 0

	dp = []
	for i in range(11):
		dp.append([0])

	for i in range(2, 11):
		dp[i][0] = i ** (N - 1) + i ** 0
		primeFlag = False
		divisors = [-1] * 11
		for base in range(2, 11):
			# check dp[base][-1] isPrime()
			divisor = isPrime(dp[base][0])
			if divisor != -1:  # is not a prime
				divisors[base] = divisor
			else:
				primeFlag = True
		# no prime in all-based
		if not primeFlag:
			num = len(dp[2]) - 1
			# convert dp[base][-1]  which is len(dp[base]) -1 into binary
			num_str = format(num, "b").zfill(N - 2)
			out = "1" + num_str + "1"  # padding
			C += 1
			output = out + " " + " ".join(str(x) for x in divisors[2:11]) + "\n"
			writeFile.write(output)
			print output
		# print out, divisors[2:11], C

	# first ele = 10001
	# for x in range(1,4):   # increment in 1xxx1  3 bits
	# 	for base in range(2, 11):
	# 		curLen = len(dp[base])	# find how many elements , let say return by recursion
	# 		for j in range(curLen):
	# 			currentBit = base**x    # 001 = 2, 010 = 4, 100 = 3
	# 			dp[base].append(dp[base][j] + currentBit)
	# print  dp
	# permutation in x-th bit
	for x in range(1, N - 1):  # increment in 1xxxx1  4 bits
		curLen = len(dp[2])  # find how many elements , let say return by recursion
		if C >= J:
			break
		for j in range(curLen):
			primeFlag = False
			divisors = [-1] * 11
			if C >= J:
				break
			for base in range(2, 11):
				currentBit = base ** x  # 001 = 2, 010 = 4, 100 = 3
				dp[base].append(dp[base][j] + currentBit)
				# check dp[base][-1] isPrime()
				divisor = isPrime(dp[base][-1])
				if divisor != -1:  # is not a prime
					divisors[base] = divisor
				else:
					primeFlag = True
			# no prime in all-based
			if not primeFlag:
				num = len(dp[2]) - 1
				# convert dp[base][-1]  which is len(dp[base]) -1 into binary
				num_str = format(num, "b").zfill(N - 2)
				out = "1" + num_str + "1"  # padding
				C += 1
				output = out + " " + " ".join(str(x) for x in divisors[2:11]) + "\n"
				writeFile.write(output)
				print output
			# print out, divisors[2:11], C


N = 16
J = 50

T = int(file.readline())
for i in range(T):
	n = file.readline()
	writeFile.write("Case #%i:\n" % (1))

	N, J = n.split()
	coinJam(N, J)

file.close()
writeFile.close()
