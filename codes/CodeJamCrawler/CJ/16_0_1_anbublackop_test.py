for _ in range(int(input())):
	n=int(input())
	a=""
	seta=list()
	another_set={'0','1','2','3','4','5','6','7','8','9'}
	if n==0:
		ans='INSOMNIA'
	else:	
		i=1
		while(set(a)!=another_set):
			mul=n*i
			a+=(str(mul))
			seta.append(mul)
			ans=mul
			i+=1
	print ('Case #{}: {}'.format(_+1,ans))
