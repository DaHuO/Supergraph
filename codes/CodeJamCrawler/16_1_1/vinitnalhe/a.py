m = 10**6 + 1

def solve(s):
	ans = s[0]
	for i in s[1:]:
		if i>= ans[0]:
			ans = i+ans
		else:
			ans = ans + i
	return ans
	
t = int(raw_input())
for caseNr in xrange(1, t+1):
	s = raw_input()
	print("Case #%i: %s" % (caseNr, solve(s)))




