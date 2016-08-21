from itertools import combinations
import sys

def ptie(picks):
	possibs = [0 for i in range(len(picks)+1)]
	possibs[0] = 1
	for p in picks:
		tpossibs = [0 for i in range(len(picks)+1)]
		for j in range(len(picks)):
			tpossibs[j+1] = possibs[j+1]*(1-p)+possibs[j]*p
		tpossibs[0] = possibs[0]*(1-p)
		possibs = tpossibs
	return possibs[len(possibs)>>1]

a = open(sys.argv[1]+'.in').readlines()
b = [[float(x) for x in a[i].strip().split(' ')] for i in range(2, len(a), 2)]
out = open(sys.argv[1]+'.out', 'w')

for i in range(len(b)):
	k = int(a[i+i+1].strip().split(' ')[1])
	out.write('Case #%d: %f\n' % (i+1, max(ptie(j) for j in combinations(b[i], r=k))))

out.close()
