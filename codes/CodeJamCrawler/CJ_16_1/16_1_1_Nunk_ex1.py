N = int(input())

for i in range(N) :
	S=str(input())
	ct=S[0]
	res=""
	for c in S :
		if res=="":
			res=c
		else :
			if c<res[0]:
				res=res+c
			else :
				res=c+res
			
		
	print('Case #'+str(i+1)+': '+str(res))


