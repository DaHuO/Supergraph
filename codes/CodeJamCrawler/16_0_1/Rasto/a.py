# Counting Sheep

import fileinput

def solve(n):
	if n == 0: return 'INSOMNIA'

	v = set(range(0, 10))
	a = 0
	d = set()
	while d != v:
		a += n
		d |= set(int(c) for c in str(a))

	return a

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	n = int(f.readline().rstrip())
	z = solve(n)
	print('Case #%s: %s' % (t + 1, z))
