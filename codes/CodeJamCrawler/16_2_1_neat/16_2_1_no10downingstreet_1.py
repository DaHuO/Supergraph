from collections import defaultdict

def solve(S):
	res = []
	d = defaultdict(int)
	for i in S:
		d[i] += 1

	for i in S:
		if i == 'W':	
			res.append(2)
			d['T'] -= 1
			d['W'] -= 1
			d['O'] -= 1
		elif i == 'U':
			res.append(4)
			d['F'] -= 1
			d['O'] -= 1
			d['U'] -= 1  	
			d['R'] -= 1
		elif i == 'X':
			res.append(6)
			d['S'] -= 1
			d['I'] -= 1
			d['X'] -= 1
		elif i == 'G':
			res.append(8)
			d['E'] -= 1
			d['I'] -= 1
			d['G'] -= 1
			d['H'] -= 1
			d['T'] -= 1
		elif i == 'Z':
			res.append(0)
			d['E'] -= 1
			d['R'] -= 1
			d['O'] -= 1
			d['Z'] -= 1

	one = d['O']
	for i in xrange(one):
		res.append(1)
		d['O'] -= 1
		d['N'] -= 1
		d['E'] -= 1

	three = d['T']	
	for i in xrange(three):
		res.append(3)
		d['T'] -= 1
		d['H'] -= 1
		d['R'] -= 1
		d['E'] -= 1
		d['E'] -= 1

	five = d['F']
	for i in xrange(five):
		res.append(5)
		d['F'] -= 1
		d['I'] -= 1
		d['V'] -= 1
		d['E'] -= 1

	seven = d['S']
	for i in xrange(seven):
		res.append(7)
		d['S'] -= 1
		d['E'] -= 1
		d['V'] -= 1
		d['E'] -= 1
		d['N'] -= 1

	nine = d['I']
	for i in xrange(nine):
		res.append(9)
		d['N'] -= 1
		d['I'] -= 1
		d['N'] -= 1
		d['E'] -= 1

	res.sort()		
	return ''.join(str(x) for x in res)


T = input()
for t in xrange(1, T+1):
	S = raw_input()
	print "Case #{0}: {1}".format(t, solve(S))











