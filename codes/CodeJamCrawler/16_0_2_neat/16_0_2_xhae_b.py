T = int(raw_input())
for kase in range(1, T + 1):
	s = raw_input()
	ans = 0
	while True:
		finished = True
		for ch in s:
			if ch == '-':
				finished = False
		if finished:
			break

		while s[-1] == '+':
			s = s[:-1]

		backlen = 0
		ind = len(s) - 1
		while ind >= 0:
			if s[ind] == '-':
				backlen += 1
				ind -= 1
			else:
				break

		ind = 0
		while ind < backlen:
			if s[ind] == '+':
				pend = ind
				while pend < len(s):
					if s[pend] == '+':
						pend += 1
					else:
						break
				ans += 1
				if ind > 0:
					ans += 1
				s = '-' * pend + s[pend:]
				ind = pend
			else:
				ind += 1

		news = ''
		for ch in s:
			if ch == '-':
				news = '+' + news
			else:
				news = '-' + news
		s = news
		ans += 1

	print 'Case #' + str(kase) + ': ' + str(ans)