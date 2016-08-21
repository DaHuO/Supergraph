def solve(s):
	r = ''
	if len(s) == 1:
		return s
	r = s[0]
	for i in range(1, len(s)):
		if s[i] >= r[0]:
			r = s[i] + r
		else:
			r = r + s[i]
	return r

caseNum = int(raw_input())
for i in range(caseNum):
	print 'Case #%d: %s' % (i+1, solve(raw_input()))