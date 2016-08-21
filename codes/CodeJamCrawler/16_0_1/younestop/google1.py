N=int(raw_input())
M=N+1
for i in range (1,M):
	nbr=raw_input()
	if int(nbr)==0:
		print 'Case #%d: INSOMNIA'%i
	else:
		nbr_temp=nbr
		nb=int(nbr)
		ens= set([])
		for j in nbr_temp:
				ens.add(j)
		while(len(ens)!=10):
			nbr_temp='%d'%(nb+int(nbr_temp))
			for j in nbr_temp:
				ens.add(j)	
		print 'Case #%d: %s'%(i,nbr_temp)
	
	
	
