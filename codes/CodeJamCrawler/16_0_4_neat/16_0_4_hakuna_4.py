T=int(raw_input())
for t in range(T):
	print "Case #"+str(t+1)+": ",
	line = raw_input().split()
	k = int(line[0])
	c = int(line[1])
	s = int(line[2])
	if k==s:
		for i in range(1,s+1):
			print str(i) + " ",
		print