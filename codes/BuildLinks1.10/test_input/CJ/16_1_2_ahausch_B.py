import sys

fin = open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin

T = int(fin.readline())

def copy_vert(m, l, i):
	for j in range(i, len(l)):
		m[j][i] = l[j]

for t in range(1, T + 1):
	N = int(fin.readline())
	L = [list(map(int, fin.readline().split(' '))) for _ in range(N * 2 - 1)]

	m = dict()
	
	for l in L:
		for c in l:
			if (not c in m):
				m[c] = 1
			else:
				m[c] += 1
			
	ans = []
	
	for c in sorted(m.keys()):
		if (m[c] % 2 == 1):
			ans.append(c)
	
	print("Case #{0}: {1}".format(t, ' '.join(str(i) for i in ans)))
