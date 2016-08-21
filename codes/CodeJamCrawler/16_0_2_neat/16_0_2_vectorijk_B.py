def solve(s):
	cnt = 0
	for i in range(len(s)-1, -1, -1):
		if s[i] == '-':
			for j in range(i, -1, -1):
				if s[j] == '+':
					s[j] = '-'
				else:
					s[j] = '+'
			cnt += 1
	return cnt

t = input()
for ks in range(1,t+1):
	n = raw_input()
	# print list(n)
	res = solve(list(n))
	print "Case #%d: %d" % (ks, res)