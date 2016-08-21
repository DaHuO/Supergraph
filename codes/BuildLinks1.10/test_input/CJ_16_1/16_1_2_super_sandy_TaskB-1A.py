from collections import Counter
t = int(raw_input())
for i in xrange(1, t + 1):
	n = int(raw_input())
	x =[]
	for j in range(2*n-1):
		x+= map(int, raw_input().split())

	a =[]
	y = Counter(x)
	z = set(x)
	for j in z:
		if y[j] % 2 != 0:
			a.append(j)
	a.sort()
	b = ' '.join(str(e) for e in a)
	print "Case #{}: {}".format(i, b)
