#!/usr/bin/env python3

import sys

def number_to_digits(number):
	return set((int(x) for x in str(number)))

def count_sheep(n):
	if n == 0:
		return 'INSOMNIA'

	inc_n, last = 0, 0
	digits = set()
	while len(digits) < 10:
		inc_n = inc_n + n
		last = inc_n
		digits |= number_to_digits(inc_n)
	return last

if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		n = int(input())
		print('Case #', i+1, ': ', count_sheep(n), sep='')
