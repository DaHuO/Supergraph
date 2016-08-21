t=int(raw_input())
for tcase in xrange(t):
	n=raw_input().strip()
	seenset=set(n)
	i_n =int(n)
	i_na= i_n
	cIdx=1
	fl=False
	while(len(seenset)!=10):
		cIdx+=1
		if i_n+i_na== i_n:
			fl=True
			break
		else:
			i_n+=i_na
			seenset=seenset.union(set(str(i_n)))
	if fl:
		print "Case #"+str(tcase+1)+": INSOMNIA"
	else:
		print "Case #"+str(tcase+1)+": "+str(i_n)

