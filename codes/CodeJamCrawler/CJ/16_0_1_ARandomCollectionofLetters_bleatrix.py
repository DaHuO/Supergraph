raw_input()

i=0
while True:
	i=i+1
	N=int(raw_input())
	seenset=set(str(N))
	if N==0:
		print "Case #"+str(i)+": INSOMNIA"
		continue
	tmp=N
	while True:
		# This loop shouldn't run that many times.
		if len(seenset)==10:
			print "Case #"+str(i)+": "+str(tmp)
			break
		tmp=tmp+N
		seenset=seenset.union(set(str(tmp)))
