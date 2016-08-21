# -*- coding: utf-8 -*-

from collections import Counter as C

def drop(counter, component):
	for letter in component:
		counter[letter] -= component[letter]

def solve(s):
	candidates = []
	counter = C(s)
	while counter['Z']:
		candidates.append(0)
		component = C('ZERO')
		drop(counter, component)
	while counter['W']:
		candidates.append(2)
		component = C('TWO')
		drop(counter, component)
	while counter['X']:
		candidates.append(6)
		component = C('SIX')
		drop(counter, component)
	while counter['G']:
		candidates.append(8)
		component = C('EIGHT')
		drop(counter, component)
	while counter['S']:
		candidates.append(7)
		component = C('SEVEN')
		drop(counter, component)
	while counter['U']:
		candidates.append(4)
		component = C('FOUR')
		drop(counter, component)
	while counter['H']:
		candidates.append(3)
		component = C('THREE')
		drop(counter, component)
	while counter['V']:
		candidates.append(5)
		component = C('FIVE')
		drop(counter, component)
	while counter['O']:
		candidates.append(1)
		component = C('ONE')
		drop(counter, component)
	while counter['N']:
		candidates.append(9)
		component = C('NINE')
		drop(counter, component)
	candidates = [str(candidate) for candidate in candidates]
	candidates.sort()
	return ''.join(candidates)

if __name__ == '__main__':
	outfile = open('a.out', 'w')
	T = int(input())
	for t in range(1, T + 1):
		s = input()
		answer = solve(s)
		outfile.write("Case #{}: {}\n".format(t, answer))
