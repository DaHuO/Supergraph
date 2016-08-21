n=int(raw_input().strip())
for j in range(1,n+1):
	a=str(raw_input().strip())
	temp=int(a)
	i=1
	while True:
	    if temp==0:
	    	print 'Case #%s: Insomnia' %j
	    	break
	    elif set(a) == set('0123456789'):
	        print 'Case #%s: %s' %(j,i*temp)
	        break
	    else:
	        i+=1
	        
	        a+=str(i*temp)