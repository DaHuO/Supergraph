for x in range(int(input())):
	s=input()
	count=0
	l=len(s)
	if len(s)==s.count('+'):
		print("Case #"+str(x+1)+": 0")
	elif len(s)==s.count('-'):
		print("Case #"+str(x+1)+": 1")
	else:
		for k in range(l-1):
			if s[k]=='-' and s[k+1]=='+':
				count+=1
			elif s[k]=='+' and s[k+1]=='-':
				count+=1
		if s[l-1]=='-':
			count+=1
		print("Case #"+str(x+1)+": "+str(count))