t = int(raw_input())
for c in range(1, t + 1):
	s = raw_input()
	out = [s[0]];
	for i in range(len(s) - 1):
		if s[i+1] >= out[0]:
			out = list(s[i+1]) + out
		else:
			out = out + list(s[i+1])
	print 'Case #%d: %s' % (c, ''.join(out))