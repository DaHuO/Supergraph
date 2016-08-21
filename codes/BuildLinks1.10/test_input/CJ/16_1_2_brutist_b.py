t=input()
for tc in range(t):
	n=input()
	mat=[]
	for i in range(2*n-1):
		mat.append(map(int,raw_input().split()))
	freq=[0]*(2505)
	for i in range(2*n-1):
		for j in range(len(mat[i])):
			freq[mat[i][j]]+=1
	extras=[]
	for i in range(1,len(freq)):
		if freq[i]%2!=0:
			extras.append(i)
	extras.sort()
	print "Case #"+str(tc+1)+":",' '.join(map(str,extras))