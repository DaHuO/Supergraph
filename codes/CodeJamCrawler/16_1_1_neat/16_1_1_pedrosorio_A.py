def solve(S):
	cur = S[0]
	for i in xrange(1, len(S)):
		if ord(S[i]) >= ord(cur[0]):
			cur = S[i] + cur
		else:
			cur = cur + S[i]
	return cur


T = int(raw_input())
for case in range(1, T+1):
	S = raw_input()
	print "Case #{}: {}".format(case, str(solve(S)))