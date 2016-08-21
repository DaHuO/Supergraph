T = int(raw_input())
for i in range(T):
	S = raw_input()
	ans = S[0]
	for j in range(1, len(S)):
		if ans[0] > S[j]:
			ans += S[j]
		else:
			ans = S[j] + ans
	print "Case #%d: %s" % ((i+1), ans)