t=int(input())
for i in range(t):
	n=int(input())
	if n==0:
		ans="INSOMNIA"
	else:
		s=set(list(str(n)))
		ans=n
		z=0
		while(len(s)<10):
			z=z+n
			k=set(list(str(z)))
			s=s|k
			ans=z

	print("Case #" + str(i+1) +": "+str(ans))