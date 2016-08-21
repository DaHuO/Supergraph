for t in xrange(1,input()+1):
	num=['1','2','3','4','5','6','7','8','9','0']
	N=input()
	M=0
	ii=0
	while len(num)!=0:
		M+=N
		n=list(str(M))
		for j in n:
			if j in num:
				num.remove(j)
		ii+=1
		if ii>5000000:break
	if len(num)!=0:
		print 'Case #%d: INSOMNIA'%t
	else:print 'Case #%d: %d'%(t,M)