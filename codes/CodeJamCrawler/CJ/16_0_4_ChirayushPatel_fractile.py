t=int(input())
ans=[]
for i in range(0,t):
	k,c,s=list(map(int,input().split(' ')))
	x=''
	for j in range(k):
		x=x+' '+str(j+1)
	if s<k :
		x="Impossible"
	ans.append(x)
for i in range(len(ans)):
	print("Case #"+str(i+1)+": "+str(ans[i]))
