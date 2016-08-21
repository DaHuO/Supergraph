import itertools
from sets import Set

T = int(raw_input())

for z in range(T):
	N = int(raw_input())
	l = []
	s = (2*N)-1
	done = False

	for y in range(s):
		r = map(int, raw_input().strip().split(' '))
		l.append(r)

	for poss in list(itertools.product([True, False], repeat=s)):
		m = []

		for j, i in enumerate(poss):
			if i is True:
				m.append(l[j])

		if len(m) == N:
			m.sort()
			flag = True
			for x in range(1, N):
				for v in range(N):
					if m[x][v] <= m[x-1][v]:
						flag = False

			if flag is True:
				flip = Set()
				for x in range(N):
					rf = []
					for v in range(N):
						rf.append(m[v][x])
					flip.add(' '.join(map(str,rf)))


				for j, i in enumerate(poss):
					if i is False:
						flip.discard(' '.join(map(str,l[j])))

				if len(flip) == 1:
					print "Case #%d: %s" % (z+1, flip.pop())
					done = True
					
		if done is True:
			break