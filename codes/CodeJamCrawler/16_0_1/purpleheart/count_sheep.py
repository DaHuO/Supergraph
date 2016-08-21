import sys
f = open(sys.argv[1],"r")
n = int(f.readline())
c = 1
while n > 0:
	s = int(f.readline())
	s_copy = s
	check = [False,False,False,False,False,False,False,False,False,False]
	if s == 0:
		answer = "INSOMNIA"
	else:
		count = 1
		while s < sys.maxint and type(s) is int:
			for x in list(str(s)):
				check[int(x)] = True
			if reduce(lambda x,y: x&y, check) == False:
				s = s_copy * count
				count += 1
			else:
				break
		if reduce(lambda x,y: x&y, check) == False:
			answer ="INSOMNIA"
		else:
			answer = s
	print ("Case #%d: %s") % (c,answer)
	n -= 1
	c += 1