
for t in range(int(input())):
	m=int(input())
	n=m
	if(n==0):
		print("Case #"+str(t+1)+": INSOMNIA")
		continue
	a=[0]*10
	k=1
	while(a.count(1)<10):
		#print(str(n),a)
		for j in str(n):
			a[ord(j)-ord('0')]=1
		if(a.count(1)==10):
			break
		n=k*m
		k+=1

	print("Case #"+str(t+1)+": "+str((k-1)*m)	)