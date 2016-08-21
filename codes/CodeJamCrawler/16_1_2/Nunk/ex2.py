T = int(input())

for k in range(T) :
	N=int(input())
	l=[]
	simple=[]
	res=""
	for i in range(2*N-1):
		l.append(input().split(" "))
	for i in range(2*N-1):
		for j in range(N):
			s=0
			for m in range(2*N-1):
				s=s+int(l[m].count(l[i][j]))
			if ((s%2)!=0)and (not(simple.count(int(l[i][j]))>0)) :
				simple.append(int(l[i][j]))
	simple.sort()
	for i in simple:
		res=res+" "+str(i)
	print('Case #'+str(k+1)+': '+str(res))
