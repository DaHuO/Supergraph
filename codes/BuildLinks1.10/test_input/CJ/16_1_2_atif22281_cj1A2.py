for  t in range(1,int(input())+1):
	n=int(input())
	l1=[]
	for i in range(1,2600):
		l1.append(0)
	for i in range(2*n-1):
		l=input().split()
		l=[int(j) for j in l]
		for j in l:
			l1[j]+=1
	op=""
	f=0
	for i in range(len(l1)):
		if l1[i]!=0 and l1[i]%2!=0:
			if f==0:
				op=str(i)
				f=1
			else:
				op=op+" "+str(i)
	print("Case #{}: {}".format(t,op))