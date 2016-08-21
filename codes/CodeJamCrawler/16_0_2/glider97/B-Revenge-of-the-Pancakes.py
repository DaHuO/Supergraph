import re
import sys

def flip(s, i):
	i = int(i)
	t = []
	for x in range(i-1,-1,-1):
		y = '+' if s[x]=='-' else '-'
		t.append(y)
	for x in s[i:]:
		t.append(x)
	return ''.join(t)

def rev(s):
	return ''.join(['+' if i=='-' else '-' for i in s])

def intelliflip(s):
	plus 		 = re.compile('\++')
	minus 		 = re.compile('-+')
	top_is_plus  = plus.match(s)
	top_is_minus = minus.match(s)

	if top_is_plus:
		if top_is_plus.end() == len(s):
			# Stack is happy side up.
			return 0
		if minus.search(s) and top_is_plus.end() == minus.search(s).start() and minus.search(s).end() == len(s):
			# Part of stack from top is happy side up, the rest is blank side up.
			return 2

	if top_is_minus:
		if top_is_minus.end() == len(s):
			# Stack is blank side up.
			return 1
		if plus.search(s) and top_is_minus.end() == plus.search(s).start() and plus.search(s).end() == len(s):
			# Part of stack from top is blank side up, the rest is happy side up.
			return 1

	if s[-1] == '-':
		return intelliflip(rev(s)) + 1

	counter = 0
	while '-' in s:
		top_is_plus  = plus.match(s)
		s = flip(s, s.find('-' if top_is_plus else '+'))
		counter += 1
	return counter

infile = sys.argv[1]
with open(infile) as f:
	t = int(f.readline())
	for x in xrange(t):
		res = intelliflip(f.readline())
		with open(infile[:-2] + 'out', 'a') as g:
			g.write("Case #" + str(x + 1) + ': ' + str(res) + '\n')
