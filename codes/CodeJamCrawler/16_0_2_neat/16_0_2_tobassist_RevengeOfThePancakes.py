def ProcessLine(N):
	c = 0;
	for i in range(1,len(N)-1):
		if (N[i] != N[i-1]):
			c = c + 1
	if (N[0] == '-' and c%2==0) or (N[0] == '+' and c%2!=0):
			c = c + 1
	return c

f= open('B-large.in','r')
# Read number of trials (T)
T = f.readline()
for t in range(int(T)):
	N = f.readline()
	result = ProcessLine(N)
	print 'Case #' + str(t+1) +': '+ str(result)
