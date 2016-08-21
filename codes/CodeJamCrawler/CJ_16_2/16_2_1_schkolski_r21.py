filename = 'A-large.in'
dd = {
	'Z': ('ZERO', 0),
	'W': ('TWO', 2),
	'U': ('FOUR', 4),
	'X': ('SIX', 6),
	'G': ('EIGHT', 8)
}
dd1 = {
	'O': ('ONE', 1),
	'T': ('THREE', 3),
	'F': ('FIVE', 5),
	'S': ('SEVEN', 7)
}

def solve(s):
	
	d = {}
	for c in s:
		d[c] = d.get(c, 0) + 1
	res = []

	for key in dd:
		n = d.get(key, 0)

		if n > 0:
			for c in dd[key][0]:
				d[c] -= n
			res.extend([dd[key][1]] * n)

	for key in dd1:
		n = d.get(key, 0)
		if n > 0:
			for c in dd1[key][0]:
				d[c] -= n
			res.extend([dd1[key][1]] * n)

	if d.get('N', 0) > 0:
		n = d['N'] / 2
		res.extend([9] * n)		

	res.sort()
	return ''.join([str(elem) for elem in res])


t = 0
for i, line in enumerate(open(filename)):
	if i == 0:
		t = int(line)
	else:
		print 'Case #{0}: {1}'.format(i, solve(line))
