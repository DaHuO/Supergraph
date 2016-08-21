for k in range(input()):
	z=0
	t=map(str,raw_input())
	for i in range(0,len(t)-1):
		if(t[i]==t[i+1]):
			continue
		else:
			z+=1
	if(t[-1]=="-"):
		z+=1
	print "Case #%d: %d"%k%z