f=open("a.in","r")
t=int(f.readline().rstrip("\n"))
for i in range(0,t):
	ans=""
	s=f.readline().rstrip("\n")
	for x in s:
		#print(s)
		if(len(ans)==0):
			ans+=x

		else:
			if(x>=ans[0]):
				ans=x+ans
				#print(ans)
			else:
				ans=ans+x
				#print("case2:"+ans)
	print("Case #"+str(i+1)+": "+ans)

