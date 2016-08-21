t = int(raw_input())
for i in range(1, t+1):
	s = raw_input().strip()
	r = s[0]
	for j in range(1, len(s)):
		if s[j] < r[0]:
			r += s[j]
		else:
			r = s[j] + r
	print "Case #" + str(i) +":", r
	