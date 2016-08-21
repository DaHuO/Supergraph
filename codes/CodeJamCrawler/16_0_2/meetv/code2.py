def ctr(s):
	i,z = 0,0
	if s[0] == '-':
		z = 1
	while (i < len(s) and s[i]=='-'):
		i += 1
	for j in xrange(i, len(s)-1):
		if (s[j]=='+' and s[j+1]=='-'):
			z+=2
	return z

f = open("B-large.in", 'r').read().split('\n')
w = open("output.txt", 'w')

t = int(f[0])
for i in xrange(t):
	st = ("Case #%d: %d" % (i+1,ctr(f[i+1])))
	print(st)
	w.write(st+"\n")