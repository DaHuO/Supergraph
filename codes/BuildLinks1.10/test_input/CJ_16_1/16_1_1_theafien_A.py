#-*- coding: utf-8 -*-


def solve(S):
	result = [S[0]]
	for x in S[1:]:
		if x >= result[0]:
			result.insert(0, x)
		else:
			result.append(x)

	return "".join(result)


def codejam():
	T = int(raw_input())
	i = 1
	while i <= T:
		S = str(raw_input())
		print "Case #%d: %s" % (i, solve(S))
		i += 1

codejam()