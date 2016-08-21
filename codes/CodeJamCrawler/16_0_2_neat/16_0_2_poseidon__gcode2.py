inp=int(raw_input())
for a in range(inp):
	s=raw_input()
	s=list(s)
	count=0
	count2=0
	p=len(s)
	while True:
		s=s[:p]
		for p in range(len(s)-1,-1,-1):
			if s[p]=='-':
				count+=1
				break
		for y in range(len(s)):
			if s[y]=='-':
				s[y]='+'
			else:
				s[y]='-'
		for x in s:
			if x=='+':
				count2+=1
			else:
				break
		if count2==len(s):
			break
		count2=0
	print "Case #"+str(a+1)+":"+" "+str(count)