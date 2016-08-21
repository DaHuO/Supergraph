T=int(raw_input())
for t in range(0,T):
	nums=list(range(0,10))
	N=int(raw_input())
	i=1
	gotAns=0
	ans=''
	while not gotAns:
		if(N):
			tmp=i*N
			# print 'NotZero  tmp:'+str(tmp)
			while tmp:
				rem=tmp%10
				try:
					nums.remove(rem)
				except:
					pass
				if(not len(nums)):
					gotAns=1
					ans=i*N
				tmp=tmp/10
		else:
			ans='INSOMNIA'
			gotAns=1
		i+=1
	T-=1
	print('Case #'+str(t+1)+': '+str(ans))
