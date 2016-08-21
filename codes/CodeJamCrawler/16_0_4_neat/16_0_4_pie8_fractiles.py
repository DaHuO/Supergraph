#!/usr/bin/env python

def solve(K, C, S):
	i = 0
	sol = []

	if K == S:
		while i < K:
			sol.append(1+(i*pow(K,C-1)))
			i += 1

		return " ".join(map(str, sol))
	else:
		return "IMPOSSIBLE"

def main():
	testcase_nb = long(raw_input().strip())
	i = 1

	with open('fractiles.out', 'w') as outfile:
		while i <= testcase_nb:
			K, C, S = map(long, raw_input().strip().split(' '))
			tiles_list = solve(K, C, S)
			outfile.write("Case #%d: %s\n" % (i, tiles_list))
			i += 1

if __name__ == '__main__':
	main()
