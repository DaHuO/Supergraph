t = int(input())

for test in range(t):
	s = input().strip()

	ans = 0
	while 1:
		i = 1
		while i < len(s) and s[i] == s[i - 1]:
			i += 1
		if i == len(s):
			if s[0] == '-':
				ans += 1
			break
		t = '-'
		if s[0] == '-':
			t = '+'
		s = t * i + s[i:]
		ans += 1	
	print('Case #%d: %d' % (test + 1, ans))	