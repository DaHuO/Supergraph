import itertools, math
def lowestDivisor(n):
	for i in xrange(2, int(math.sqrt(n)+3)):
		if n % i == 0:
			return i
	return -1

for z in xrange(input()):
	s, c = map(int, raw_input().split())
	l = list(itertools.product(range(2), repeat=s-2))
	print "Case #"+str(z+1)+":"
	for i in xrange(len(l)):
		l[i] = '1' + ''.join(map(str, l[i])) + '1'
	if s < 3:
		l = ['1'*s]
	for idx in xrange(len(l)):
		i = l[idx]
		dl = []
		for j in range(2, 11):
			n = int(i, j)
			d = lowestDivisor(n)
			if d > 0:
				dl.append(d)
		if len(dl) == 9 and c > 0:
			c = c - 1
			print i, " ".join(map(str, dl))
		if c <= 0:
			break