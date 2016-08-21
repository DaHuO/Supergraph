filename = 'A-large.in'
f = open(filename,'r')
T = int(f.readline())
for i in range(1,T+1):
	s = f.readline().rstrip()
	a=b=""
	for j in s:
		a = max(j+a,a+j)
		b = max(b+j,j+b)
	print "Case #%d: %s" % (i,max(a,b))