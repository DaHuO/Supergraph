T = int(raw_input())
for kase in range(1, T + 1):
	n = int(raw_input())
	digits = set()
	ans = "INSOMNIA"
	for lv in range(1, 10000000):
		cur = n * lv
		while cur > 0:
			digits.add(cur % 10)
			cur /= 10
		if len(digits) == 10:
			ans = n * lv
			break

	print "Case #" + str(kase) + ": " + str(ans)