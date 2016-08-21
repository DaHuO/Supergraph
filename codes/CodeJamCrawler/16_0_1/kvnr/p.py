

t=int(raw_input())

for x in xrange(1,t+1):
	n=int(raw_input())
	if n==0:
		print 'Case #'+str(x)+': '+ 'INSOMNIA'
	else:
		seen =[] 
		i=1;
		while len(seen)<10:
			l=str(i*n)
			for y in l:
				if y not in seen:
					seen+=[y]
			i+=1
		print 'Case #'+str(x)+': '+ str( (i-1)*n )
		