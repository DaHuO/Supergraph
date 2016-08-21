#!/usr/bin/python

from sys import stdin,stdout,stderr,exit

def run(S):
	total_height = len(S)

	def optimise_flips(bottom, target_side = True):
		i = bottom
		while i > 0 and S[i-1] == target_side:
			i = i-1

		if i > 0:
			return 1 + optimise_flips(i-1, not target_side)
		else:
			return 0

	return optimise_flips(total_height)

ncases = int(stdin.readline())

for case in range(1, ncases + 1):
	S = [x=='+' for x in stdin.readline().strip()]
	answer = run(S)
	stdout.write('Case #%u: %u\n' % (case, answer))
