def getResult(n):
	if(n==0):
		return "INSOMNIA"
	s = set()
	seen=0
	i = 1
	m =0
	while(True):
		m +=n
		temp  = m 
		while(temp>0):
			s.add(temp%10)
			temp = temp/10
		if(len(s)==10):
			return m
		i=i+1

t = int(raw_input()) 
for i in xrange(1, t + 1):
  n = int(raw_input())  
  result = getResult(n)
  print "Case #{}: {}".format(i, result)