for T in range(input()):
	s=list(raw_input())+["+"]
	i=0
	for x in range(1,len(s)):
		if s[x]!=s[x-1]:
			i+=1
	print "Case #%d: %d" % (T+1,i)
	
