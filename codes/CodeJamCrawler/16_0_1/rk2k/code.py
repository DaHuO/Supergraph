def find_dig(m):
	m=str(m)
	d=set()
	for i in m: d.add(i)
	#print d
	return d

for t in xrange(input()):
	n=input()
	if n==0:
		print 'Case #%d:'%(t+1),'INSOMNIA'
	else:
		seen=set()
		seen=seen.union(find_dig(n))
		step=1
		num=step*n
		while len(seen)<10:
			step+=1
			num=n*step
			seen=seen.union(find_dig(num))

		if len(seen)==10:
			print 'Case #%d:'%(t+1),num