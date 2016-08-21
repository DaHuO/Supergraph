t=int(raw_input())
i=0
while(i<t):
	i+=1
	N=int(raw_input())
	if N==0:
		#fido.write('Case #%d: INSOMNIA'%i+"\n")
		print ('Case #%d: INSOMNIA'%i)
	else:
		a=set(())
		k=2
		n=N
		while(True):
			a=set(a.union(set(map(int, str(n)))))
			#print a
			if len(a)==10:
				#fido.write('Case #%d: %d'%(i,n)+'\n')
				print ('Case #%d: %d'%(i,n))
				break
			else:	
				n=N*(k)
				#print n,a
				k+=1