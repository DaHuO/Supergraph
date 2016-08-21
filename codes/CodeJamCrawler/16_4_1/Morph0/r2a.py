import itertools
import sys


def verify_result(result):
	if len(result) == 1:
		return True

	next_result = []

	for x in xrange(0, len(result), 2):
		a, b = result[x:x+2]
		if a == b:
			return False
		if (a == 'P' and b == 'R') or (a == 'R' and b == 'P'):
			next_result.append('P')
		elif (a == 'P' and b == 'S') or (a == 'S' and b == 'P'):
			next_result.append('S')
		elif (a == 'S' and b == 'R') or (a == 'R' and b == 'S'):
			next_result.append('R')
	return verify_result(next_result)


# p, r, s
def solve(n, r, p, s):
	possible_results = []

	for result in itertools.permutations(list('R' * r + 'P' * p + 'S' * s), 2 ** n):
		if verify_result(result):
			possible_results.append(result)

	if len(possible_results) == 0:
		return "IMPOSSIBLE"

	possible_results.sort()
	return "".join(possible_results[0])


for i in xrange(int(raw_input())):
	n, r, p, s = (int(x) for x in raw_input().split(" "))
	print "Case #{}: {}".format(i + 1, solve(n, r, p, s))