import sys

def answer(x):
	count = 1
	prev = x[0]
	last = ''
	m_flag = False if x[0] == '+' else True
	for i in range(1, len(x)):
		if x[i] == '-':
			m_flag = True
		if not x[i] == prev:
			count += 1
			last = x[i]
		prev = x[i]
	if last == '+':
		count -= 1
	return count if m_flag else 0

data = sys.stdin
i = 1
for line in data.readlines()[1:]:
	print "Case #{}: {}".format(i, answer(line.rstrip('\n')))
	i += 1