t = input()
for it in xrange(1,t+1):
	s = raw_input()
	s += "#"
	l = [1]
	prev = s[0]
	i = 1
	while s[i] != '#':
		if s[i] == prev:
			l[len(l)-1]+=1
		else:
			l.append(1)
		prev = s[i]
		i+=1
	#print l
	ans = 0
	if s[0] == '-':
		ans = 1
		ans += 2*((len(l)-1)//2)
	else:
		ans += 2*(len(l)//2)
	print "Case #%d: %d" % (it,ans)
		