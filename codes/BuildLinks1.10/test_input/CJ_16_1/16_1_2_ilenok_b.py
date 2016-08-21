inf = open("b.in", 'r')
outf = open("b.out", 'w')

MAXHEIGHT = 3000


t = int(inf.readline())

for k in xrange(0, t):
	heights = [0] * MAXHEIGHT
	n = int(inf.readline())
	print "n:" , n,
	m = 2 * n - 1
	for i in xrange(0, m):
		rorc = map(int, inf.readline().split())
		for h in rorc:
			heights[h] += 1
	res = []
	for h in range(0, MAXHEIGHT):
		if (heights[h] % 2 == 1):
			res.append(h)
	res.sort()
	print len(res)			
				
	outf.write("Case #" + str(k + 1) + ": ")	
	outf.write(' '.join(map(str, res)) + "\n")
outf.close()
