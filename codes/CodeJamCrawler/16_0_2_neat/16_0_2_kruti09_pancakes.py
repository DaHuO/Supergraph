T=int(input())
for _ in range(T):
	s=input()
	c=0
	for i in range(len(s)-1):		
		if(s[i]!=s[i+1]):
		    c=c+1
	if s[-1]=='-':
	    print('Case #{}: {}'.format(_+1,c+1))
	else:
	    print('Case #{}: {}'.format(_+1,c))

