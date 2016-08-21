def trata(z):
	s = set();
	if z == 0:
		return "INSOMNIA"
	n2 = 1
	n = set([1,2,3,4,5,6,7,8,9,0])
	while (1):
		s2 = n2*z
		s22 = str(s2)
		for t in s22:
			s.add(int(t))
		n2+=1
		if(n.issubset(s)):
			return s22



n = input()
i = 0
while i < n:
	try:
	   z = input()
	except Exception, e:
		break
	print 'Case #'+ str(i+1) + ": "+str(trata(z))
	i+=1
