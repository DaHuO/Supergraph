#/usr/bin/env python3

import sys

def all_happy(pancakes):
	return sum(pancakes) == len(pancakes)

def unhappy(pancakes):
	return any((x == -1 for x in pancakes))

def flip(pancakes):
	return [-x for x in pancakes[::-1]]

# Ignore happy pancakes on the bottom
def mixed_top(pancakes):
	n = len(pancakes)
	while pancakes[n - 1] == 1:
		n -= 1
	return pancakes[:n]

def make_happy(pancakes):
	nflips = 0
	while unhappy(pancakes):
		pancakes = mixed_top(pancakes)
		i = 0
		while pancakes[i] == 1:
			i += 1
		if pancakes[-1] != pancakes[0]: # +- case
			# Just flip top pancakes
			pancakes = flip(pancakes[:i]) + pancakes[i:]
		else:
			pancakes = flip(pancakes)
		nflips += 1

	return nflips

if __name__ == '__main__':
	for i in range(int(input())):
		pancakes = [1 if x == '+' else -1 for x in sys.stdin.readline()[:-1]]
		print('Case #{}: {}'.format(i + 1, make_happy(pancakes)))

