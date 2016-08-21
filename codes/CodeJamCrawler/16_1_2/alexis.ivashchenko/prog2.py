tests = int(input())


def solve(matrix, size):
	a = []
	for i in matrix:
		for j in i:
			a.append(j)
	d = [i for i in a if a.count(i) % 2 == 1]
	d = list(set(d))
	d.sort()
	return d
	
test = 1
while test <= tests:
	N = int(input())
	l = []
	for i in range(2 * N - 1):
		l.append(list(map(int, input().split(' '))))
	#print('####', l)
	print('Case #%d: %s' % (test, ' '.join(map(str,solve(l, N)))))
	test += 1