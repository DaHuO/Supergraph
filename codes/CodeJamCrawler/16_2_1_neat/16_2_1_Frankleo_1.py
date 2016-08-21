import collections
def getNum(s):
	d = collections.defaultdict(int)
	s_dict = collections.defaultdict(int)
	res = []

	for i in xrange(len(s)):
		s_dict[s[i]] += 1

	z_num = s_dict['Z']
	u_num = s_dict['U']
	x_num = s_dict['X']
	g_num = s_dict['G']

	for z in xrange(z_num):
		s_dict['Z'] -= 1
		s_dict['E'] -= 1
		s_dict['R'] -= 1
		s_dict['O'] -= 1
		d[0] += 1
	for u in xrange(u_num):
		s_dict['F'] -= 1
		s_dict['O'] -= 1
		s_dict['U'] -= 1
		s_dict['R'] -= 1
		d[4] += 1
	for x in xrange(x_num):
		s_dict['S'] -= 1
		s_dict['I'] -= 1
		s_dict['X'] -= 1
		d[6] += 1
	for g in xrange(g_num):
		s_dict['E'] -= 1
		s_dict['I'] -= 1
		s_dict['G'] -= 1
		s_dict['H'] -= 1
		s_dict['T'] -= 1
		d[8] += 1

	h_num = s_dict['H']
	f_num = s_dict['F']
	s_num = s_dict['S']
	w_num = s_dict['W']

	for h in xrange(h_num):
		s_dict['T'] -= 1
		s_dict['H'] -= 1
		s_dict['R'] -= 1
		s_dict['E'] -= 2
		d[3] += 1
	for f in xrange(f_num):
		s_dict['F'] -= 1
		s_dict['I'] -= 1
		s_dict['V'] -= 1
		s_dict['E'] -= 1
		d[5] += 1
	for s in xrange(s_num):
		s_dict['S'] -= 1
		s_dict['E'] -= 2
		s_dict['V'] -= 1
		s_dict['N'] -= 1
		d[7] += 1
	for w in xrange(w_num):
		s_dict['T'] -= 1
		s_dict['W'] -= 1
		s_dict['O'] -= 1
		d[2] += 1

	o_num = s_dict['O']

	for o in xrange(o_num):
		s_dict['O'] -= 1
		s_dict['N'] -= 1
		s_dict['E'] -= 1
		d[1] += 1

	i_num = s_dict['I']
	for i in xrange(i_num):
		d[9] += 1


	for i in xrange(0, 10):
		for j in xrange(d[i]):
			res.append(i)

	return ''.join(str(x) for x in sorted(res))




t = int(raw_input())
for i in xrange(t):
	s = raw_input()
	print 'Case #%s: %s'%(i+1, getNum(s))
