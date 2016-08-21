def check(z):
	s=z[:]
	su=sum(s)
	for u in range(len(s)):
		if s[u]>(su/2):
			return False
	return True




for i in range(input()):
	print "Case #"+str(i+1)+":",
	n=input()
	p=map(int,raw_input().split())
	#print "p: ",p
	#p1='A'
	j=0


	k=0
	c=p[:]
	while not(all(v == 0 for v in c)):
		y=0
	#	print "k: ",k
		x=[]
		c[k]=c[k]-1
	#	print "c: ",c
		x0=c[k]
		for l in range(len(c)):
	#		print "l: ",l
			c[l]=c[l]-1
	#		print "C in l: ",c
			if check(c):
	#			print "YES"
				x.append(chr(ord('A') + k))
				x.append(chr(ord('A') +l))
				e=x[0]
				d=x[1]
				y=1
				print e+d,
	#			print
				break
			else:
				c[l]+=1

		if len(x)==0:
	#		print "c in if :",c
			if check(c):
	#			print "IF YES"
				print chr(ord('A') +k),
	#			print 
				y=1
		if y==0:
			c[k]=c[k]+1

	#	print "c after the loop: ",c
	#	print "x: ",x	
		k+=1
		k=k%len(c)
		
	print