rf = open('A-large.in', 'r')
wf = open('A-large.out', 'w')

cases = int(rf.readline())

for case in range(1, cases + 1):
	digits = [False] * 10
	n = int(rf.readline())
	if n == 0:
		wf.write('Case #%s: INSOMNIA\n' % case)
		continue
	for i in range(1, 999999):
		cur = n * i
		for c in str(cur):
			digits[int(c)] = True
		if all(digits):
			wf.write('Case #%s: %s\n' % (case, cur))
			break