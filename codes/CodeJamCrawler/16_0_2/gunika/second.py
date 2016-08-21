t=int(input())
b=1
while(t>0):
	s=input()
	c=0
	for i in range(len(s)-1):
		if(s[i]!=s[i+1]):
			c+=1
	if(s[len(s)-1]=='-'):
		c+=1
	print("Case #{}: {}".format(b,c))
	b+=1
	t-=1