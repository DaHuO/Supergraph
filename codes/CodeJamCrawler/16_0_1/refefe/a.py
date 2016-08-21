import sys

T = int(sys.stdin.readline())

for k in xrange(T):
	N = sys.stdin.readline()
	if N[-1] == '\n':
		N = N[:-1]
	N = int(N)

	if N == 0:
		print "Case #{0}: {1}".format(k+1, "INSOMNIA")
		continue

	d = {}
	i = 1
	nt = 0
	while len(d) < 10:
		ni = (N * i)
		nt = ni
		while ni > 0:
			d[ni % 10] = 1
			ni = ni / 10
		
		i += 1
		#print nt, d
		#break
		
	print "Case #{0}: {1}".format(k+1,nt) 
