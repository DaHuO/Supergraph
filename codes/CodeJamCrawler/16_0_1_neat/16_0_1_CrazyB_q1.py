t=int(raw_input())
for i in xrange(t):
	n=int(raw_input())
	l=range(0,10)
	#print l
	if(n==0):
		print("Case #" + str(i+1) + ": INSOMNIA")
		continue;
	temp=n
	while(len(l)!=0):
		dig=map(int,str(temp));
		for num in dig:
			if num in l:
				l.remove(num)
		#print temp
		#print l
		temp=temp+n
	temp=temp-n
	print "Case #"+str(i+1)+": "+ str(temp)
