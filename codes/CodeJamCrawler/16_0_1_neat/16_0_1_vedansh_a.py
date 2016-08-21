
def getCount(n):
	i = 1
	a = ['0','1','2','3','4','5','6','7','8','9']
	while True:
		q = n*i
		i = i + 1
		a = list(set(a) - set(str(q)))
		if a == []:
			return q
			break


t = input()
for i in xrange(t):
	a = int(raw_input())
	if a != 0:
		c = getCount(n=a)
		print "Case #%d: %d" % (i+1,c)	
	else:
		print "Case #%d: INSOMNIA" % (i+1)
		