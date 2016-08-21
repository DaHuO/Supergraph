#!/usr/bin/env python3.5

def majority(n):
	return n // 2 + 1

def solve():
	N = int(input())
	P = [int(i) for i in input().split()]
	result = ""
	members = sum(P)
	while members > 0:
		# next majority is either
		majority_1 = majority(members - 1)
		majority_2 = majority(members - 2)

		most = max(P)
		n_most = P.count(most)
		if n_most == 2 or n_most > 3:
			# remove 2
			for i in range(len(P)):
				if P[i] == most:
					P[i] -= 1
					result += chr(65 + i)
					break
			for i in range(len(P)):
				if P[i] == most:
					P[i] -= 1
					result += chr(65 + i)
					break
			members -= 2
		else:
			# remove 1
			for i in range(len(P)):
				if P[i] == most:
					P[i] -= 1	
					result += chr(65 + i)
					break
			members -= 1
		result += " "
	return result[:-1]

T = int(input())
for t in range(1, T+1):
	print("Case #{}: {}".format(t, solve()))

