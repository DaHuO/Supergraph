t=input()
case=1
while(t>0):
	n,mul=input(),1
	temp=n
	if n==0: print 'Case #'+str(case)+':','INSOMNIA'
	else:
		a=set('1234567890')
		while len(a)>0:
			a=a-set(str(temp*mul))
			n=temp*mul
			mul+=1
		print 'Case #'+str(case)+':',n
	case+=1	
	t-=1	
