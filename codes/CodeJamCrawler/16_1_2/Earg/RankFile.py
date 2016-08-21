T = int (input ())
for i in range (0, T):
	N = int (input ())
	nums = {}
	for j in range (0,(2*N-1)):
		c = raw_input()
		for a in c.split():
			if a in nums:
				nums [a] += 1
			else:
				nums [a] = 1
		l = []
		for b in nums:
			if (nums[b] % 2) == 1:
				l.append(b)
	l.sort(key = int)
	s = ' '.join(l)
	print("Case #{}: {} ".format(i+1,s))
