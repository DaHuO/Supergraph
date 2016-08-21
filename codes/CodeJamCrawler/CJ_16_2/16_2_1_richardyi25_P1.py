from sys import stdin
from collections import Counter
cin = lambda: stdin.readline().strip('\r\n ')
t = int(cin())

for i in range(t):
	s = Counter(cin())
	num = ''
	if 'Z' in s:
		n = s['Z']
		num += '0' * n
		s['Z'] -= n
		s['E'] -= n
		s['R'] -= n
		s['O'] -= n
	if 'W' in s:
		n = s['W']
		num += '2' * n
		s['T'] -= n
		s['W'] -= n
		s['O'] -= n
	if 'U' in s:
		n = s['U']
		num += '4' * n
		s['F'] -= n
		s['O'] -= n
		s['U'] -= n
		s['R'] -= n
	if 'X' in s:
		n = s['X']
		num += '6' * n
		s['S'] -= n
		s['I'] -= n
		s['X'] -= n
	if 'G' in s:
		n = s['G']
		num += '8' * n
		s['E'] -= n
		s['I'] -= n
		s['G'] -= n
		s['H'] -= n
		s['T'] -= n
	if 'O' in s:
		n = s['O']
		num += '1' * n
		s['O'] -= n
		s['N'] -= n
		s['E'] -= n
	if 'T' in s:
		n = s['T']
		num += '3' * n
		s['T'] -= n
		s['H'] -= n
		s['R'] -= n
		s['E'] -= (n * 2)
	if 'F' in s:
		n = s['F']
		num += '5' * n
		s['F'] -= n
		s['I'] -= n
		s['V'] -= n
		s['E'] -= n
	if 'S' in s:
		n = s['S']
		num += '7' * n
		s['S'] -= n
		s['E'] -= (n * 2)
		s['V'] -= n
		s['N'] -= n
	if 'N' in s:
		n = s['N']
		num += '9' * (n/2)
	
	print "Case #%i: %s" % (i+1, "".join(sorted(num)))