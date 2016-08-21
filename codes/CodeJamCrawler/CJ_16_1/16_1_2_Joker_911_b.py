with open('B-small.in','r') as f:
	t=int(f.readline())
	for i in range(t):
		n=int(f.readline())
		di=dict()
		lir=list()
		
		for j in range(2*n-1):
			st=f.readline().split()
			for k in range(n):
				di[int(st[k])]=di.get(int(st[k]),0)+1
		for h in di.keys():
			if not di[h]%2==0:
				lir.append(h)
		print("Case #"+str(i+1)+": ",end='')
		lir.sort()
		for g in range(len(lir)):
			print(lir[g],end=" ")
		print("")



			