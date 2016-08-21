import sys

sys.stdin.readline() # T

def solve(l):
	l = l.strip()
	if len(l) == 0:
		return 0
	prev = ''
	groups = 0
	for c in l:
		if c != prev:
			groups += 1
			prev = c
	if c == '+':
		groups -= 1
	return groups

i = 1
for l in sys.stdin:
	print('Case #{}: {}'.format(i, solve(l)))
	i += 1

