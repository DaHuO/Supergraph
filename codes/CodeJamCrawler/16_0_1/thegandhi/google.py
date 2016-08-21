content = []
with open("/home/rubal/A-large.in") as f:
    content = f.readlines()

thetestcases = content[0]
b = 0
while b!=int(thetestcases):

	thenumbers = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 0]
	an = content[b+1]
	n = int(an)
	i = 1
	newlist = []

	while (1):
		
		if n == 0:
			print "Case #" + str(b+1) + ":",
			print "INSOMNIA"
			break
		ans = i * n
		newlist = map(int, str(ans))
		for x in range(len(newlist)):
			if(newlist[x] in thenumbers):
				thenumbers.remove(newlist[x]) 
		if len(thenumbers) == 0:
			print "Case #" + str(b+1) + ":",
			print ans
			break	
		i = i + 1
	
	b = b + 1
