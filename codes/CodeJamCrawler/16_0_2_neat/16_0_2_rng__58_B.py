def func(s):
	n = len(s)
	ans = 0
	for i in range(n-1):
		if s[i] != s[i+1]:
			ans = ans + 1
	return ans

T = input()

for t in range(T):
	s = raw_input()
	print "Case #" + str(t + 1) + ": " + str(func(s + "+"))
