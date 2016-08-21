t = int(raw_input())
for i in range(t):
	n = int(raw_input())
	if n==0:
		print "Case #%d: INSOMNIA" % (i+1)
	else:
		j=1
		k=0
		p=set()
		r=set()
		while True:
			k=j*n
			r=set(map(int,str(k)))
			p |= r
			if (0 in p and 1 in p and 2 in p and 3 in p and 4 in p and 5 in p and 6 in p and 7 in p and 8 in p and 9 in p):
				print "Case #%d: %d" %(i+1,k)
				break
			else:
				j+=1