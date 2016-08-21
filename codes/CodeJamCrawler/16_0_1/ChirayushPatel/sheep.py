t=int(input())
ans=[]
for i in range(0,t):
	n=int(input())
	mul=n
	d=set(str(n))
	while(len(d)<10 and n!=0):
		mul=mul+n
		for j in set(str(mul)):
			d.add(j)
	if n==0: ans.append("Insomnia")
	else:	ans.append(mul)
for i in range(len(ans)):
	print("Case #"+str(i+1)+": "+str(ans[i]))
