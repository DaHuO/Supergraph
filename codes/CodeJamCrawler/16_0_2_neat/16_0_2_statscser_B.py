out = open('outputB_l.txt', 'w')
with open('B-large.in', 'r') as f:
	T = int(f.readline())
	for i in range(1, T+1):
		out.write('Case #%s: ' % i)
		s = f.readline().strip()
		count = 1
		curr = s[0]
		for i in range(1, len(s)):
			if s[i] != curr:
				count += 1
				curr = s[i]
		if s[-1] == '+':
			count -= 1
		out.write('%s\n' % count)

out.close()

