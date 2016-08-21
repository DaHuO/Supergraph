def solve(s):
	if len(s) == 0:
		return 0
	r = 1
	for i in range(len(s) - 1):
		if s[i] != s[i+1]:
			r += 1
	if s[-1] == '+':
		r -= 1
	return r

caseNum = int(raw_input())
for i in range(caseNum):
	print 'Case #%d: %s' % (i+1, solve(raw_input()))