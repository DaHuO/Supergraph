
t=int(raw_input())
#t=int(lis[0])
for i in range(0,t):
	lis=[]*10
	for j in range(0,10):
		lis.insert(j,0)
	n=int(raw_input())
	solution = 0
	if n==0:
		print 'Case #'+str(i+1)+': INSOMNIA'
	else:
		p=1
		while p!=0:
			m=p*n
			solution = p*n
			while m:
				dig=m%10
				m//=10
				if lis[dig]==0:
					lis[dig]=1
			for x in range(0,10):
				if x==9 and lis[x]==1:
					p=0
				if lis[x]==0:
					p+=1
					break

		print 'Case #'+str(i+1)+': '+str(solution)