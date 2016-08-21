N = int(input())

for i in range(N) :
	nb=int(input())
	t=nb
	if nb==0:
		res="INSOMNIA"
	else:
		k=[0,0,0,0,0,0,0,0,0,0]
		while k!=[1,1,1,1,1,1,1,1,1,1]:
			s=str(t)
			for c in s:
				k[int(c)]=1
			t=t+nb
		res=int(t-nb)
	print('Case #'+str(i+1)+': '+str(res))


