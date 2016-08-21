# Revenge of the Pancakes

import fileinput

def flip(s, p, n):
	s = s[0:p][::-1] + s[p:n]
	for i in range(0, p): s[i] = '+' if s[i] == '-' else '-'
	return s

def solve(s):
	n = len(s)
	z = 0
	j = n - 1
	while j >= 0:
		if s[j] == '-':
			p = 0
			while p < j and s[p] == '+': p += 1
			if p > 0:
				for i in range(0, p): s[i] = '-'
				z += 1

			s = flip(s, j + 1, n)
			z += 1

		j -= 1

	return z

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	s = list(f.readline().rstrip())
	z = solve(s)
	print('Case #%s: %s' % (t + 1, z))
