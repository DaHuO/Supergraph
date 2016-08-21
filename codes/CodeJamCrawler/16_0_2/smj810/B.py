n = int(raw_input())
for i in xrange(n):
	ans = 0
	
	line = raw_input()
	curr = line[0]
	for c in line:
		if c != curr:
			curr = c
			ans += 1
	if line[-1] != '+':
		ans += 1
	print "Case #" + str(i+1) + ": " + str(ans);
