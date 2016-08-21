from itertools import permutations
import sys

def valid(keys):
	w = {
		'R': {'R': '', 'P': 'P', 'S': 'R'},
		'P': {'R': 'P', 'P': '', 'S': 'S'},
		'S': {'R': 'R', 'P': 'S', 'S': ''},
	}
	x = [i for i in keys]
	while len(x) > 1:
		y = []
		for i in range(0, len(x), 2):
			z = w[x[i]][x[i+1]]
			if z == '':
				return False
			y.append(z)
		#print(x, y)
		x = y
	return True

a = open(sys.argv[1]+'.in').readlines()
b = [[int(x) for x in a[i].strip().split(' ')] for i in range(1, len(a))]
out = open(sys.argv[1]+'.out', 'w')

for i in range(len(b)):
	n = int(b[i][0])
	r = int(b[i][1])
	p = int(b[i][2])
	s = int(b[i][3])
	x = [''.join(j) for j in permutations('R'*r+'P'*p+'S'*s) if valid(j)]
	out.write('Case #%d: %s\n' % (i+1, min(x) if len(x) > 0 else "IMPOSSIBLE"))
	out.flush()

out.close()
