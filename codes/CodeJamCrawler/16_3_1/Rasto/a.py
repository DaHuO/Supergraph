# Senate Evacuation

import fileinput

def solvemore(n, d):
	m1, m2 = (0, 0), (0, 0)
	for i, p in enumerate(sorted(d.items(), key=lambda x: -x[1])):
		if i == 0: m1 = p
		elif i == 1: m2 = p
		else: break

	del d[m1[0]]
	del d[m2[0]]
	if m1[1] - m2[1]:
		z = [m1[0]] * (m1[1] - m2[1])
	else:
		z = []

	for k, v in sorted(d.items(), key=lambda x: -x[1]): z += [k] * v

	return z + solvetwo(m2[1], m1[0], m2[0])

def solvetwo(i, x, y):
	return [x + y] * i

def solve(n, c):
	if n == 2:
		z = solvetwo(c[0], 'A', 'B')
	else:
		d = {}
		for i, x in enumerate(c): d[chr(65 + i)] = x
		z = solvemore(n, d)

	return " ".join(z)

f = fileinput.input()
for t in range(int(f.readline().rstrip())):
	n = int(f.readline().rstrip())
	c = list(map(int, f.readline().rstrip().split(' ')))
	z = solve(n, c)
	print('Case #%s: %s' % (t + 1, z))
