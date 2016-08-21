def solve(n):
	dg = [0,0,0,0,0,0,0,0,0,0]
	i = 0
	c = 0
	while c<10:
		i+=1
		t = n*i
		while t!=0:
			d = t%10
			t/=10
			if dg[d] == 0:
				dg[d] = 1
				c+=1
	return i*n

t = int(raw_input())

for i in range(1, t+1):
	n = int(raw_input())
	if n == 0:
		print "Case #%d: INSOMNIA" % i
	else:
		print "Case #%d: %d" % (i, solve(n))
	
