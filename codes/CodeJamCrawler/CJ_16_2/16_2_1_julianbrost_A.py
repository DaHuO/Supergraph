#!/usr/bin/env python3

import sys
from collections import defaultdict

magic = [
	('X', 'SIX', 6),
	('G', 'EIGHT', 8),
	('Z', 'ZERO', 0),
	('W', 'TWO', 2),
	('H', 'THREE', 3),
	('R', 'FOUR', 4),
	('O', 'ONE', 1),
	('F', 'FIVE', 5),
	('V', 'SEVEN', 7),
	('I', 'NINE', 9),
]

N = int(input())

def dbg(x):
	return {k: v for k, v in x.items() if v}

def solve(inp):
	char_counts = defaultdict(int)
	digit_counts = defaultdict(int)
	for c in inp:
		char_counts[c] += 1
	for c, s, d in magic:
		num = char_counts[c]
		#print(c, s, d, num, dbg(char_counts))
		for x in s:
			char_counts[x] -= num
			assert char_counts[x] >= 0
		digit_counts[d] += num
	for v in char_counts.values():
		assert v == 0
	return ''.join(str(x) * digit_counts[x] for x in range(10))

for n in range(N):
	print('Case #{}: {}'.format(n+1, solve(input())))
