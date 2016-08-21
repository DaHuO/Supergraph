filename = 'B-large.in'
f = open(filename,'r')
T = int(f.readline())


def calc(plist):
	p = list()
	for i in range(len(plist)+1):
		p.append([0]*(250))
	p[0][0] = 1 - plist[0]
	p[0][1] = plist[0]
	for i in range(1,len(plist)):
		x = plist[i]
		for j in range(i+2):
			p[i][j] = p[i-1][j-1] * x + p[i-1][j] * (1-x)
	return p[len(plist)-1][(len(plist))/2]


for i in range(1,T+1):
	print "Case #%d:" % i,
	n,k = map(int,f.readline().split())
	p = map(float,f.readline().split())
	p.sort()
	x = 0
	for i in range(k+1):
		pl = p[0:i] + p[(n-k+i):n]
		x = max(x,calc(pl))
	print "%.6f" % x