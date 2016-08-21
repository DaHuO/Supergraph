n=int(raw_input())
i=0
while(i<n):
	s=""
	user=raw_input()
	s=s+user[0]
	for x in user[1:len(user)]:
		if (x<s[0]):
			s=s+x
		else:
			s=x+s

	print "Case #"+str(i+1)+": "+s
	i=i+1

