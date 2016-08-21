t=int(raw_input())
for i in range(0,t):
	s=raw_input()
	sz=len(s)
	lis=[]
	for j in s:
		if j =='+':
			lis.append(1)
		elif j =='-':
			lis.append(0)
	p=1
	solution = 0
	m=0
	for w in range(0,sz):
		if lis[w]==0:
			m=0
			break
		elif lis[w]==1 and w==sz-1:
			solution = 0
			m=1
			break

	if m==0:
		while p!=0:
			x=0
			pattern=0
			while x<sz-1:
				if lis[x]==lis[x+1]:
					x+=1
					pattern=lis[x]
				elif lis[x]!=lis[x+1]:
					pattern = lis[x]
					break
		

			for y in range(0,x+1):
				if pattern==0:
					lis[y]=1
				else:
					lis[y]=0
			for y in range(0,sz):
				if lis[y]==0:
					p+=1
					break
				elif y==sz-1 and lis[y]==1:
					solution = p
					p=0

	print 'Case #'+str(i+1)+': '+str(solution)