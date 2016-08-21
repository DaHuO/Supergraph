for i in range(int(input())):
	n=input()
	s1=""
	for ch in n:
		if s1=="":
			s1=s1+str(ch)
		else:
			if s1[0]>ch:
				s1=s1+str(ch)
			elif s1[0]<ch or s1[0]==ch:
				s1=str(ch)+s1
	print("Case #"+str(i+1)+": "+s1)