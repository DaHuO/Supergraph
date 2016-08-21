t = int(raw_input())
for i in xrange(1, t + 1):
	s = raw_input()
	res=''
	for j in s:
		if not res:
			res+=j
		else:
			if res[0] >j:
				res+=j
			else:
				res = j + res
	print "Case #{}: {}".format(i, res)