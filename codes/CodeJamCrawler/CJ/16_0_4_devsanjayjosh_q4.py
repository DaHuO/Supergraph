#lis=[]
def find(a,b,c):
	if a==1:
		return [1]
	if b ==1:
		#print(1)
		if a>c:
			return 'Impossible'
		else:
			lis=list(i for i in range(1,a+1))
	else:
		#print(2)
		if (a-1)>c:
			return 'Impossible'		
		else:	
			lis=list(i for i in range(2,a+1))

	return lis	




t=int(input())

for i in range(1,t+1):
	a=input()
	#print(a)
	b=list(map(int,a.split()))
	ans=find(b[0],b[1],b[2]);
	s="Case #"+str(i)+":"
	if type(ans) == list:
		print(s,end=" ")
		for i in range(0,len(ans)):
			print(ans[i],end=" ")
		print()	
	else:
		print(s,ans) 	
	
	