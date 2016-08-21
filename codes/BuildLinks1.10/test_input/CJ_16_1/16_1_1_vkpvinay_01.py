# your code goes here
for i in range(1,int(input())+1):
	s=input()
	ans=s[0]
	for j in range(1,len(s)):
		if(s[j]<ans[0]):
			ans=ans+s[j]
		else:
			ans=s[j]+ans
	print(ans)