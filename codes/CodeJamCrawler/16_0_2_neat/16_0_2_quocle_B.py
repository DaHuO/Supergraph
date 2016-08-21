import sys
f = open(sys.argv[1], 'r')
N = int(f.readline().strip())
for case in xrange(1,N+1):
	s = f.readline().strip()
	count = 0
	for i in xrange(len(s)):
		if s[i] == '+':
			if i > 0 and s[i-1] == '-':
				count += 1
		elif s[i] == '-':
			if i > 0 and s[i-1] == '+':
				count += 1
	if s[-1] == '-':
		count += 1
	print 'Case #%s: %s' %(case, count)
