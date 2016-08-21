t=int(input())
while(t):
	j=1
	a=input()
	s=a[0]
	b=len(a)
	for i in range(b-1):
		d=a[i+1]
		if ord(d)>=ord(s[0]):
			s=a[i+1]+s
		else:
			if ord(s[0])>ord(d):
				s=s+a[i+1]
	print("Case #{}: {}".format(j,s))
	j=j+1
	t=t-1