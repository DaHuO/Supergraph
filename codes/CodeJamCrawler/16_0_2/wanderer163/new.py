t=int(raw_input())
for _ in xrange(t):
	n=int(raw_input())
	count =0
	a=2
	val =n
	lol = [0,0,0,0,0,0,0,0,0,0]
	if n==0:
		zz = "#"+str(_+1)+":"
		print "Case",zz,"INSOMNIA"
		continue
	while 1:
		s=str(val)
		#print s
		for i in xrange(len(s)):
			if lol[int(s[i])]==0:
				lol[int(s[i])] = 1
				count+=1

		if count==10:
			break
		val=n*a
		a+=1
	zz = "#"+str(_+1)+":"
	print "Case",zz,val